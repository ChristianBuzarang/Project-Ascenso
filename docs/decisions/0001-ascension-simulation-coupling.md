# [ADR-0001] Decouple Ascension Record Queries from Home Dashboard Rendering

- **Status:** Accepted
- **Date:** 2026-10-17
- **Deciders:** Christian Buzarang

## Context & Problem Statement
The `home_view()` endpoint in `apps/home/views.py` directly coordinates data rendering for user sessions alongside `AscensionRecord` and `FearScenario` simulation states. Direct synchronous queries in the view layer risk bloating response latency as historical simulation records expand.

## Decision Drivers
- Keep view handlers thin and delegate metric calculations to model querysets or service utilities.
- Maintain a clean AST call path verifiable through Graphify.
- Support real-time biometric visualization charting without payload overhead.

## Considered Options
1. **Direct View Aggregation:** Compute averages and scenario histories inline within `apps/home/views.py`.
2. **Dedicated API Contract:** Expose `chart_data_api()` as an isolated JSON endpoint consuming scoped querysets.

## Decision Outcome
Chosen option: **Dedicated API Contract** (`chart_data_api()`). 

### Positive Consequences
- The home page renders its base DOM immediately without waiting for historical metric aggregation.
- Clear separation between UI rendering and analytical JSON payloads.

### Negative Consequences / Trade-offs
- Requires client-side fetch handling on the dashboard.

## Structural Verification (Graphify Reference)
- **Knowledge Graph:** [[code-graph]]
- **Primary Modules:** `apps/home/views.py`, `simulation/models.py`
- **Expected Hop Route:**
  `apps_home_views` -> `AscensionRecord`
[imports]


