#GitHub: elpapitaslays

import psutil
from core.config import ROCKET_LEAGUE_PROCESS_NAME

def is_rocket_league_running():
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] == ROCKET_LEAGUE_PROCESS_NAME:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False