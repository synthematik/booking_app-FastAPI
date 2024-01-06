import pytest


@pytest.mark.asyncio
async def test_abc(prepare_database):
    assert 1 == 1
