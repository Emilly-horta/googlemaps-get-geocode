# Getting geocode from Google Map's API with Python

### Dependencies

Dependency management made with [**Pipenv**](https://pipenv.pypa.io/en/latest/). Make sure it is already installed before get continue.

```shell
$ pip install -U pipenv
```

The dependecies declarated at `Pipfile`.

- flask (1.1.2)
- requests (2.24.0)
- python-dotenv (0.14.0)

The following commands will install all dependencies for this project.

```shell
$ pipenv install
$ pipenv shell
```

### Before executing

Set your **API KEY** from _Google Cloud Console_ as environment variable, or just create a `get_geocode/.env` file that contains it like this:

    API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXX

## Executing 

```shell
# RUNNING JUST THE GET_GEOCODE MODULE
$ pipenv run get_geocode

# RUNNING THE WEBSITE FOR TEST AT FLASK
$ pipenv run website
```