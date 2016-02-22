Documentation:
********************************************************************************
Read http://docs.python-guide.org/en/latest/dev/virtualenvs/ for more information.

Setup an environment:
********************************************************************************
1. pip install virtualenv
2. cd project_folder
3. virtualenv .
4. If the current virtual environment does not appear on the left of the prompt, then: source bin/activate
5. cp phoodServer .
6. pip install django
7. pip install requests
8. pip install MetaMindApi --upgrade

Work in the environment for the project::
********************************************************************************
1. cd project_folder
2. source bin/activate

When you are done working with the project:
********************************************************************************
1. deactivate
