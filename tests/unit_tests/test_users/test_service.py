import pytest
from src.users.service import UserService


@pytest.mark.parametrize("id_user, email, exists", [
    (1, "test@test.com", True),
    (2, "artem@example.com", True),
    (3, "...", False)
])
async def test_find__user_by_id(id_user: int, email: str, exists: bool):
    user = await UserService.find_by_id(id_user)

    if exists:
        assert user.email == email
        assert user.id == id_user
    else:
        assert not user


@pytest.mark.parametrize("email, exists", [
    ("test@test.com", True),
    ("artem@example.com", True),
    ("adadadad", False)
])
async def test_find_one_or_none(email: str, exists: bool):
    user = await UserService.find_one_or_none(email=email)

    if exists:
        assert user.email == email
    else:
        assert not user
