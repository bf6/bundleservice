import json
from datetime import datetime
from locust import HttpLocust, TaskSet, task

class Behavior(TaskSet):

    @task(1)
    def get_bundle(self):
        params = {
            'device_uuid': 'b21ad0676f26439482cc9b1c7e827de4',
            'sensor_type': 'temperature',
            'start_time': 1510093202,
            'end_time': 1510093202,
        }
        self.client.get('/bundles', params=params)

    @task(2)
    def post_bundle(self):
        body = {
            'device_uuid': 'b21ad0676f26439482cc9b1c7e827de4',
            'sensor_type': 'temperature',
            'sensor_value': 50.0,
            'sensor_reading_time': 1510093202,
        }
        headers = {
            'Content-Type': 'application/json'
        }
        self.client.post('/bundles', data=json.dumps(body), headers=headers)

class SimulatedSensor(HttpLocust):
    task_set = Behavior
