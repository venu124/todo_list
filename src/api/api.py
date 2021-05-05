# Use this file to add in functions for your programs functionality

"""
Installed typer and requests
--pip install requests
--pip install typer
"""
import typer, requests, json
from typing import Optional

base_url = "https://60823c20827b350017cfbf0b.mockapi.io"
base_path = "/api/v2"

app = typer.Typer()


def format_json(response_body: object) -> object:
    """Represents responses from API in a pretty json format"""
    response_json_object = json.loads(response_body)
    json_formatted_response = json.dumps(response_json_object, indent=2)
    return json_formatted_response


@app.command()
def add_task(name: str = typer.Option(...), comment: str = typer.Option(...)) -> json:
    """Adds a task to your todo list"""
    print("Adding your task...")
    response = requests.post(
        base_url + base_path + "/todo", json={"name": name, "comment": comment}
    )
    print(format_json(response.text))


@app.command()
def list_all(
    id: Optional[str] = typer.Option(""),
    name: Optional[str] = typer.Option(""),
    completed: Optional[bool] = typer.Option(False),
    comment: Optional[str] = typer.Option(""),
    limit: Optional[str] = typer.Option(""),
) -> json:
    """Lists all or some of your tasks based on your selected option"""
    print("Listing all your tasks...")
    response = requests.get(base_url + base_path + "/todo/" + id)
    print(format_json(response.text))


@app.command()
def update_task(
    id: str = typer.Option(...),
    name: str = typer.Option(...),
    completed: Optional[bool] = typer.Option(False),
    comment: str = typer.Option(...),
) -> json:
    """Updates selected task in your todo list"""
    print("Updating your task...")
    response = requests.put(
        base_url + base_path + "/todo/" + id,
        json={"name": name, "name": name, "completed": completed, "comment": comment},
    )
    print(format_json(response.text))


@app.command()
def delete_task(id: str = typer.Option(...)) -> json:
    """Deletes selected task from your todo list"""
    print("Updating your task...")
    response = requests.delete(base_url + base_path + "/todo/" + id)
    print(format_json(response.text))


@app.command()
def mark_as_done(id: str = typer.Option(...)) -> json:
    """Marks a particular task as completed"""
    print("Marking your task as done...")
    response = requests.put(
        base_url + base_path + "/todo/" + id, json={"completed": True}
    )
    print(format_json(response.text))


if __name__ == "__main__":
    app()
