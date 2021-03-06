from os.path import dirname, abspath, join

PROJECT_ROOT = dirname(dirname(abspath(__file__)))
LOGS_DIR = join(PROJECT_ROOT, "logs")
LOGS_STDOUT_FILE = join(LOGS_DIR, "stdout.log")
