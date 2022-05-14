**Normal Setup**
-  Clone the project form github -> **git clone --branch master  https://github.com/krishna31/eterlast.git**
-  Create virtual environment -> **virtualenv -p python3.9 .venv**
-  Activate the environment -> **source .venv/bin/activate**
-  install the project dependency -> **pip install -r requirements.txt**
-  Migrate the database schema -> **python manage.py makemigrations**
-  Create Superuser -> **python manage.py createsuperuser**
-  Load the initial data -> **python manage.py loaddata nft/fixtures/initial_data.json  --app nft**
-  Run the project -> **python manage.py runserver**

**Run with docker**
-  Clone the project form github -> **git clone --branch master  https://github.com/krishna31/eterlast.git**
-  Build the project -> **sudo docker-compose -f docker-compose.local.yml build**
-  Run the project -> **sudo docker-compose -f docker-compose.local.yml up**
-  Login to container -> **sudo docker exec -it eterlast sh**
-  Migrate the database schema -> **python manage.py migrate**
-  Create Superuser -> **python manage.py createsuperuser**
-  Load the initial data -> **python manage.py loaddata nft/fixtures/initial_data.json  --app nft**
