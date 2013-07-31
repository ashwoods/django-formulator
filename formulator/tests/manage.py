#!/usr/bin/env python
"""This is here just to help with integration tests"""

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "formulator.tests.test_settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
