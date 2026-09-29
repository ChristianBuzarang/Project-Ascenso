import json
import base64
import numpy as np
import cv2

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .ai_agent import AscendAgent
from .models import AscensionRecord, FearScenario

# Initialize our agent globally
agent = AscendAgent()

# We keep Levels hardcoded since they belong to the Michael's Consortium framework
FEAR_LEVELS = {
    "1": "Level 1: Apprehension",
    "2": "Level 2: Denial",
    "3": "Level 3: Fright",
    "4": "Level 4: Retreat",
    "5": "Level 5: Terror",
    "6": "Level 6: Numbness",
    "7": "Level 7: Apathy",
}

FEAR_THRESHOLDS = {"1": 95, "2": 110, "3": 120, "4": 135, "5": 150, "6": 165, "7": 180}


@login_required(login_url="login:login")
def immersive_room_view(request):
    # Get the Database ID from the URL (e.g., ?scenario=1)
    scenario_id = request.GET.get("scenario")
    level_key = request.GET.get("level", "5")

    try:
        # Fetch the exact video and name from your Database!
        scenario_obj = FearScenario.objects.get(id=scenario_id)
        scenario_name = scenario_obj.name
        scenario_media = scenario_obj.media_file
    except (FearScenario.DoesNotExist, ValueError):
        scenario_name = "[System Error] Unknown Protocol"
        scenario_media = ""

    context = {
        "scenario_id": scenario_id,  # Pass ID to HTML so it can save it later
        "scenario_name": scenario_name,
        "scenario_media": scenario_media,
        "target_level_name": FEAR_LEVELS.get(level_key, "Level 5: Panic"),
        "target_hr": FEAR_THRESHOLDS.get(level_key, 150),
    }
    return render(request, "simulation/immersive.html", context)


@csrf_exempt
def process_frame_api(request):
    if request.method == "POST":
        data = json.loads(request.body)

        img_data = base64.b64decode(data["image"].split(",")[1])
        np_arr = np.frombuffer(img_data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        prev_fear = float(data.get("current_fear", 10.0))
        last_center = data.get("last_center", None)
        scenario_name = data.get("scenario_name")
        level_name = data.get("level_name")
        target_hr = float(data.get("target_hr", 150))

        current_fear_cv, new_center = agent.analyze_frame(frame, prev_fear, last_center)
        simulated_hr = 70 + (current_fear_cv * 1.0) + np.random.normal(0, 2)
        predicted_state = agent.perceive(simulated_hr, 100 - current_fear_cv, 80, 2.0)

        response_data = {
            "fear_score": current_fear_cv,
            "heart_rate": simulated_hr,
            "new_center": new_center,
            "intervention_script": None,
            "audio_url": None,
        }

        if simulated_hr >= target_hr:
            script, audio_url = agent.actuate_override(scenario_name, level_name)
            response_data["intervention_script"] = script
            response_data["audio_url"] = audio_url

        return JsonResponse(response_data)


@csrf_exempt
def end_session_api(request):
    """Saves the final session data to the Supabase Database when the user exits"""
    if request.method == "POST":
        data = json.loads(request.body)

        if request.user.is_authenticated:
            try:
                # Find the scenario object so we can link it as a Foreign Key
                scenario_obj = FearScenario.objects.get(id=data.get("scenario_id"))
            except FearScenario.DoesNotExist:
                scenario_obj = None

            AscensionRecord.objects.create(
                user=request.user,
                scenario=scenario_obj,  # Saves the exact scenario from the DB!
                target_level=data.get("target_level", "Unknown"),
                peak_hr=data.get("peak_hr", 70.0),
                end_hr=data.get("end_hr", 70.0),
            )

        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "failed"}, status=400)
