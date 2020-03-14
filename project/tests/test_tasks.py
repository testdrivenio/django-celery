from django.urls import reverse


def test_home(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200
