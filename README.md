composetest
-----------

A simple setup to validate:

* python setup (including editor and poetry)
* docker and docker compose installation
* basic docker networking (between containers and from containers to the internet)

howto
------

1. `poetry install`
2. Feel free to mess around with `composetest/server.py`
3. `docker-compose -f docker-compose-test.yaml up --abort-on-container-exit'`

The logs should wrap up nicely and include 2 HTTP responses from simpleclient 1:
* One labeled "server.py says" saying "Hello, world!"
* One labeled "httpbin says" followed by 32 random bytes gathered from https://httpbin.org
