import time

import requests
from requests.exceptions import RequestException


class APIClient:
    def __init__(self, url, params, retries=3, timeout=5):
        self.url = url
        self.params = params
        self.retries = retries
        self.timeout = timeout

    def request(self):
        for attempt in range(self.retries + 1):
            try:
                response = requests.get(self.url, params=self.params, timeout=self.timeout)
                response.raise_for_status()
                return response.json()
            except RequestException as e:
                if attempt >= self.retries:
                    print(f'Try {attempt}/{self.retries} failed: {e}')
                    raise e
                time.sleep(attempt / self.retries)
