# Use this file as your main entrypoint for your program

from src.api import cli


def init():
    """Invokes selected CLI command with user input values"""
    cli.app()


# This is the main entrypoint for this program"""
if __name__ == "__main__":
    init()
