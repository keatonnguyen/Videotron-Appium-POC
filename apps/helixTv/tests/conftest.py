import pytest


# INHERITS FROM ROOT CONFTEST.PY
# DEFINE APP NAME FOR TESTS IN THIS APP
@pytest.fixture
def app_name():
    return "helixTv"
