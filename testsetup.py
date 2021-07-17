import unittest
import board_trello
import time

import card_trello


class MyTestCase(unittest.TestCase):
    def test_create_board(self):
        try:
            board_id = board_trello.create_board('board_' + str(time.time()))
            self.assertIsNotNone(board_id)
            board_trello.delete_board(board_id)

        except Exception as exp:
            print(exp)
            self.assertTrue(False)

    def test_create_card(self):
        try:
            num = 3  # create 3 cards
            board_id = board_trello.create_board('board_' + str(time.time()))
            list_id = board_trello.create_list_on_board(board_id)
            for i in range(num + 1):
                card_id = card_trello.create_card(list_id)
                self.assertIsNotNone(card_id)
            board_trello.delete_board(board_id)

        except Exception as exp:
            print(exp)
            self.assertTrue(False)

    def test_edit_card(self):
        try:
            board_id = board_trello.create_board('board_' + str(time.time()))
            list_id = board_trello.create_list_on_board(board_id)
            card_id = card_trello.create_card(list_id)
            card_trello.edit_card(card_id)
            board_trello.delete_board(board_id)
            self.assertIsNotNone(card_id)
        except Exception as exp:
            print(exp)
            self.assertTrue(False)

    def test_delete_card(self):
        try:
            board_id = board_trello.create_board('board_' + str(time.time()))
            list_id = board_trello.create_list_on_board(board_id)
            card_id = card_trello.create_card(list_id)
            card_trello.delete_card(card_id)
            board_trello.delete_board(board_id)
            self.assertIsNotNone(card_id)
        except Exception as exp:
            print(exp)
            self.assertTrue(False)

    def test_add_comment(self):
        try:
            board_id = board_trello.create_board('board_' + str(time.time()))
            list_id = board_trello.create_list_on_board(board_id)
            card_id = card_trello.create_card(list_id)
            card_trello.add_comment(card_id)
            board_trello.delete_board(board_id)
            self.assertIsNotNone(card_id)
        except Exception as exp:
            print(exp)
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
