import pytest
from .. import server
from multiprocessing import Process
import requests as req


@pytest.fixture(scope='session', autouse=True)
def server_setup():
    instance = server.create_server()

    process = Process(target=instance.serve_forever)
    process.daemon = True

    process.start()


@pytest.fixture(scope='function')
def api_call():
    return req.get('http://127.0.0.1:5000')
