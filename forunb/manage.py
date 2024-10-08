#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from forunb.env import env, BASE_DIR

def main():
    """Run administrative tasks."""
    # Read the environment variables from the .env file
    env.read_env(os.path.join(BASE_DIR, '.env'))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', env('DJANGO_SETTINGS_MODULE'))
    try:
        from django.core.management import execute_from_command_line # pylint: disable=C0415
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
