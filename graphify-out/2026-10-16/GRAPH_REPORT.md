# Graph Report - Project_Ascend_Web  (2026-10-16)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 209 nodes · 267 edges · 29 communities (9 shown, 20 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 15 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `38fffb07`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- simulation/views.py
- user_profile/admin.py
- django_contrib
- register/views.py
- django_apps
- os
- Base HTML Template
- django_db
- simulation/admin.py
- django_test
- package.json
- home/migrations/__init__.py
- Chart Data
- Chart Data
- setup

## God Nodes (most connected - your core abstractions)
1. `AscensionRecord` - 9 edges
2. `FearScenario` - 9 edges
3. `AscendAgent` - 6 edges
4. `Profile` - 6 edges
5. `UserSettings` - 6 edges
6. `home_view()` - 6 edges
7. `end_session_api()` - 6 edges
8. `process_frame_api()` - 6 edges
9. `Base HTML Template` - 6 edges
10. `Project Ascend Documentation` - 5 edges

## Surprising Connections (you probably didn't know these)
- `chart_data_api()` --uses--> `AscensionRecord`  [INFERRED]
  apps/home/views.py → apps/simulation/models.py
- `home_view()` --uses--> `AscensionRecord`  [INFERRED]
  apps/home/views.py → apps/simulation/models.py
- `end_session_api()` --uses--> `AscensionRecord`  [INFERRED]
  apps/simulation/views.py → apps/simulation/models.py
- `home_view()` --uses--> `FearScenario`  [INFERRED]
  apps/home/views.py → apps/simulation/models.py
- `end_session_api()` --uses--> `FearScenario`  [INFERRED]
  apps/simulation/views.py → apps/simulation/models.py

## Import Cycles
- None detected.

## Communities (29 total, 20 thin omitted)

### Community 0 - "simulation/views.py"
Cohesion: 0.08
Nodes (10): chart_data_api(), home_view(), AscendAgent, AscensionRecord, Meta, FearScenario, Meta, end_session_api() (+2 more)

### Community 1 - "user_profile/admin.py"
Cohesion: 0.13
Nodes (13): PatientAdmin, ProfessionalAdmin, ProfessionalAssignmentAdmin, ProfileAdmin, Patient, Meta, Professional, Meta (+5 more)

### Community 2 - "django_contrib"
Cohesion: 0.11
Nodes (6): HomeConfig, LoginConfig, RegisterConfig, SimulationConfig, UserProfileConfig, UserSettingsConfig

### Community 3 - "register/views.py"
Cohesion: 0.14
Nodes (4): UserSettingsAdmin, UserSettings, Meta, settings_view()

### Community 6 - "Base HTML Template"
Cohesion: 0.15
Nodes (13): End Session, Process Frame, Base HTML Template, Home HTML Template, Login, Login HTML Template, Register, Register HTML Template (+5 more)

### Community 7 - "django_db"
Cohesion: 0.23
Nodes (3): Migration, Migration, Migration

### Community 8 - "simulation/admin.py"
Cohesion: 0.20
Nodes (9): ExtendedRegistrationForm, Meta, register_view(), Architectural Decisions (ADRs), Architecture Report, Django, Project Ascend Documentation, System Architecture (+1 more)

### Community 9 - "django_test"
Cohesion: 0.31
Nodes (5): AscensionRecordAdmin, FearScenarioAdmin, UserDeviceAdmin, UserDevice, Meta

### Community 11 - "package.json"
Cohesion: 0.33
Nodes (5): devDependencies, tailwindcss, @tailwindcss/cli, tailwindcss, @tailwindcss/cli

## Knowledge Gaps
- **16 isolated node(s):** `tailwindcss`, `@tailwindcss/cli`, `Home`, `Chart Data`, `setup` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 105 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **20 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AscensionRecord` connect `simulation/views.py` to `django_test`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `AscensionRecord` (e.g. with `chart_data_api()` and `home_view()`) actually correct?**
  _`AscensionRecord` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `tailwindcss`, `@tailwindcss/cli`, `Home` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `simulation/views.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08408408408408409 - nodes in this community are weakly interconnected._
- **Are the 3 inferred relationships involving `FearScenario` (e.g. with `home_view()` and `end_session_api()`) actually correct?**
  _`FearScenario` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `user_profile/admin.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12681159420289856 - nodes in this community are weakly interconnected._
- **Should `django_contrib` be split into smaller, more focused modules?**
  _Cohesion score 0.10526315789473684 - nodes in this community are weakly interconnected._