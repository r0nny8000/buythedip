Crypto Trading Tool 
===================

Some Python code to play around with the crypto trading platfrom API.


Getting started
---------------
Checkout this project and use [Poetry](https://python-poetry.org).

Install dependencies

    poetry install

Execute

    poetry shell
    cry/cry.py

or

    poetry run python cry/cry.py

Install a new module 

    poetry add <module>
    poetry add -D pylint

Build and Install locally

    poetry build
    pip install dist/workstream-0.1.0.tar.gz

Config VSCodium
---------------

In this folder run 
    
    poetry shell
    which python

or

    poetry env info

to get the full path to the Pipenv's virtualenv. This is something like 

    /Users/me/Library/Caches/pypoetry/virtualenvs/marketdata-cli-MiIDVtXc-py3.7

Press Cmd+Shift+P and search for "Select Interpreter". Press enter, and select any of the suggested interpreters and a .vscode directory will be created inside your project root. It contains a settings.json. Edit this file and set python.pythonPath to the virtualenv path and add /bin/python at the end.

    {
        "python.defaultInterpreterPath": "/Users/me/Library/Caches/pypoetry/virtualenvs/marketdata-cli-MiIDVtXc-py3.7/bin/python"
    }


Troubleshooting
---------------

If import is not working you may have configured an interpreter before. Delete the config with Cmd+Shift+P and execute "Python: Clear Workspace Interpreter Settings". Now the import should work.

Check if LANG and LC_ALL envirnonment variable is set:

    locale
    LANG="de_DE.UTF-8"
    LC_ALL="de_DE.UTF-8"