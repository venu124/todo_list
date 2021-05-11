# Use this file to add in functions for your cli if you use one!

from typing import Optional

import typer

from src.api import api

app = typer.Typer()


@app.command()
def add_task(name: str = typer.Option(...), comment: str = typer.Option(...)) -> object:
    """Adds a task to your todo list"""
    print("Adding your task...")
    response = api.create_task(name, comment)
    print(response)
    return response


@app.command()
def list_all(
    id: Optional[str] = typer.Option(""),
    name: Optional[str] = typer.Option(""),
    completed: Optional[bool] = typer.Option(False),
    comment: Optional[str] = typer.Option(""),
    limit: Optional[str] = typer.Option(""),
) -> object:
    """Lists all or some of your tasks based on your selected option"""
    print("Listing your task(s) " + str(id))
    response = api.get_tasks(id, name, completed, comment, limit)
    print(response)
    return response


@app.command()
def update_task(
    id: str = typer.Option(...),
    name: str = typer.Option(...),
    completed: Optional[bool] = typer.Option(False),
    comment: str = typer.Option(...),
) -> object:
    """Updates selected task in your todo list"""
    print("Updating your task...")
    response = api.update_task(id, name, completed, comment)
    print(response)
    return response


@app.command()
def delete_task(id: str = typer.Option(...)) -> object:
    """Deletes selected task from your todo list"""
    print("Deleting your task...")
    response = api.delete_task(id)
    print(response)
    return response


@app.command()
def mark_as_done(id: str = typer.Option(...)) -> object:
    """Marks a particular task as completed"""
    print("Marking your task as done...")
    response = api.mark_task_as_done(id)
    print(response)
    return response
