import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from apps.simulation.models import AscensionRecord, FearScenario


FEAR_LEVELS = {
    "1": "Level 1: Apprehension",
    "2": "Level 2: Denial",
    "3": "Level 3: Fright",
    "4": "Level 4: Retreat",
    "5": "Level 5: Terror",
    "6": "Level 6: Numbness",
    "7": "Level 7: Apathy",
}


@login_required(login_url="login:login")
def home_view(request):
    """Loads the Dashboard HTML"""
    records = AscensionRecord.objects.filter(user=request.user)

    scenarios = FearScenario.objects.filter(is_active=True).order_by("category", "name")

    categorized_scenarios = {}
    for s in scenarios:
        if s.category not in categorized_scenarios:
            categorized_scenarios[s.category] = []
        categorized_scenarios[s.category].append({"id": s.id, "name": s.name})

    context = {
        "categories_json": json.dumps(categorized_scenarios),
        "levels": FEAR_LEVELS,
        "has_history": len(records) > 0,
    }
    return render(request, "home/home.html", context)


@login_required(login_url="login:login")
def chart_data_api(request):
    """Silent API endpoint that fetches the Supabase data for the graph"""
    records = AscensionRecord.objects.filter(user=request.user).order_by("timestamp")

    labels = []
    peak_hrs = []
    end_hrs = []

    for i, record in enumerate(records):
        labels.append(f"Session {i + 1}")
        peak_hrs.append(record.peak_hr)
        end_hrs.append(record.end_hr)

    return JsonResponse(
        {
            "has_history": len(records) > 0,
            "chart_labels": labels,
            "chart_peak_hr": peak_hrs,
            "chart_end_hr": end_hrs,
        }
    )
