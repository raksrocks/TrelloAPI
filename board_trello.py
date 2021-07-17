# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import config_trello
import json


def create_board(board_name):
    print('**** creating board ' + board_name)
    url = "https://api.trello.com/1/boards/"

    query = {
        'key': config_trello.get_api_key(),
        'token': config_trello.get_token(),
        'name': board_name,
        'idOrganization': '60f1a7f468032e09d03531d2'
    }

    response = requests.post(
        url,
        '',
        params=query
    )

    print('**** response: '+response.text)
    return json.loads(response.text)['id']


def create_list_on_board(board_id):
    print('**** Creating a list on board')
    url = "https://api.trello.com/1/boards/"+board_id+"/lists"

    query = {
        'key': config_trello.get_api_key(),
        'token': config_trello.get_token(),
        'name': 'id_list'
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )

    print('**** result '+response.text)
    return json.loads(response.text)['id']


def delete_board(board_id):
    print('**** deleting the board '+board_id)
    url = "https://api.trello.com/1/boards/"+str(board_id)

    query = {
        'key': config_trello.get_api_key(),
        'token': config_trello.get_token()
    }

    response = requests.request(
        "DELETE",
        url,
        params=query
    )

    print(response.text)

