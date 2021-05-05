# Use this file to add in your tests!

from typer.testing import CliRunner

from src.api import cli

ERROR_DESCRIPTION = "Oops! Failed to perform the selected command. Please check your input details and try again."

runner = CliRunner()


# Temporarily test cases hit the actual External API instead of mocking the API responses. Need to delete this test
# case once mock responses are setup
def delete_existing_valid_task():
    result = runner.invoke(cli.app, ["delete-task", "--id", "6"])


# Following tests are fot add-task command
def test_add_task():
    result = runner.invoke(cli.app, ["add-task", "--name", "TEST Name", "--comment", "Test comment"])
    assert "Created your task successfully" in result.stdout


# Following tests are for list-all command
def test_list_all_without_options():
    result = runner.invoke(cli.app, ["list-all"])
    assert "Here is your task(s) list" in result.stdout


def test_list_all_with_options():
    result = runner.invoke(
        cli.app,
        ["list-all", "--id", "1", "--name", "Test name", "--completed", "--comment", "Test comment", "--limit", "5",],
    )
    assert "Here is your task(s) list" in result.stdout


def test_list_all_with_invalid_option_value():
    result = runner.invoke(cli.app, ["list-all", "--id", "my_test_id"])
    assert "Here is your task(s) list" not in result.stdout
    assert ERROR_DESCRIPTION in result.stdout


# Following tests are for update-task command
def test_update_task():
    result = runner.invoke(
        cli.app,
        ["update-task", "--id", "6", "--name", "TEST Name", "--completed", "--comment", "Updated Test comment",],
    )
    assert "Updated your task successfully" in result.stdout


def test_update_task_with_invalid_id():
    result = runner.invoke(
        cli.app,
        [
            "update-task",
            "--id",
            "my_test_id",
            "--name",
            "TEST Name",
            "--completed",
            "--comment",
            "Updated Test comment",
        ],
    )
    assert "Updated your task successfully" not in result.stdout
    assert ERROR_DESCRIPTION in result.stdout


# Following tests are for mark-as-done command
def test_mark_task_as_done():
    result = runner.invoke(cli.app, ["mark-as-done", "--id", "6"])
    assert "Marked your task as completed" in result.stdout


def test_mark_task_as_done_with_invalid_id():
    result = runner.invoke(cli.app, ["mark-as-done", "--id", "my_test_id"])
    assert "Marked your task as completed" not in result.stdout
    assert ERROR_DESCRIPTION in result.stdout


# Below are general test cases for all commands
def test_commands_with_invalid_options():
    result = runner.invoke(cli.app, ["list-all", "--random", "1"])
    assert "Here is your task(s) list" not in result.stdout
    assert "Error: no such option" in result.stdout


def test_commands_with_missing_options():
    result = runner.invoke(cli.app, ["update-task", "--id", "6", "--name", "TEST Name", "--completed"])
    assert "Updated your task successfully" not in result.stdout
    assert "Error: Missing option '--comment'" in result.stdout


# Following tests are for delete-task command
def test_delete_task():
    result = runner.invoke(cli.app, ["delete-task", "--id", "6"])
    assert "Deleted your task successfully" in result.stdout


def test_delete_task_with_invalid_id():
    result = runner.invoke(cli.app, ["delete-task", "--id", "my_test_id"])
    assert "Deleted your task successfully" not in result.stdout
    assert ERROR_DESCRIPTION in result.stdout
