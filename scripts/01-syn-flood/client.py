import time
import requests

import config

while True:
    r = requests.get(f"http://{config.SERVER_IP}:{config.SERVER_PORT}")
    print(r.status_code)
    time.sleep(config.SLEEP_BETWEEN_REQUESTS)