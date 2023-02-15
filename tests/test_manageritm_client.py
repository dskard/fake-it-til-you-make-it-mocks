import pytest
import uuid

from manageritm.client import ManagerITMClient


class TestClient:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.base_uri = "https://localhost:5000"

    def test_get_client_default_ports(self, requests_mock):
        expected_status = 200
        expected_data = {'client_id': str(uuid.uuid4())}
        requests_mock.get(f"{self.base_uri}/client", status_code=expected_status, json=expected_data)
        requests_mock.get(f"{self.base_uri}/{expected_data['client_id']}/proxy/status", status_code=200, json={'status': None})

        client = ManagerITMClient(self.base_uri)
        actual_data = client.client()

        assert actual_data == expected_data
        assert client._uri == self.base_uri
        assert client._client_id == expected_data['client_id']

    def test_get_client_set_all_ports(self, requests_mock):
        expected_status = 200
        expected_data = {
            'client_id': str(uuid.uuid4()),
            'port': 5200,
            'webport': 5201,
        }
        requests_mock.get(f"{self.base_uri}/client?port=5200&webport=5201", status_code=expected_status, json=expected_data)
        requests_mock.get(f"{self.base_uri}/{expected_data['client_id']}/proxy/status", status_code=200, json={'status': None})

        client = ManagerITMClient(self.base_uri)
        actual_data = client.client(port=5200, webport=5201)

        assert actual_data == expected_data
        assert client._uri == self.base_uri
        assert client._client_id == expected_data['client_id']
