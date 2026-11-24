# Graph Report - Project_Ascend_Web  (2026-11-24)

## Corpus Check
- 73 files · ~10,372 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: .css 4, (none) 2)

## Summary
- 268 nodes · 367 edges · 32 communities (12 shown, 20 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 44 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `63e2f9e9`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- ai_agent.py
- user_profile/admin.py
- django_contrib
- register/views.py
- AscensionRecord
- os
- Base HTML Template
- django_db
- [ADR-XXXX] Title: Short Sentence Describing the Decision
- package.json
- home/migrations/__init__.py
- Chart Data
- Chart Data
- setup
- Project Ascend Documentation
- Communities (30 total, 20 thin omitted)
- simulation/admin.py

## God Nodes (most connected - your core abstractions)
1. `Profile` - 15 edges
2. `AscensionRecord` - 15 edges
3. `FearScenario` - 12 edges
4. `Graph Report - Project_Ascend_Web  (2026-10-17)` - 11 edges
5. `Communities (30 total, 20 thin omitted)` - 11 edges
6. `chart_data_api()` - 9 edges
7. `home_view()` - 9 edges
8. `AscendAgent` - 8 edges
9. `Patient` - 8 edges
10. `Professional` - 8 edges

## Surprising Connections (you probably didn't know these)
- `Structural Verification (Graphify Reference)` --references--> `AscensionRecord`  [INFERRED]
  docs/decisions/template.md → apps/simulation/models.py
- `God Nodes (most connected - your core abstractions)` --references--> `AscendAgent`  [INFERRED]
  docs/code-graph.md → apps/simulation/ai_agent.py
- `Surprising Connections (you probably didn't know these)` --references--> `AscendAgent`  [INFERRED]
  docs/code-graph.md → apps/simulation/ai_agent.py
- `God Nodes (most connected - your core abstractions)` --references--> `Profile`  [INFERRED]
  docs/code-graph.md → apps/user_profile/models.py
- `Structural Verification (Graphify Reference)` --references--> `AscensionRecord`  [INFERRED]
  docs/decisions/0001-ascension-simulation-coupling.md → apps/simulation/models.py

## Import Cycles
- None detected.

## Communities (32 total, 20 thin omitted)

### Community 0 - "ai_agent.py"
Cohesion: 0.12
Nodes (3): AscendAgent, immersive_room_view(), process_frame_api()

### Community 1 - "user_profile/admin.py"
Cohesion: 0.10
Nodes (13): PatientAdmin, ProfessionalAdmin, ProfessionalAssignmentAdmin, ProfileAdmin, Patient, Meta, Professional, Meta (+5 more)

### Community 2 - "django_contrib"
Cohesion: 0.11
Nodes (6): HomeConfig, LoginConfig, RegisterConfig, SimulationConfig, UserProfileConfig, UserSettingsConfig

### Community 3 - "register/views.py"
Cohesion: 0.11
Nodes (11): EmailAuthenticationForm, login_view(), logout_view(), ExtendedRegistrationForm, Meta, register_view(), UserSettingsAdmin, UserSettings (+3 more)

### Community 4 - "AscensionRecord"
Cohesion: 0.14
Nodes (18): chart_data_api(), home_view(), AscensionRecord, Meta, FearScenario, Meta, end_session_api(), God Nodes (most connected - your core abstractions) (+10 more)

### Community 6 - "Base HTML Template"
Cohesion: 0.15
Nodes (13): End Session, Process Frame, Base HTML Template, Home HTML Template, Login, Login HTML Template, Register, Register HTML Template (+5 more)

### Community 7 - "django_db"
Cohesion: 0.09
Nodes (7): Migration, Migration, Migration, Migration, Migration, Migration, Migration

### Community 8 - "[ADR-XXXX] Title: Short Sentence Describing the Decision"
Cohesion: 0.22
Nodes (8): [ADR-XXXX] Title: Short Sentence Describing the Decision, Considered Options, Context & Problem Statement, Decision Drivers, Decision Outcome, Negative Consequences / Trade-offs, Positive Consequences, Structural Verification (Graphify Reference)

### Community 11 - "package.json"
Cohesion: 0.33
Nodes (5): devDependencies, tailwindcss, @tailwindcss/cli, tailwindcss, @tailwindcss/cli

### Community 29 - "Project Ascend Documentation"
Cohesion: 0.40
Nodes (5): Architectural Decisions (ADRs), Architecture Report, Project Ascend Documentation, System Architecture, Views and Endpoints

### Community 30 - "Communities (30 total, 20 thin omitted)"
Cohesion: 0.10
Nodes (18): Communities (30 total, 20 thin omitted), Community 11 - "package.json", Community 1 - "user_profile/admin.py", Community 29 - "Graph Report - Project_Ascend_Web  (2026-10-16)", Community 2 - "django_contrib", Community 3 - "django_contrib", Community 4 - "AscensionRecord", Community 6 - "Base HTML Template" (+10 more)

### Community 31 - "simulation/admin.py"
Cohesion: 0.29
Nodes (5): AscensionRecordAdmin, FearScenarioAdmin, UserDeviceAdmin, UserDevice, Meta

## Knowledge Gaps
- **16 isolated node(s):** `tailwindcss`, `@tailwindcss/cli`, `Home`, `Chart Data`, `setup` (+11 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 140 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **20 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `God Nodes (most connected - your core abstractions)` connect `AscensionRecord` to `ai_agent.py`, `user_profile/admin.py`, `Communities (30 total, 20 thin omitted)`?**
  _High betweenness centrality (0.112) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Profile` (e.g. with `register_view()` and `profile_view()`) actually correct?**
  _`Profile` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `tailwindcss`, `@tailwindcss/cli`, `Home` to the rest of the system?**
  _16 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `ai_agent.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11688311688311688 - nodes in this community are weakly interconnected._
- **Why does `AscensionRecord` connect `AscensionRecord` to `ai_agent.py`, `[ADR-XXXX] Title: Short Sentence Describing the Decision`, `simulation/admin.py`?**
  _High betweenness centrality (0.109) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `AscensionRecord` (e.g. with `chart_data_api()` and `home_view()`) actually correct?**
  _`AscensionRecord` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Should `user_profile/admin.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09879032258064516 - nodes in this community are weakly interconnected._