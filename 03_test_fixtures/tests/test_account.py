"""
Test Cases TestAccountModel
"""
import json
from unittest import TestCase
from models import db
from models.account import Account
import random
import numpy as np
from typing import Dict

ACCOUNT_DATA = {}


class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):
        """Connect and load data needed by tests"""
        global ACCOUNT_DATA
        db.create_all()
        with open("tests/fixtures/account_data.json") as json_data:
            ACCOUNT_DATA = json.load(json_data)

    @classmethod
    def tearDownClass(cls):
        """Disconnect from database"""
        db.session.close()  # type: ignore

    def setUp(self):
        """Truncate the tables"""
        db.session.query(Account).delete()

    def tearDown(self):
        """Remove the session"""
        db.session.remove()

    def account_creation(self):
        # select random account
        rand_id = random.choice(np.arange(0, len(ACCOUNT_DATA)))
        data = ACCOUNT_DATA[rand_id]

        # create account
        account = Account(**data)
        account.create()

        return account, data

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_account(self):
        """Test creating an account"""
        rand_id = random.choice(np.arange(0, len(ACCOUNT_DATA)))
        data = ACCOUNT_DATA[rand_id]

        # create account
        account = Account(**data)
        account.create()

        self.assertEqual(len(Account.all()), 1)

    def test_create_all_accounts(self):
        """Create all test user accounts"""

        for data in ACCOUNT_DATA:
            account = Account(**data)
            account.create()

        # check the account creation status
        self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))

    def test_account_update(self):
        # select random account
        account, data = self.account_creation()

        # check account phone number
        db_objs: Account = Account.all()[0]
        self.assertEqual(db_objs.phone_number, data["phone_number"])

        # update phone number and check
        account.phone_number = None
        account.update()
        self.assertIsNone(Account.all()[0].phone_number)

    def test_to_dict(self):
        # select random account
        account, _ = self.account_creation()

        self.assertIsInstance(account.to_dict(), Dict)

        # verify same
        ref_keyset = set(ACCOUNT_DATA[0].keys())
        db_obj_keys = set(Account.all()[0].to_dict().keys())
        self.assertEqual(len(ref_keyset.intersection(db_obj_keys)), 4)

    def test_delete(self):
        # create sample account from test data
        account, _ = self.account_creation()

        self.assertEqual(len(Account.all()), 1)

        # delete the account
        account.delete()

        # recheck the accounts count it should be zero
        self.assertEqual(len(Account.all()), 0)
