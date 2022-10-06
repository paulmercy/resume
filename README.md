
# Personal Portfolio Django
To run locally, do the usual:

 1. Create a Python 3.8+ virtualenv and activate it

 2. Install dependencies: `python3 -m pip install -r requirements.txt`

 3. Rename resume>dotenv file to resume>.env

 4. key in the necessary Postgres db credentials
 
 3. Run server:
    `python3 manage.py migrate`
    
    `python3 manage.py runserver`

 
 ### Running Locally with Docker
 1. Build the images:
    `sudo docker-compose up --build`
 2. Spin up the containers:
    `sudo docker-compose up`
 3. Enter the container:
    `sudo docker-compose exec backend sh`
    `python manage.py migrate`
