import pytest


@pytest.fixture
@pytest.mark.djang_db
def get_token(client, django_user_model):
    username = "tim"
    password = "tim"

    django_user_model.objects.create_user(
        username=username, password=password, role='admin'
    )

    response = client.post("/user/token/", {
        "username": username,
        "password": password,
        "role": "admin"
    })

    return response.data["access"]
