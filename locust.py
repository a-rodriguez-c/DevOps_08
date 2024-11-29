import logging
from locust import HttpUser, task, between
import gevent
from faker import Faker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
fake = Faker()


class AWSDeploymentPolicyTest(HttpUser):
    wait_time = between(1, 3)
    email = ""

    def on_start(self):
        self.token = self.get_valid_token()
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

    @task
    def request_endpoints(self):
        gevent.joinall([
            gevent.spawn(self.create_email),
            gevent.spawn(self.get_email),
            gevent.spawn(self.get_ping),
        ])

        gevent.sleep(10)

    def create_email(self):
        self.email = fake.email()
        url = f"{self.host}blacklists"
        payload = {
            "email": self.email,
            "app_uuid": fake.uuid4(),
            "blocked_reason": "Suspicious activity"
        }
        logger.info(f"Realizando POST request a: {url}")
        response = self.client.post(url, headers=self.headers, json=payload)

        # Imprimir el status code y el contenido de la respuesta
        logger.info(f"Status code: {response.status_code}")
        logger.info(f"Response content: {response.text}")

    def get_email(self):
        url = f"{self.host}blacklists/{self.email}"
        logger.info(f"Realizando GET request a: {url}")
        response = self.client.get(url, headers={'Authorization': self.headers['Authorization']})

        # Imprimir el status code y el contenido de la respuesta
        logger.info(f"Status code: {response.status_code}")
        logger.info(f"Response content: {response.text}")

    def get_ping(self):
        url = f"{self.host}blacklists/ping"
        logger.info(f"Realizando GET request a: {url}")
        response = self.client.get(url)

        # Imprimir el status code y el contenido de la respuesta
        logger.info(f"Status code: {response.status_code}")
        logger.info(f"Response content: {response.text}")

    def get_valid_token(self):
        return "token-super-secreto"


if __name__ == "__main__":
    from locust.env import Environment
    my_env = Environment(user_classes=[AWSDeploymentPolicyTest])
    AWSDeploymentPolicyTest(my_env).run()
