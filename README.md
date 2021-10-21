# Github OAuth Exercise

A simple Django application that allows OAuth login via github 

Prequisites:
- Docker
- GNU Make

## To run
* First, go to https://github.com/settings/applications/new to register an OAuth app with Github
  - Homepage URL should be `http://127.0.0.1:8000/`,
  - Authorization callback URL should be `http://127.0.0.1:8000/accounts/github/login/callback/`
* Copy `src/.env.example` to `src/.env` and update `GITHUB_CLIENTID` and `GITHUB_SECRET` with values obtained above
* `make run` to build and run the docker image
* Go to http://127.0.0.1:8000/ to view the app
* `make test` will run the unit test suite

