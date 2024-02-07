"""
Test Cases for Mocking Lab
"""

import json
from unittest import TestCase
from unittest.mock import patch, Mock
from requests import Response
from models import IMDb

IMDB_DATA = {}


class TestIMDbDatabase(TestCase):
    """Tests Cases for IMDb Database"""

    @classmethod
    def setUpClass(cls):
        """Load imdb responses needed by tests"""
        global IMDB_DATA
        with open("tests/fixtures/imdb_responses.json") as json_data:
            IMDB_DATA = json.load(json_data)

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################
    @patch(target="test_imdb.IMDb.search_titles")
    def test_serach_by_title(self, imdb_mock):
        """Test search by title"""
        # set return value of the mock object
        imdb_mock.return_value = IMDB_DATA["GOOD_SEARCH"]
        imdb = IMDb(apikey="k_12345678")
        # search movie
        results = imdb.search_titles(title="Bambi")
        self.assertIsNotNone(results)
        self.assertIsNone(results["errorMessage"])
        self.assertIsNotNone(results["results"])
        self.assertEqual(results["results"][0]["id"], "tt1375666")

    @patch(target="models.imdb.requests.get")
    def test_search_with_no_results(self, imdb_mock):
        """Test search with title not inside the imdb"""
        # define the mock retrun value
        imdb_mock.return_value = Mock(status_code=404)
        imdb = IMDb(apikey="k_12345678")
        # search movie
        results = imdb.search_titles(title="Bambi")
        self.assertEqual(results, {})

    @patch(target="models.imdb.requests.get")
    def test_search_by_title_failed(self, imdb_mock):
        """Test searching by title failed"""
        imdb_mock.return_value = Mock(
            spec=Response,
            status_code=200,
            json=Mock(return_value=IMDB_DATA["INVALID_API"]),
        )
        imdb = IMDb("bad-key")
        results = imdb.search_titles("Bambi")
        self.assertIsNotNone(results)
        self.assertEqual(results["errorMessage"], "Invalid API Key")

    @patch(target="models.imdb.requests.get")
    def test_review_search_by_id(self, imdb_mock):
        """Test review search by movie id"""
        imdb_mock.return_value = Mock(
            spec=Response,
            status_code=200,
            json=Mock(return_value=IMDB_DATA["GOOD_REVIEW"]),
        )
        imdb = IMDb(apikey="k_12345678")
        results = imdb.movie_reviews(imdb_id="tt1375666")
        self.assertIsNone(results["errorMessage"])
        self.assertEqual(results["title"], "Bambi")

    @patch(target="models.imdb.requests.get")
    def test_review_search_by_id_failed(self, imdb_mock):
        """Test review search by id failed"""
        imdb_mock.return_value = Mock(status_code=404)
        imdb = IMDb(apikey="k_12345678")
        results = imdb.movie_reviews(imdb_id="bad id")
        self.assertEqual(results, {})

    @patch(target="models.imdb.requests.get")
    def test_rating_search_by_id(self, imdb_mock):
        """Test movie Ratings"""
        # define the mock to mimic the request response
        imdb_mock.return_value = Mock(
            spec=Response,
            status_code=200,
            json=Mock(return_value=IMDB_DATA["GOOD_RATING"]),
        )
        imdb = IMDb("k_12345678")
        results = imdb.movie_ratings("tt1375666")
        self.assertIsNotNone(results)
        self.assertEqual(results["title"], "Bambi")
        self.assertEqual(results["filmAffinity"], 3)
        self.assertEqual(results["rottenTomatoes"], 5)

    @patch(target="models.imdb.requests.get")
    def test_rating_search_by_id_failed(self, imdb_mock):
        """Test rating search by id failed"""
        imdb_mock.return_value = Mock(status_code=404)
        imdb = IMDb(apikey="k_12345678")
        results = imdb.movie_ratings(imdb_id="bad id")
        self.assertEqual(results, {})
