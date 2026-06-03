"""`python -m agent_interlude` shortcut → identical to the `agent-interlude` console script.

We forward to agent_interlude.proxy.main rather than introduce a separate
dispatcher so there's only one entrypoint to maintain. Module-form invocation
stays useful for diagnostics (`python -m agent_interlude --no-ui`) without
having the entry-point shim on PATH.
"""

from agent_interlude.proxy import main

if __name__ == "__main__":
    main()
