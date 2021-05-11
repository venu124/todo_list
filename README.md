# Application - 👩‍💻 External API's

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/venu124/todo_list)
![coverage](https://img.shields.io/badge/coverage-95%25-green)

<description>

## Requirements

This program requires the following Python packages

- [typer](https://typer.tiangolo.com/)
- [requests](https://pypi.org/project/requests/)

They can be installed manually or using a pipenv with the supplied `Pipfile` by running the following

```bash
cd todo_list
pipenv install requests
pipenv install typer
```

## Usage

To use the program with pipenv simply enter a pipenv shell by running `pipenv shell` or prefix `pipenv run` before any Python command

### Program options

<description>

## Pros, cons and next steps

### Pros

- Perform CRUD operations on todo list

### Cons

- Mock unit tests hit the actual External API instead of mocking the API responses

### Next steps

- Improve documentation on explaining how the program works
- Mock External API responses inside unit tests

## License

This project is licensed under the terms of the MIT license.
