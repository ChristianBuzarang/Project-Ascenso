# Graph Report - Project_Ascend_Web  (2026-10-17)

## Corpus Check
- 68 files · ~8,211 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: .css 4, (none) 2)

## Summary
- 249 nodes · 327 edges · 32 communities (12 shown, 20 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 37 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e1846cf4`
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
- django_contrib
- package.json
- home/migrations/__init__.py
- Chart Data
- Chart Data
- setup
- Graph Report - Project_Ascend_Web  (2026-10-16)
- Communities (30 total, 20 thin omitted)
- simulation/admin.py

## God Nodes (most connected - your core abstractions)
1. `AscensionRecord` - 15 edges
2. `FearScenario` - 12 edges
3. `Graph Report - Project_Ascend_Web  (2026-10-17)` - 11 edges
4. `Communities (30 total, 20 thin omitted)` - 11 edges
5. `chart_data_api()` - 9 edges
6. `home_view()` - 9 edges
7. `God Nodes (most connected - your core abstractions)` - 8 edges
8. `AscendAgent` - 8 edges
9. `end_session_api()` - 8 edges
10. `Profile` - 7 edges

## Surprising Connections (you probably didn't know these)
- `Structural Verification (Graphify Reference)` --references--> `AscensionRecord`  [INFERRED]
  docs/decisions/0001-ascension-simulation-coupling.md → apps/simulation/models.py
- `Structural Verification (Graphify Reference)` --references--> `AscensionRecord`  [INFERRED]
  docs/decisions/template.md → apps/simulation/models.py
- `Considered Options` --references--> `chart_data_api()`  [INFERRED]
  docs/decisions/0001-ascension-simulation-coupling.md → apps/home/views.py
- `God Nodes (most connected - your core abstractions)` --references--> `AscendAgent`  [INFERRED]
  docs/code-graph.md → apps/simulation/ai_agent.py
- `God Nodes (most connected - your core abstractions)` --references--> `Profile`  [INFERRED]
  docs/code-graph.md → apps/user_profile/models.py

## Import Cycles
- None detected.

## Communities (32 total, 20 thin omitted)

### Community 1 - "user_profile/admin.py"
Cohesion: 0.13
Nodes (13): PatientAdmin, ProfessionalAdmin, ProfessionalAssignmentAdmin, ProfileAdmin, Patient, Meta, Professional, Meta (+5 more)

### Community 2 - "django_contrib"
Cohesion: 0.11
Nodes (6): HomeConfig, LoginConfig, RegisterConfig, SimulationConfig, UserProfileConfig, UserSettingsConfig

### Community 3 - "django_contrib"
Cohesion: 0.09
Nodes (11): login_view(), logout_view(), ExtendedRegistrationForm, Meta, register_view(), Architectural Decisions (ADRs), Architecture Report, Django (+3 more)

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

### Community 9 - "django_contrib"
Cohesion: 0.13
Nodes (4): UserSettingsAdmin, UserSettings, Meta, settings_view()

### Community 11 - "package.json"
Cohesion: 0.33
Nodes (5): devDependencies, tailwindcss, @tailwindcss/cli, tailwindcss, @tailwindcss/cli

### Community 29 - "Graph Report - Project_Ascend_Web  (2026-10-16)"
Cohesion: 0.12
Nodes (14): Community Hubs (Navigation), Corpus Check, Graph Freshness, Graph Report - Project_Ascend_Web  (2026-10-17), Import Cycles, Knowledge Gaps, Summary, [ADR-0001] Decouple Ascension Record Queries from Home Dashboard Rendering (+6 more)

### Community 30 - "Communities (30 total, 20 thin omitted)"
Cohesion: 0.18
Nodes (11): Communities (30 total, 20 thin omitted), Community 11 - "package.json", Community 1 - "user_profile/admin.py", Community 29 - "Graph Report - Project_Ascend_Web  (2026-10-16)", Community 2 - "django_contrib", Community 3 - "django_contrib", Community 4 - "AscensionRecord", Community 6 - "Base HTML Template" (+3 more)

### Community 31 - "simulation/admin.py"
Cohesion: 0.33
Nodes (5): AscensionRecordAdmin, FearScenarioAdmin, UserDeviceAdmin, UserDevice, Meta

## Knowledge Gaps
- **16 isolated node(s):** `tailwindcss`, `@tailwindcss/cli`, `Home`, `Chart Data`, `setup` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 130 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **20 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AscensionRecord` connect `AscensionRecord` to `[ADR-XXXX] Title: Short Sentence Describing the Decision`, `Graph Report - Project_Ascend_Web  (2026-10-16)`, `simulation/admin.py`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `AscensionRecord` (e.g. with `chart_data_api()` and `home_view()`) actually correct?**
  _`AscensionRecord` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `tailwindcss`, `@tailwindcss/cli`, `Home` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `user_profile/admin.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13438735177865613 - nodes in this community are weakly interconnected._
- **Why does `Graph Report - Project_Ascend_Web  (2026-10-17)` connect `Graph Report - Project_Ascend_Web  (2026-10-16)` to `AscensionRecord`, `Communities (30 total, 20 thin omitted)`?**
  _High betweenness centrality (0.103) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `FearScenario` (e.g. with `home_view()` and `end_session_api()`) actually correct?**
  _`FearScenario` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Should `django_contrib` be split into smaller, more focused modules?**
  _Cohesion score 0.10526315789473684 - nodes in this community are weakly interconnected._