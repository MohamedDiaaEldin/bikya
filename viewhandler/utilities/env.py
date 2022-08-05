

import os
from dotenv import load_dotenv

def get_env(key):        
    load_dotenv()
    env_variable = os.getenv(key)
    return env_variable
