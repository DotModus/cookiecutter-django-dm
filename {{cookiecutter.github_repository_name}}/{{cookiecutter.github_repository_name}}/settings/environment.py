"""
Execution environment related settings.

The environment variable reader (env)  is instantiated in this module and then
imported into the other settings definition files.
"""
from pathlib import Path

import environ


env = environ.Env(DEBUG=(bool, False))

CURRENT_PATH = Path(__file__).parent
SITE_ROOT = CURRENT_PATH.parent.parent
env_file = SITE_ROOT / '.env'

if env_file.exists():
    environ.Env.read_env(env_file=env_file)
else:
    print('No env file found')
