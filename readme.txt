pip install virtualenv
cd project_folder
virtualenv .
cp phoodServer .
pip install django
pip install requests
source environment.sh
python manage.py runserver