# `python_base`: a fully featured `uv` base repo for Python development

`python_base` is fully configured to enable a quick start for Python development using [`uv`](https://docs.astral.sh/uv). `python_base` includes a fully-featured example [pyproject.toml](./pyproject.example.toml), a reasonable [dev container configuration](./.devcontainer/devcontainer.json), appropriate [VS Code settings](./.vscode/settings.json), and an opinionated [EditorConfig](./.editorconfig).

## Configuration

To configure this template for your specific project, the template must updated in the following areas:

1. `./LICENSE`
    - Update to an [appropriate license](https://choosealicense.com).
1. `./.devcontainer/devcontainer.json`
    - `name`

After the app (or project / library) is initialized—see [Using `uv`](#using-uv)—the dev container `postCreateCommand` `uv` command can be uncommented to automatically create a virtual environment and sync the development environment from the `pyproject.toml` using the [`devcontainer-uv-setup.bash`](./devcontainer-uv-setup.bash) script upon dev container startup.

## Opinionated defaults

This template makes a few key assumptions for how the user would like to manage their project:

- The [`ruff` linter](https://docs.astral.sh/ruff/) will be used to manage all Python formatting.
    - Docstrings will use the [`google`](https://github.com/NilsJPWerner/autoDocstring/blob/master/docs/google.md) format.
    - Aggressive rulesets have been enabled:
        - [flake8-builtins (A)](https://docs.astral.sh/ruff/rules/#flake8-builtins-a)
        - [flake8-bugbear (B)](https://docs.astral.sh/ruff/rules/#flake8-bugbear-b)
        - [pydocstyle (D)](https://docs.astral.sh/ruff/rules/#pydocstyle-d)
        - [pycodestyle (E)](https://docs.astral.sh/ruff/rules/#error-e)
        - [pyflakes (F)](https://docs.astral.sh/ruff/rules/#pyflakes-f)
        - [pep8-naming (N)](https://docs.astral.sh/ruff/rules/#pep8-naming-n)
        - [isort (I)](https://docs.astral.sh/ruff/rules/#isort-i)
        - [flake8-quotes (Q)](https://docs.astral.sh/ruff/rules/#flake8-quotes-q)
        - [flake8-simplify (SIM)](https://docs.astral.sh/ruff/rules/#flake8-simplify-sim)
        - [pyupgrade (UP)](https://docs.astral.sh/ruff/rules/#pyupgrade-up)
- Strict type checking will be enforced by [`mypy`](https://mypy.readthedocs.io/en/stable/).
- The project will be tested using [`pytest`](https://docs.pytest.org/en/stable/).
- [`shellcheck`](https://marketplace.visualstudio.com/items?itemName=timonwong.shellcheck) and [`shfmt`](https://marketplace.visualstudio.com/items?itemName=foxundermoon.shell-format) will be used for `*sh` files.

## Using `uv`

Full documentation for `uv` is available on the [documentation site](https://docs.astral.sh/uv).

- To create a new app:

```bash
uv init --directory . --name python_base
```

- To create a new project:

```bash
uv init --directory . --package --name python_base
```

- To create a new library:

```bash
uv init --directory . --library --name python_base
```

- To add requirements to the project:

```bash
uv add requests
```

- To remove requirements from the project:

```bash
uv remove requests
```

- To add development requirements to the project:

```bash
uv add --group dev ruff mypy pre-commit
```

- To add test requirements to the project:

```bash
uv add --group dev pytest pytest-cov
```

- To create a virtual environment:

```bash
uv venv
```

- To enter the virtual environment:

```bash
source ./.venv/bin/activate
```

- To install all project requirements:

```bash
uv sync
```

- To install all project requirements, including development and testing requirements:

```bash
uv sync --group dev --group test
```

- To lock all dependencies:

```bash
uv lock
```

- To check the lockfile:

```bash
uv lock --check
```

- To update all dependencies:

```bash
uv lock --upgrade
```

- To update a specific dependency:

```bash
uv lock --upgrade-package requests
```

- To run a Python script:

```bash
uv run example.py
```

- To build the project as a package:

```bash
uv build
```

## License

This template repository is [licensed](./LICENSE) under "[The Unlicense](https://choosealicense.com/licenses/unlicense/)" so as to be as freely useable as possible.
