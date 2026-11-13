# Migration validation

2026-11-14: original two branch refs, five tag refs (including tag object SHAs) and 28 PR head SHAs match archived source metadata exactly. Git fsck --full passed. Original LICENCE.md is byte-identical to upstream. Default successor branch next descends from original PR #70. Upstream main is preserved unchanged.

Local Python 3.12 tests: Django 5.2.19/MCP 2.3.0: 9 passed; Django 4.2.30/MCP 2.0.0: 9 passed. Adapted icons draft: 11 passed on latest tested SDK. Build and twine check passed. Both artifacts include LICENCE.md and NOTICE.md. The PyPI distribution name is prepared, not reserved or published.

CI is configured for push and pull_request with read-only permissions, minimum/latest SDK and Python/Django matrix. Remote Actions results must be checked independently; local passes do not imply a successful remote matrix. Historical branches/tags intentionally contain original upstream package identity.
