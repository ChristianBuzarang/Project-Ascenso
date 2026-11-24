# Graph Report - Project_Ascend_Web  (2026-11-24)

## Corpus Check
- 74 files · ~14,994 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: .css 4, (none) 2)

## Summary
- 293 nodes · 404 edges · 38 communities (12 shown, 26 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 42 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `21d3992e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- AscensionRecord
- user_profile/admin.py
- django_contrib
- register/views.py
- simulation/views.py
- os
- Base HTML Template
- django_db
- [ADR-XXXX] Title: Short Sentence Describing the Decision
- package.json
- home/migrations/__init__.py
- Chart Data
- Chart Data
- setup
- Communities (30 total, 20 thin omitted)
- ModelAdmin
- Profile

## God Nodes (most connected - your core abstractions)
1. `Profile` - 18 edges
2. `AscensionRecord` - 12 edges
3. `Communities (30 total, 20 thin omitted)` - 11 edges
4. `Graph Report - Project_Ascend_Web  (2026-10-17)` - 11 edges
5. `Professional` - 10 edges
6. `Patient` - 9 edges
7. `FearScenario` - 9 edges
8. `ProfessionalAssignment` - 8 edges
9. `AscendAgent` - 8 edges
10. `chart_data_api()` - 8 edges

## Surprising Connections (you probably didn't know these)
- `Structural Verification (Graphify Reference)` --references--> `AscensionRecord`  [INFERRED]
  docs/decisions/template.md → apps/simulation/models.py
- `God Nodes (most connected - your core abstractions)` --references--> `Profile`  [INFERRED]
  docs/code-graph.md → apps/user_profile/models.py
- `Structural Verification (Graphify Reference)` --references--> `AscensionRecord`  [INFERRED]
  docs/decisions/0001-ascension-simulation-coupling.md → apps/simulation/models.py
- `God Nodes (most connected - your core abstractions)` --references--> `FearScenario`  [INFERRED]
  docs/code-graph.md → apps/simulation/models.py
- `Suggested Questions` --references--> `FearScenario`  [INFERRED]
  docs/code-graph.md → apps/simulation/models.py

## Import Cycles
- None detected.

## Communities (38 total, 26 thin omitted)

### Community 0 - "AscensionRecord"
Cohesion: 0.08
Nodes (24): chart_data_api(), home_view(), AscendAgent, AscensionRecord, Meta, end_session_api(), Community Hubs (Navigation), Corpus Check (+16 more)

### Community 1 - "user_profile/admin.py"
Cohesion: 0.12
Nodes (11): Patient, Meta, Professional, Meta, ProfessionalAssignment, Meta, Profile, Meta (+3 more)

### Community 2 - "django_contrib"
Cohesion: 0.11
Nodes (6): HomeConfig, LoginConfig, RegisterConfig, SimulationConfig, UserProfileConfig, UserSettingsConfig

### Community 3 - "register/views.py"
Cohesion: 0.09
Nodes (4): UserSettingsAdmin, UserSettings, Meta, settings_view()

### Community 4 - "simulation/views.py"
Cohesion: 0.10
Nodes (7): FearScenario, Meta, UserDevice, Meta, admin_orm_queries_view(), immersive_room_view(), process_frame_api()

### Community 6 - "Base HTML Template"
Cohesion: 0.15
Nodes (13): End Session, Process Frame, Base HTML Template, Home HTML Template, Login, Login HTML Template, Register, Register HTML Template (+5 more)

### Community 7 - "django_db"
Cohesion: 0.11
Nodes (8): Migration, Migration, Migration, Migration, Migration, Migration, Migration, Migration

### Community 8 - "[ADR-XXXX] Title: Short Sentence Describing the Decision"
Cohesion: 0.22
Nodes (8): [ADR-XXXX] Title: Short Sentence Describing the Decision, Considered Options, Context & Problem Statement, Decision Drivers, Decision Outcome, Negative Consequences / Trade-offs, Positive Consequences, Structural Verification (Graphify Reference)

### Community 11 - "package.json"
Cohesion: 0.33
Nodes (5): devDependencies, tailwindcss, @tailwindcss/cli, tailwindcss, @tailwindcss/cli

### Community 30 - "Communities (30 total, 20 thin omitted)"
Cohesion: 0.18
Nodes (11): Communities (30 total, 20 thin omitted), Community 11 - "package.json", Community 1 - "user_profile/admin.py", Community 29 - "Graph Report - Project_Ascend_Web  (2026-10-16)", Community 2 - "django_contrib", Community 3 - "django_contrib", Community 4 - "AscensionRecord", Community 6 - "Base HTML Template" (+3 more)

### Community 31 - "ModelAdmin"
Cohesion: 0.17
Nodes (8): AscensionRecordAdmin, FearScenarioAdmin, UserDeviceAdmin, PatientAdmin, ProfessionalAdmin, ProfessionalAssignmentAdmin, ProfileAdmin, UserWithRoleAdmin

### Community 34 - "Profile"
Cohesion: 0.12
Nodes (12): EmailAuthenticationForm, login_view(), logout_view(), ExtendedRegistrationForm, Meta, register_view(), Architectural Decisions (ADRs), Architecture Report (+4 more)

## Knowledge Gaps
- **16 isolated node(s):** `tailwindcss`, `@tailwindcss/cli`, `Home`, `Chart Data`, `setup` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 156 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **26 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AscensionRecord` connect `AscensionRecord` to `[ADR-XXXX] Title: Short Sentence Describing the Decision`, `user_profile/admin.py`, `simulation/views.py`?**
  _High betweenness centrality (0.093) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `Profile` (e.g. with `assignment_view()` and `connect_view()`) actually correct?**
  _`Profile` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `tailwindcss`, `@tailwindcss/cli`, `Home` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `AscensionRecord` be split into smaller, more focused modules?**
  _Cohesion score 0.0761904761904762 - nodes in this community are weakly interconnected._
- **Why does `Graph Report - Project_Ascend_Web  (2026-10-17)` connect `AscensionRecord` to `Communities (30 total, 20 thin omitted)`?**
  _High betweenness centrality (0.090) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `AscensionRecord` (e.g. with `God Nodes (most connected - your core abstractions)` and `Suggested Questions`) actually correct?**
  _`AscensionRecord` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Should `user_profile/admin.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11693548387096774 - nodes in this community are weakly interconnected._