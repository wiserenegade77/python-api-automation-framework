import requests

class APIClient:
    def __init__(self,base_url,session,timeout=10):
        self.base_url = base_url
        self.timeout = timeout
        self.session = session

    def get(self,endpoint):
        url = f"{self.base_url}/{endpoint.lstrip("/")}"

        response = self.session.get(url,
        timeout=self.timeout)

        return response

    def close(self):
        self.session.close()