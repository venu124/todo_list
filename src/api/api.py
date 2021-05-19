# Use this file to add in functions for your programs functionality

import json
from typing import Optional

import requests

BASE_URL = "https://60823c20827b350017cfbf0b.mockapi.io"
BASE_PATH = "/api/v2"

ERROR_DESCRIPTION = "Oops! Failed to perform the selected command. Please check your input details and try again."


def build_error_response(error_message: str) -> str:
    """Returns the error message based on the External API response"""
    return "Error message: " + error_message + "\n " + "Error description: " + ERROR_DESCRIPTION


def create_task(name: str, comment: str) -> str:
    """
    :param name: This parameter accepts a string and contains the task name
    :param comment: This parameter accepts a string and contains the task comment
    :return: Returns a string which contains success or failure response based on the API response status
    """
    response = requests.post(BASE_URL + BASE_PATH + "/todo", json={"name": name, "comment": comment})
    if response.status_code == 201:
        print("Created your task successfully")
        return json.dumps(response.json(), indent=4)
    else:
        return build_error_response(response.text)


def get_tasks(
    id: Optional[str], name: Optional[str], completed: Optional[bool], comment: Optional[str], limit: Optional[str],
) -> str:
    """
    :param id: This optional parameter accepts a string and response is filtered based on this value
    :param name: This optional parameter accepts a string and response is filtered based on this value
    :param completed: This optional parameter accepts a boolean and response is filtered based on this value
    :param comment: This optional parameter accepts a string and response is filtered based on this value
    :param limit: This optional parameter accepts a string and response is filtered based on this value
    :return: Returns a string which contains success or failure response based on the API response status
    """
    response = requests.get(BASE_URL + BASE_PATH + "/todo/" + str(id))
    if response.status_code == 200:
        print("Here is your task(s) list:")
        return json.dumps(response.json(), indent=4)
    else:
        return build_error_response(response.text)


def update_task(id: str, name: str, completed: Optional[bool], comment: str,) -> str:
    """
    :param id: This parameter accepts a string and its value is used to find and update the task
    :param name: This parameter accepts a string and its value is used to update the task name
    :param completed: This parameter accepts a boolean and its value is used to make the task as completed
    :param comment: This parameter accepts a string and its value is used to update the task comment
    :return: Returns a string which contains success or failure response based on the API response status
    """
    response = requests.put(
        BASE_URL + BASE_PATH + "/todo/" + id, json={"name": name, "completed": completed, "comment": comment},
    )
    if response.status_code == 200:
        print("Updated your task successfully")
        return json.dumps(response.json(), indent=4)
    else:
        return build_error_response(response.text)


def delete_task(id: str) -> str:
    """
    :param id: This parameter accepts a string and its value is used to delete the task
    :return: Returns a string which contains success or failure response based on the API response status
    """
    response = requests.delete(BASE_URL + BASE_PATH + "/todo/" + id)
    if response.status_code == 200:
        print("Deleted your task successfully")
        return json.dumps(response.json(), indent=4)
    else:
        return build_error_response(response.text)


def mark_task_as_done(id: str) -> str:
    """
    :param id: This parameter accepts a string and its value is used to mark the task as completed
    :return: Returns a string which contains success or failure response based on the API response status
    """
    response = requests.put(BASE_URL + BASE_PATH + "/todo/" + id, json={"completed": True})
    if response.status_code == 200:
        print("Marked your task as completed")
        return json.dumps(response.json(), indent=4)
    else:
        return build_error_response(response.text)
