"""
Test Cases for Counter Web Service
"""

from unittest import TestCase
import status
from counter import app
import status
import json


class CounterTest(TestCase):
    """Test Cases for Counter Web Service"""

    def setUp(self):
        self.client = app.test_client()

    def test_create_counter(self):
        """Test creation of a counter"""
        result = self.client.post("/counters/shoes")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

    def test_duplicate_counter(self):
        """Test duplicate counters creation"""
        result = self.client.post("/counters/bags")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        # try to duplicate the creation
        result = self.client.post("/counters/bags")
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)

    def test_counter_update(self):
        """Test counter update api"""
        # define inventory levels
        inventory = {"sell": 0, "left": 200}

        result = self.client.put("/counters/cream", data=json.dumps(inventory))
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.json["cream"]["left"], 200)

    def test_read_counter(self):
        """Test counter read api"""
        # first create the counter
        self.client.post("/counters/shampoo")

        # update the content
        inventory = {"sell": 20, "left": 180}
        # send put request with inventory data
        self.client.put("/counters/shampoo", data=json.dumps(inventory))
        # get data from the api
        results = self.client.get("/counters/shampoo")
        self.assertEqual(results.status_code, status.HTTP_200_OK)
        self.assertEqual(results.json["shampoo"]["sell"], 20)

    def test_delete_counter(self):
        """Test counter deletion"""
        # first create the counter
        self.client.post("/counters/pens")

        # update the content
        inventory = {"sell": 210, "left": 1810}
        # send put request with inventory data
        self.client.put("/counters/pens", data=json.dumps(inventory))
        # get data from the api
        results = self.client.get("/counters/pens")
        self.assertEqual(results.status_code, status.HTTP_200_OK)
        self.assertEqual(results.json["pens"]["sell"], 210)

        # delete the item
        result = self.client.delete("/counters/pens")
        self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)

        # send a get request and check
        results = self.client.get("/counters/pens")
        self.assertEqual(results.status_code, status.HTTP_404_NOT_FOUND)
