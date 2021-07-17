import yaml


def read_yml():
    with open('variables.yaml', 'r') as variables:
        return yaml.safe_load(variables)


def get_api_key():
    return read_yml()['key']


def get_auth_secret():
    return read_yml()['secret']


def get_token():
    return read_yml()['token']
