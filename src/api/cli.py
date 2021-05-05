# Use this file to add in functions for your cli if you use one!

import json

def format_json(response_body: object) -> object:
    """Represents responses from API in a pretty json format"""
    response_json_object = json.loads(response_body)
    json_formatted_response = json.dumps(response_json_object, indent=2)
    return json_formatted_response