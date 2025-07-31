#!/usr/bin/env python
"""Utility script mirroring Django’s manage.py for this FastAPI project."""

import sys
import os
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent


def run_tests() -> None:
    """Discover and run all unittests in the tests/ folder."""
    # Ensure project root on PYTHONPATH so `app` imports work
    sys.path.insert(0, str(PROJECT_ROOT))

    loader = unittest.TestLoader()
    suite = loader.discover("tests")        # looks inside tests/ recursively
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    # Exit code 0 for success, 1 for any failure
    sys.exit(0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        run_tests()
    else:
        print("Usage:")
        print("  python manage.py test   # run unit-tests")
