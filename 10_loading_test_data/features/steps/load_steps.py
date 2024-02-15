# pylint: disable=function-redefined, missing-function-docstring
# flake8: noqa
"""
Pet Steps
Steps file for Pet.feature
For information on Waiting until elements are present in the HTML see:
    https://selenium-python.readthedocs.io/waits.html
"""
import requests
from behave import given


# Load data here


@given("the following pets")
def step_impl(context):
    """Refresh all the pets in the database"""

    # first send a get request and gather previous pet ids before delete
    get_response = context.driver.get(f"{context.base_url}/pets")
    # check the get status code
    assert get_response.status_code == 200

    # iterate over every pet item and delete from the db
    for i_pet in context.get_response.json():
        pet_id = i_pet["id"]
        # delete pet
        delete_response = context.driver.delete(f"{context.base_url}/pets/{pet_id}")

        # check the delete status
        assert delete_response.status_code == 204

    # complete delete previous records

    for i_data in context.table:
        # data instance is a dict with column names
        payload = {
            "name": i_data["name"],
            "category": i_data["category"],
            "available": i_data["available"] in ["True", "true", 1],
            "gender": i_data["gender"],
            "birthday": i_data["birthday"],
        }

        # send the web post request with payload data
        post_response = context.driver.post(f"{context.base_url}/pets", json=payload)
        # check the creation status code
        assert post_response.status_code == 201
