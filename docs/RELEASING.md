# Release preparation (no publication performed)

Distribution: `django-mcp-server-next`; development version: `0.6.0a1`.
Python import and Django app label remain `mcp_server` for compatibility.
Do not install the original distribution alongside the successor: they share this package.
Original authors remain in package metadata; Torsten Kneuss is the maintainer.

Before a release:
1. Resolve P0 field-access security findings (#72 and #66) with regression tests across all pipeline stages.
2. Complete MCP 2.x protocol/HTTP/STDIO validation and minimum-version CI.
3. Review dependency advisories, supported Python/Django versions, and release notes.
4. Check PyPI name availability and account ownership; this migration does not reserve the name.
5. Build locally: `python -m build`; validate: `python -m twine check dist/*`.
6. Inspect wheel/sdist for LICENCE.md, NOTICE.md and correct project URLs.
7. Obtain explicit release authorization. No upload workflow or PyPI credentials are configured.

Upstream tags are historical artifacts, not successor releases.
