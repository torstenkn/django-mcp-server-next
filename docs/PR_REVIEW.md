# Upstream PR review queue

Snapshot: 2026-11-14. 5 closed, 8 open, 15 merged. All 28 PR heads and API records preserved.

Review uses original PR heads against PR #70, not a blanket approval. No contribution has been merged into the successor baseline. Priorities: P0 security/baseline, P1 compatibility, P2 feature correctness, P3 docs/optional.

| Original PR | Original status | Author | Priority | Recommendation |
|---|---|---|---|---|
| [#72](https://github.com/gts360/django-mcp-server/pull/72) security: validate $match/$project field paths against allowed_models/exclude_fields | closed | kemrec | P0 | Request changes |
| [#70](https://github.com/gts360/django-mcp-server/pull/70) Migrate to mcp 2.x (MCPServer) | open | torstenkn | P0 | Baseline adopted |
| [#69](https://github.com/gts360/django-mcp-server/pull/69) docs: fix Agent Development Kit typo | open | meichuanyi | P3 | Merge after docs review |
| [#68](https://github.com/gts360/django-mcp-server/pull/68) fix: use Count("pk") to support models with custom primary key (closes #65) | open | gghez | P1 | Merge after targeted regression |
| [#67](https://github.com/gts360/django-mcp-server/pull/67) feat: forward icons parameter to FastMCP (closes #58) | open | gghez | P1 | Adapt and test |
| [#66](https://github.com/gts360/django-mcp-server/pull/66) Enforce ModelQueryToolset.fields as a real output boundary | open | noamblitz | P0 | Request changes |
| [#64](https://github.com/gts360/django-mcp-server/pull/64) Added links for Homepage, Repository, etc for pypi sidebar. | open | kelvinhammond | P3 | Superseded; no duplicate draft |
| [#63](https://github.com/gts360/django-mcp-server/pull/63) feat: add register_drf_filter_tool for django-filter integration | open | harryd31 | P2 | Request changes: security |
| [#61](https://github.com/gts360/django-mcp-server/pull/61) Add AgentRank score badge | closed | superlowburn | P3 | Do not import |
| [#60](https://github.com/gts360/django-mcp-server/pull/60) feat: add DJANGO_MCP_SERVER_CLASS setting to allow custom DjangoMCP subclass | open | Mathias206 | P2 | Request changes |
| [#49](https://github.com/gts360/django-mcp-server/pull/49) Fix typo in pipeline DSL specification | merged | roskakori | — | Already integrated upstream |
| [#45](https://github.com/gts360/django-mcp-server/pull/45) fix: implement server instructions tool | merged | ant-ms | — | Already integrated upstream |
| [#42](https://github.com/gts360/django-mcp-server/pull/42) #33 Fix warning with drf-spectacular | closed | roskakori | P3 | Defer; redesign optional integration |
| [#41](https://github.com/gts360/django-mcp-server/pull/41) Fix/29 settings fields | merged | omarbenhamid | — | Already integrated upstream |
| [#40](https://github.com/gts360/django-mcp-server/pull/40) Fix DRF Integration Body Processing and API Failure Issues | merged | zacharypodbela | — | Already integrated upstream |
| [#38](https://github.com/gts360/django-mcp-server/pull/38) Add Claude local memory files to .gitignore | merged | zacharypodbela | — | Already integrated upstream |
| [#37](https://github.com/gts360/django-mcp-server/pull/37) fix field required bug | closed | anfreshman | P2 | Defer; superseded approach |
| [#31](https://github.com/gts360/django-mcp-server/pull/31) Remove confusing comment | merged | roskakori | — | Already integrated upstream |
| [#28](https://github.com/gts360/django-mcp-server/pull/28) Added a new setting to determine the endpoint | merged | lairdresearch | — | Already integrated upstream |
| [#27](https://github.com/gts360/django-mcp-server/pull/27) fix: request handling improvements | merged | Artui | — | Already integrated upstream |
| [#25](https://github.com/gts360/django-mcp-server/pull/25) Added new command showing all tools, prompts and resources | merged | lairdresearch | — | Already integrated upstream |
| [#23](https://github.com/gts360/django-mcp-server/pull/23) feature: DRF Viewset support | merged | Artui | — | Already integrated upstream |
| [#22](https://github.com/gts360/django-mcp-server/pull/22) Correct secondary MCP usage and update example app | merged | MrMebelMan | — | Already integrated upstream |
| [#18](https://github.com/gts360/django-mcp-server/pull/18) Update README.md with Remote MCP options for claude desktop | closed | rsp2k | P3 | Defer; documentation refresh |
| [#17](https://github.com/gts360/django-mcp-server/pull/17) as discussed in the issue tracker | merged | d3cline | — | Already integrated upstream |
| [#13](https://github.com/gts360/django-mcp-server/pull/13) Fixed: Autodiscovery MCPToolset bug | merged | domlysi | — | Already integrated upstream |
| [#7](https://github.com/gts360/django-mcp-server/pull/7) Fix django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet | merged | chaz-working | — | Already integrated upstream |
| [#6](https://github.com/gts360/django-mcp-server/pull/6) DRF publish list tool | merged | csalom | — | Already integrated upstream |

## Detailed findings

### #72 — P0: Request changes

Partial security fix; reproduced excluded-field leak via $group/$max and search oracle. Validate $group/$sort/$search/$text, pk aliases and relation traversal consistently. No regression tests in contribution. Overlaps #66.

### #66 — P0: Request changes

13 tests pass with #70, but reproduced empty allowed_fields returning all columns. Dotted sources/pk exemptions and aggregate/filter side channels need tests and fail-closed policy. Overlaps #72; reconcile together.

### #70 — P0: Baseline adopted

Original commits are the ancestor of next; no duplicate PR. MCP 2.3.0/Django 5.2: eight original tests plus successor protocol smoke pass. Minimum SDK and HTTP/session/STDIO coverage still required.

### #68 — P1: Merge after targeted regression

Small correct Count(id) -> Count(pk) fix. Clean with #70; eight existing tests pass but lack custom-PK cases. Add UUID/string PK tests for $sum:1 and $count:1. Low security risk; touches same query engine as #66/#72.

### #67 — P1: Adapt and test

Textual conflicts with #70 in constructor and dependencies. Original tests reference _mcp_server and camelCase Icon metadata. Port to MCPServer keyword-only instructions, _lowlevel_server and MCP 2 Icon fields; never downgrade SDK.

### #60 — P2: Request changes

Clean with #70, existing eight tests pass. Custom subclass import during module initialization can produce circular imports (especially documented app.mcp path); non-class values raise TypeError. Add startup/import-order and invalid-setting tests. Settings must remain trusted.

### #63 — P2: Request changes: security

Clean with #70, existing eight tests pass, no feature regression tests. _resolve_queryset falls back to Model.objects.all(), bypassing request-scoped get_queryset; caller directly serializes without view dispatch/permissions. Add request, tenant, permission, negative-limit and filter validation tests before use.

### #64 — P3: Superseded; no duplicate draft

Project URLs/PEP 621 metadata are implemented in successor identity commit with attribution to this proposal. Upstream URLs would point at wrong project. Original branch archived, no duplicate feature PR.

### #69 — P3: Merge after docs review

Documentation spelling only, clean with #70; eight tests pass. Preserve original authorship. No security impact.

### #42 — P3: Defer; redesign optional integration

Schema exclusion useful, but introduces mandatory drf-spectacular dependency. Import cleanup overlaps #70. Require optional integration and schema tests before revival; archived branch only.

### #37 — P2: Defer; superseded approach

Old DRF request monkeypatch predates merged #40; changes initialize_request semantics. Reproduce on current baseline and test authentication/body parsing before revival. No blind replay.

### #18 — P3: Defer; documentation refresh

Historical client/proxy instructions and plan claims require revalidation; avoid importing outdated requirements. Archived branch only.

### #61 — P3: Do not import

Closed promotional badge contribution adds no runtime or maintenance value; archived with attribution.

## Evidence and limits

[Raw compatibility results](compatibility-results.json) record isolated merge-tree and pytest results against #70. #67 was not tested unchanged because it conflicts. Passing the existing tests does not validate new features. [Security probes](security-probes.txt) reproduce #66/#72 failures on isolated combined trees.

Successor tests exercise MCP initialize, tool listing/call, instructions, resources and prompts over in-memory transport. HTTP/ASGI/WSGI sessions, DRF authorization and full supported-version coverage remain release gates. CI matrix tests Python 3.10/3.12/3.13, Django 4.2/5.2 and MCP 2.0/latest 2.x. See GitHub Actions for actual matrix outcomes.

Review order: reconcile #72 + #66 with regression tests; fix compatibility #68 + #67; validate #60 and #63 authorization; then documentation. Original #64 is superseded by successor metadata. Drafts preserve attribution but convey no approval.

## Successor draft queue

| Original | Successor draft | Branch |
|---|---|---|
| #72 | [https://github.com/torstenkn/django-mcp-server-next/pull/1](https://github.com/torstenkn/django-mcp-server-next/pull/1) | `review/upstream-72` |
| #66 | [https://github.com/torstenkn/django-mcp-server-next/pull/2](https://github.com/torstenkn/django-mcp-server-next/pull/2) | `review/upstream-66` |
| #68 | [https://github.com/torstenkn/django-mcp-server-next/pull/3](https://github.com/torstenkn/django-mcp-server-next/pull/3) | `review/upstream-68` |
| #67 | [https://github.com/torstenkn/django-mcp-server-next/pull/4](https://github.com/torstenkn/django-mcp-server-next/pull/4) | `review/upstream-67` |
| #60 | [https://github.com/torstenkn/django-mcp-server-next/pull/5](https://github.com/torstenkn/django-mcp-server-next/pull/5) | `review/upstream-60` |
| #63 | [https://github.com/torstenkn/django-mcp-server-next/pull/6](https://github.com/torstenkn/django-mcp-server-next/pull/6) | `review/upstream-63` |
| #69 | [https://github.com/torstenkn/django-mcp-server-next/pull/7](https://github.com/torstenkn/django-mcp-server-next/pull/7) | `review/upstream-69` |

Final local validation: Python 3.12, Django 5.2.19 / MCP 2.3.0: 9 passed; Django 4.2.30 / MCP 2.0.0: 9 passed. Adapted #67: 11 passed with MCP 2.3.0. Wheel/sdist build and twine check passed, both contain original MIT license and provenance notice. No package uploaded.
