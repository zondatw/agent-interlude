"""agent-interlude — capture AI coding agent <-> API traffic for prompt-architecture analysis.

This package exposes three entry points (declared in pyproject.toml):

    agent-interlude          → agent_interlude.proxy:main   (bundled launcher: proxy + UI)
    agent-interlude-report   → agent_interlude.report:main  (web UI alone, reads logs)
    agent-interlude-analyze  → agent_interlude.analyze:main (text report)

Each module is also runnable as `python -m agent_interlude.<name>` for diagnostics.
"""

__version__ = "0.2.1"
