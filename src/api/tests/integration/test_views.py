import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


class TestHealthAPIView:

    url = reverse("api-health")

    def test_api_health(self, api_client) -> None:
        response = api_client.get(self.url)
        assert response.status_code == 200
