How to Setup the project.
1. Clone the project form github -> **git clone git@github.com:krishna31/eterlast.git**
2. Create virtual environment -> **virtualenv -p python3.9 .venv**
3. Activate the environment -> **source .venv/bin/activate**
4. install the project dependency -> **pip install -r requirements.txt**
5. Migrate the database schema -> **python manage.py makemigrations**
6. Create Superuser -> **python manage.py createsuperuser**
7. Load the initial data -> **python manage.py loaddata nft/fixtures/initial_data.json  --app nft**
8. Run the project -> **python manage.py runserver**


**Run with docker**
-  Clone the project form github -> **git clone git@github.com:krishna31/eterlast.git**
-  Build the project -> **sudo docker-compose -f docker-compose.local.yml build**
-  Run the project -> **sudo docker-compose -f docker-compose.local.yml up**
-  Login to container -> **sudo docker exec -it eterlast sh**
-  Migrate the database schema -> **python manage.py migrate**
-  Create Superuser -> **python manage.py createsuperuser**
-  Load the initial data -> **python manage.py loaddata nft/fixtures/initial_data.json  --app nft**
