#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess
import atexit
from pathlib import Path


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # If running the development server, start Vite dev server alongside it.
    vite_proc = None
    if 'runserver' in sys.argv:
        base_dir = Path(__file__).resolve().parent
        vite_dir = base_dir / 'front-end'
        try:
            vite_proc = subprocess.Popen(['npm', 'run', 'dev'], cwd=str(vite_dir))
        except Exception:
            vite_proc = None

        def _stop_vite():
            if vite_proc and vite_proc.poll() is None:
                try:
                    vite_proc.terminate()
                except Exception:
                    pass

        atexit.register(_stop_vite)

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
