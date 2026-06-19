import subprocess
from pathlib import Path
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings


class Command(BaseCommand):
    help = 'Run Django development server and Vite dev server together.'

    def add_arguments(self, parser):
        parser.add_argument('addrport', nargs='?', help='Optional port')

    def handle(self, *args, **options):
        base_dir = Path(settings.BASE_DIR)
        vite_dir = base_dir / 'front-end'

        self.stdout.write(self.style.NOTICE('Starting Vite dev server...'))
        vite_proc = subprocess.Popen(['npm', 'run', 'dev'], cwd=str(vite_dir))

        try:
            addrport = options.get('addrport') or ''
            call_command('runserver', addrport)
        finally:
            self.stdout.write(self.style.NOTICE('Stopping Vite dev server...'))
            vite_proc.terminate()
            try:
                vite_proc.wait(timeout=5)
            except Exception:
                vite_proc.kill()
