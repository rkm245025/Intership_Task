# Intership_Task

how to run in your local machine.

git clone <repository_url>
cd <repository_name>

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver


You can now access the API using the base URL http://localhost:8000. 




