# Contribution Guidelines

Read these guidelines before contributing to the project.

## Setting Up Your Developer Environment

Create a virtual environment using venv/conda/your preferred tool with Python 3.10 (highly recommend conda!).

Install the dependencies.
```bash
pip install -r requirements.txt
```

## Git Workflow

There will be 2 main branches for this project.

1. `main` - The branch for the official release ready software.
1. `dev` - The current development version of the software.

After a feature is assigned to a project member the development workflow will look like this:

1. Pull the latest version of the `dev` branch

```bash
git checkout dev
git pull
```

2. Create a feature branch from the current `dev` branch. Feature branches will always be named `feature-<name>`.

```bash
git checkout -b feature-myname
git push --set-upstream origin feature-myname
```

3. Start coding in the feature branch. Commit all the source code changes to the new feature branch.

Per feature there is only one feature branch which has the `dev` branch as it's origin. However you are free to create any number of subbranches which inherit from the feature branch. You are also free to merge however you want amongst your subbranches and your feature branch.

Always `rebase` your feature branch and subbranch before merging (see [Before Merging](#before-merging)).

Be sure to delete any subbranches after merging into a higher or your feature branch if they are not needed anymore.

> If you work with multiple people on the same feature you might want to create a subbranch from the feature branch for each person and then merge for each completed subtask into the feature branch.

Subbranches will follow the naming scheme `feature-<feature name>-sub-<name>`.

### Before Merging

If the feature is completed it is now time to prepare the merge request into the `dev` branch. Make sure all the changes in the feature branch are pushed to the remote repository. Be carful not to commit any configuration files specific to your editor to the repository unless it was specifically talked about. If they are not ignored in the `.gitignore` file, add them.

After that, **rebase** your feature branch and resolve eventual merge conflicts originating from the `dev` branch.

```bash
git rebase dev
```

**Make sure that all requirements of the [Coding Style](#coding-style), [Documentation](#documentation) and [Testing](#testing) sections are met!**

### Merge Requests

After preparing the feature branch you are ready to create a merge request for the `dev` branch.

> See [Merge Requests](https://docs.gitlab.com/ee/user/project/merge_requests/) for further information

Provide an adequate description and if not clear documentation, as well as usage examples for your code. Make sure you select the [Squash commits in a merge request option](https://docs.gitlab.com/ee/user/project/merge_requests/squash_and_merge.html#set-default-squash-options-for-a-merge-request), so that only one commit will be created when merging. `Assign approvers` for the merge request and wait for feedback.
Resolve corrections requested by the approver.
If all looks good the approver will merge into the `dev` branch. The feature branch and subbranches are then deleted.

### Creating A Merge Request

1. Add a suitable title. The title should follow the [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) guidelines. Example: `feat: ✨ Add audio playback`.

2. Add an adequate description. It should follow this format:

```md
## Changes
- a change
- another change

Link to Jira: [OFA-num TaskName](#)
```

3. Assign your expert engineer as a reviewer.

4. Ensure that the `Delete source branch` and `Squash commits` options are selected.

## Coding Style

We will abide by the [PEP 8 Style Guide](https://peps.python.org/pep-0008/).

### Type hinting/definitions

Make sure that all variables and functions signatures include type hinting/definitions. Check out [Type hinting in python](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) for more information.

### Module export symbols

In python there is a concept which lets you define which functions and classes can be imported from the module. To define these you add `__all__` to the top of your python file.

> For more information click [here](https://www.geeksforgeeks.org/python-__all__/)

```python
__all__ = ['my_func', 'MyClass']

def my_func() -> None: ...

class MyClass: ...
```

## Documentation

Document all your public facing symbols. In python we can use the docstring syntax for that. This will also show up in your editor's intellisense. It ensures that other people working with your code know what each class and function does and how to use it. If necessary also provide usage examples.
For [docstrings](https://peps.python.org/pep-0257/) we will use the [reST style](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html):

- File
  Write a short description of what is contained in the file.

```python
"""
This file contains this and is used for that.
"""

import ...

...
```

- Functions

```python
def my_func(param1: str, param2: str) -> str: ...
    """
    This is a reST style.

    :param param1: this is a first param
    :param param2: this is a second param
    :returns: this is a description of what is returned
    :raises KeyError: raises an exception
    """
    ...
```

You wont need to include the `:type ...` mentioned in the [sphinx documentation for the reST style](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html) as with the use of type hinting this will be obsolete.

- Classes
  Give a brief description of what the class does and what it is used for. Also provide a docstring for each public function and property.

```python

class MyClass:
    """
    MyClass does this and it used for that...
    """

    def my_public_class_function(self, params1: str, param2: str) -> str:
        """
        This is function is for this and does that.

        :param param1: this is a first param
        :param param2: this is a second param
        :returns: this is a description of what is returned
        :raises KeyError: raises an exception
        """

    @property
    def my_property(self) -> str:
        """
        (This is my_property. It does this and is used for that.
        -> can be omitted if the description is clear from the :returns section)

        :returns: this is the description of what is returned
        """
        ...
    ...

```

## Testing

Make sure all public facing classes and functions are [unit tested](https://en.wikipedia.org/wiki/Unit_testing). For this the [pytest](https://docs.pytest.org/en/7.2.x/) module will be used.

> For further information how to use pytest refer to [this documentation](https://docs.pytest.org/en/7.2.x/)

## Credits

Thanks:

Daniel Stoffel, for providing a baseline template.
