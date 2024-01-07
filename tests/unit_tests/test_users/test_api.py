import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("email, password, status_code", [
    ("sfedu@mail.ru", "sfedu", 200),
    ("sfedu@mail.ru", "sfeduu", 409),
    ("pass1@mail.ru", "pass1", 200),
    ("pass1", "pass1", 422)
])
async def test_register_user(ac: AsyncClient, email: str, password: str, status_code: int):
    response = await ac.post("/auth/register/", json={
        "email": email,
        "password": password,
    })
    assert response.status_code == status_code


@pytest.mark.parametrize("email, password, status_code", [
    ("test@test.com", "test", 200),
    ("test@test.com", "qwerty", 401)
])
async def test_login_user(ac: AsyncClient, email: str, password: str, status_code: int):
    response = await ac.post("/auth/login/", json={
        "email": email,
        "password": password
    })
    assert response.status_code == status_code
