# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import json

import requests
import yaml
import config_trello


def create_card(id_list):
    print('**** creating card with board id ' + id_list)
    url = "https://api.trello.com/1/cards"

    query = {
        'key': config_trello.get_api_key(),
        'token': config_trello.get_token(),
        'idList': id_list
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )

    print(response.text)
    return json.loads(response.text)['id']


def edit_card(card_id):
    print('**** Updating card with id ' + card_id)
    url = "https://api.trello.com/1/cards/" + card_id

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': config_trello.get_api_key(),
        'token': config_trello.get_token(),
        'name' : "name_"+card_id
    }

    response = requests.request(
        "PUT",
        url,
        headers=headers,
        params=query
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


def delete_card(card_id):
    print('**** deleting card with card id ' + card_id)
    url = "https://api.trello.com/1/cards/" + card_id

    response = requests.delete(
        url
    )

    print(response.text)


def add_comment(card_id):
    print('**** adding comment on card with id ' + card_id)
    url = "https://api.trello.com/1/cards/"+card_id+"/actions/comments"

    query = {
        'key': config_trello.get_api_key(),
        'token': config_trello.get_token(),
        'text' : 'Comment updated form API'
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )

    print(response.text)