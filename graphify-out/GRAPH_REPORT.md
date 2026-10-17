# Graph Report - Project_Ascend_Web  (2026-10-16)

## Corpus Check
- 66 files · ~7,702 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: .css 4, (none) 2)

## Summary
- 230 nodes · 305 edges · 30 communities (11 shown, 19 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 33 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b0b6cd7d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- simulation/views.py
- user_profile/admin.py
- django_contrib
- django_contrib
- AscensionRecord
- os
- Base HTML Template
- django_db
- Project Ascend Documentation
- django_test
- package.json
- home/migrations/__init__.py
- Chart Data
- Chart Data
- setup
- Graph Report - Project_Ascend_Web  (2026-10-16)

## God Nodes (most connected - your core abstractions)
1. `AscensionRecord` - 12 edges
2. `FearScenario` - 12 edges
3. `Graph Report - Project_Ascend_Web  (2026-10-16)` - 11 edges
4. `Communities (29 total, 20 thin omitted)` - 10 edges
5. `God Nodes (most connected - your core abstractions)` - 9 edges
6. `home_view()` - 9 edges
7. `end_session_api()` - 9 edges
8. `AscendAgent` - 7 edges
9. `Profile` - 7 edges
10. `UserSettings` - 7 edges

## Surprising Connections (you probably didn't know these)
- `God Nodes (most connected - your core abstractions)` --references--> `AscendAgent`  [INFERRED]
  docs/code-graph.md → apps/simulation/ai_agent.py
- `God Nodes (most connected - your core abstractions)` --references--> `process_frame_api()`  [INFERRED]
  docs/code-graph.md → apps/simulation/views.py
- `God Nodes (most connected - your core abstractions)` --references--> `Profile`  [INFERRED]
  docs/code-graph.md → apps/user_profile/models.py
- `God Nodes (most connected - your core abstractions)` --references--> `UserSettings`  [INFERRED]
  docs/code-graph.md → apps/user_settings/models.py
- `God Nodes (most connected - your core abstractions)` --references--> `home_view()`  [INFERRED]
  docs/code-graph.md → apps/home/views.py

## Import Cycles
- None detected.

## Communities (30 total, 19 thin omitted)

### Community 0 - "simulation/views.py"
Cohesion: 0.11
Nodes (3): AscendAgent, immersive_room_view(), process_frame_api()

### Community 1 - "user_profile/admin.py"
Cohesion: 0.11
Nodes (13): PatientAdmin, ProfessionalAdmin, ProfessionalAssignmentAdmin, ProfileAdmin, Patient, Meta, Professional, Meta (+5 more)

### Community 2 - "django_contrib"
Cohesion: 0.11
Nodes (6): HomeConfig, LoginConfig, RegisterConfig, SimulationConfig, UserProfileConfig, UserSettingsConfig

### Community 3 - "django_contrib"
Cohesion: 0.08
Nodes (9): login_view(), logout_view(), ExtendedRegistrationForm, Meta, register_view(), UserSettingsAdmin, UserSettings, Meta (+1 more)

### Community 4 - "AscensionRecord"
Cohesion: 0.22
Nodes (10): chart_data_api(), home_view(), AscensionRecord, Meta, FearScenario, Meta, end_session_api(), God Nodes (most connected - your core abstractions) (+2 more)

### Community 6 - "Base HTML Template"
Cohesion: 0.15
Nodes (13): End Session, Process Frame, Base HTML Template, Home HTML Template, Login, Login HTML Template, Register, Register HTML Template (+5 more)

### Community 7 - "django_db"
Cohesion: 0.23
Nodes (3): Migration, Migration, Migration

### Community 8 - "Project Ascend Documentation"
Cohesion: 0.33
Nodes (6): Architectural Decisions (ADRs), Architecture Report, Django, Project Ascend Documentation, System Architecture, Views and Endpoints

### Community 9 - "django_test"
Cohesion: 0.33
Nodes (5): AscensionRecordAdmin, FearScenarioAdmin, UserDeviceAdmin, UserDevice, Meta

### Community 11 - "package.json"
Cohesion: 0.33
Nodes (5): devDependencies, tailwindcss, @tailwindcss/cli, tailwindcss, @tailwindcss/cli

### Community 29 - "Graph Report - Project_Ascend_Web  (2026-10-16)"
Cohesion: 0.11
Nodes (17): Communities (29 total, 20 thin omitted), Community 0 - "simulation/views.py", Community 11 - "package.json", Community 1 - "user_profile/admin.py", Community 2 - "django_contrib", Community 3 - "register/views.py", Community 6 - "Base HTML Template", Community 7 - "django_db" (+9 more)

## Knowledge Gaps
- **16 isolated node(s):** `tailwindcss`, `@tailwindcss/cli`, `Home`, `Chart Data`, `setup` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 121 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **19 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `God Nodes (most connected - your core abstractions)` connect `AscensionRecord` to `simulation/views.py`, `user_profile/admin.py`, `django_contrib`, `Graph Report - Project_Ascend_Web  (2026-10-16)`?**
  _High betweenness centrality (0.121) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `AscensionRecord` (e.g. with `chart_data_api()` and `home_view()`) actually correct?**
  _`AscensionRecord` has 6 INFERRED edges - model-reasoned connections that need verification._
- **What connects `tailwindcss`, `@tailwindcss/cli`, `Home` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `simulation/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10507246376811594 - nodes in this community are weakly interconnected._
- **Why does `Graph Report - Project_Ascend_Web  (2026-10-16)` connect `Graph Report - Project_Ascend_Web  (2026-10-16)` to `AscensionRecord`?**
  _High betweenness centrality (0.101) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `FearScenario` (e.g. with `home_view()` and `end_session_api()`) actually correct?**
  _`FearScenario` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Should `user_profile/admin.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11384615384615385 - nodes in this community are weakly interconnected._