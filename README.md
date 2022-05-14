How to Setup the project.
1. Clone the project form github
    public repo
2. Create virtual environment
    virtualenv -p python3.9 .venv
3. Activate the environment
    source .venv/bin/activate
4. install the project dependency
    pip install -r requirements.txt
5. Migrate the database schema
    python manage.py makemigrations
6. Load the initial data
    python manage.py loaddata nft/fixtures/initial_data.json  --app nft
7. Run the project
    python manage.py runserver



