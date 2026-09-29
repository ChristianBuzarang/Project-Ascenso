import json
import base64
import numpy as np
import cv2
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .ai_agent import AscendAgent
from .models import AscensionRecord

# Initialize our agent globally
agent = AscendAgent()

FEAR_SCENARIOS = {
    "darkness": {
        "name": "[Primal] Fear of Darkness",
        "gif": "https://media1.tenor.com/m/7aX9v2wQx8IAAAAd/creepy-dark.gif",
    },
    "spiders": {
        "name": "[Primal] Fear of Spiders",
        "gif": "https://media1.tenor.com/m/BvP_1O83Ew8AAAAd/spider-jump.gif",
    },
    "public_speaking": {
        "name": "[Social] Public Speaking",
        "gif": "https://media1.tenor.com/m/9e9W2n4XNjgAAAAd/crowd-staring.gif",
    },
    "unknown": {
        "name": "[Existential] The Unknown",
        "gif": "https://media1.tenor.com/m/0o_8z2l4L70AAAAd/trippy-abstract.gif",
    },
}

FEAR_LEVELS = {
    "1": "Level 1: Apprehension",
    "3": "Level 3: Fright",
    "5": "Level 5: Panic",
    "7": "Level 7: Collapse",
}
FEAR_THRESHOLDS = {"1": 95, "3": 120, "5": 150, "7": 180}


@login_required(login_url="login:login")
def immersive_room_view(request):
    scenario_key = request.GET.get("scenario", "unknown")
    level_key = request.GET.get("level", "5")

    context = {
        "scenario_name": FEAR_SCENARIOS[scenario_key]["name"],
        "scenario_gif": FEAR_SCENARIOS[scenario_key]["gif"],
        "target_level_name": FEAR_LEVELS[level_key],
        "target_hr": FEAR_THRESHOLDS[level_key],
    }
    return render(request, "simulation/immersive.html", context)


@csrf_exempt
def process_frame_api(request):
    """The browser sends webcam snapshots here every 1 second (Now perfectly thread-safe)"""
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
    if request.method == "POST":
        data = json.loads(request.body)
        if request.user.is_authenticated:
            AscensionRecord.objects.create(
                user=request.user,
                scenario=data.get("scenario", "Unknown"),
                target_level=data.get("target_level", "Unknown"),
                peak_hr=data.get("peak_hr", 70.0),
                end_hr=data.get("end_hr", 70.0),
            )
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "failed"}, status=400)
