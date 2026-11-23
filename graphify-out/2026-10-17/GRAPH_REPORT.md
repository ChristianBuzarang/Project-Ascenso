# Graph Report - Project_Ascend_Web  (2026-10-17)

## Corpus Check
- 68 files · ~8,050 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: .css 4, (none) 2)

## Summary
- 248 nodes · 329 edges · 30 communities (10 shown, 20 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 40 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `73533263`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- ai_agent.py
- user_profile/admin.py
- django_contrib
- django_contrib
- AscensionRecord
- os
- Base HTML Template
- django_db
- [ADR-XXXX] Title: Short Sentence Describing the Decision
- simulation/admin.py
- package.json
- home/migrations/__init__.py
- Chart Data
- Chart Data
- setup
- Graph Report - Project_Ascend_Web  (2026-10-16)

## God Nodes (most connected - your core abstractions)
1. `AscensionRecord` - 15 edges
2. `FearScenario` - 13 edges
3. `Graph Report - Project_Ascend_Web  (2026-10-16)` - 11 edges
4. `home_view()` - 10 edges
5. `Communities (29 total, 20 thin omitted)` - 10 edges
6. `end_session_api()` - 9 edges
7. `God Nodes (most connected - your core abstractions)` - 9 edges
8. `chart_data_api()` - 8 edges
9. `AscendAgent` - 7 edges
10. `Profile` - 7 edges

## Surprising Connections (you probably didn't know these)
- `Considered Options` --references--> `chart_data_api()`  [INFERRED]
  docs/decisions/0001-ascension-simulation-coupling.md → apps/home/views.py
- `Structural Verification (Graphify Reference)` --references--> `AscensionRecord`  [INFERRED]
  docs/decisions/0001-ascension-simulation-coupling.md → apps/simulation/models.py
- `Structural Verification (Graphify Reference)` --references--> `AscensionRecord`  [INFERRED]
  docs/decisions/template.md → apps/simulation/models.py
- `Decision Outcome` --references--> `chart_data_api()`  [INFERRED]
  docs/decisions/0001-ascension-simulation-coupling.md → apps/home/views.py
- `God Nodes (most connected - your core abstractions)` --references--> `AscendAgent`  [INFERRED]
  docs/code-graph.md → apps/simulation/ai_agent.py

## Import Cycles
- None detected.

## Communities (30 total, 20 thin omitted)

### Community 1 - "user_profile/admin.py"
Cohesion: 0.13
Nodes (13): PatientAdmin, ProfessionalAdmin, ProfessionalAssignmentAdmin, ProfileAdmin, Patient, Meta, Professional, Meta (+5 more)

### Community 2 - "django_contrib"
Cohesion: 0.11
Nodes (6): HomeConfig, LoginConfig, RegisterConfig, SimulationConfig, UserProfileConfig, UserSettingsConfig

### Community 3 - "django_contrib"
Cohesion: 0.07
Nodes (14): login_view(), logout_view(), ExtendedRegistrationForm, Meta, register_view(), UserSettings, Meta, settings_view() (+6 more)

### Community 4 - "AscensionRecord"
Cohesion: 0.14
Nodes (13): chart_data_api(), home_view(), AscensionRecord, Meta, FearScenario, Meta, end_session_api(), immersive_room_view() (+5 more)

### Community 6 - "Base HTML Template"
Cohesion: 0.15
Nodes (13): End Session, Process Frame, Base HTML Template, Home HTML Template, Login, Login HTML Template, Register, Register HTML Template (+5 more)

### Community 7 - "django_db"
Cohesion: 0.23
Nodes (3): Migration, Migration, Migration

### Community 8 - "[ADR-XXXX] Title: Short Sentence Describing the Decision"
Cohesion: 0.22
Nodes (8): [ADR-XXXX] Title: Short Sentence Describing the Decision, Considered Options, Context & Problem Statement, Decision Drivers, Decision Outcome, Negative Consequences / Trade-offs, Positive Consequences, Structural Verification (Graphify Reference)

### Community 9 - "simulation/admin.py"
Cohesion: 0.14
Nodes (6): AscensionRecordAdmin, FearScenarioAdmin, UserDeviceAdmin, UserDevice, Meta, UserSettingsAdmin

### Community 11 - "package.json"
Cohesion: 0.33
Nodes (5): devDependencies, tailwindcss, @tailwindcss/cli, tailwindcss, @tailwindcss/cli

### Community 29 - "Graph Report - Project_Ascend_Web  (2026-10-16)"
Cohesion: 0.08
Nodes (24): Communities (29 total, 20 thin omitted), Community 0 - "simulation/views.py", Community 11 - "package.json", Community 1 - "user_profile/admin.py", Community 2 - "django_contrib", Community 3 - "register/views.py", Community 6 - "Base HTML Template", Community 7 - "django_db" (+16 more)

## Knowledge Gaps
- **16 isolated node(s):** `tailwindcss`, `@tailwindcss/cli`, `Home`, `Chart Data`, `setup` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 129 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **20 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `God Nodes (most connected - your core abstractions)` connect `AscensionRecord` to `ai_agent.py`, `user_profile/admin.py`, `django_contrib`, `Graph Report - Project_Ascend_Web  (2026-10-16)`?**
  _High betweenness centrality (0.119) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `AscensionRecord` (e.g. with `chart_data_api()` and `home_view()`) actually correct?**
  _`AscensionRecord` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `tailwindcss`, `@tailwindcss/cli`, `Home` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `user_profile/admin.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13438735177865613 - nodes in this community are weakly interconnected._
- **Why does `AscensionRecord` connect `AscensionRecord` to `[ADR-XXXX] Title: Short Sentence Describing the Decision`, `simulation/admin.py`, `Graph Report - Project_Ascend_Web  (2026-10-16)`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `FearScenario` (e.g. with `home_view()` and `end_session_api()`) actually correct?**
  _`FearScenario` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Should `django_contrib` be split into smaller, more focused modules?**
  _Cohesion score 0.10526315789473684 - nodes in this community are weakly interconnected._