#!/usr/bin/env python3
"""Compatibility entry point for the working Ratchet v0.4 engine.

The former v0.3 file validated prewritten admission receipts but did not
generate or adjudicate candidates. The current process lives in
`ratchet_engine.py`; this name remains so existing commands fail forward into
the working DIG -> GATE -> RECEIPT loop.
"""

from ratchet_engine import (  # noqa: F401
    SCHEMA_VERSION,
    main,
    run_packet,
    run_self_test,
    validate_run,
)


if __name__ == "__main__":
    raise SystemExit(main())
