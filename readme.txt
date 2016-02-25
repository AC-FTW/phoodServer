pip install virtualenv
cd project_folder
virtualenv .
cp phoodServer .
pip install django
pip install requests
pip install MetaMindApi --upgrade
source environment.sh
python manage.py runserver
