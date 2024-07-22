from dotenv import load_dotenv
import logging, os

from const import env_variables


load_dotenv(override=True)

if not all(key in os.environ for key in env_variables):
    logging.fatal(
        'Missing keys in .env\n'
        'Make sure these are written:\n'
        f'{env_variables}'
    )
    quit()

REDIS_HOST: str = os.environ.get('REDIS_HOST')
REDIS_PORT: str = os.environ.get('REDIS_PORT')
REDIS_DB: str = os.environ.get('REDIS_DB')
REDIS_PASSWORD: str = os.environ.get('REDIS_PASSWORD')
