# SoccerTournament

This project consist of a simple REST service build with python framework FLASK that includes singup and login endpoint to create an user and then login which will return a JWT token.
With help of this token, you will be able to interact with different endpoint that allow you to create Restaurants into the database.

## Models

This application consists of three simple models of data and its attributes:

### Player

- **Photo:** String. Required for signing up.
  > **Note:** This is an URL
- **FirstName:** String.
- **LastName:** String.
- **BirthDate:** Date.
- **Position:** String, it has specific choices.
- **ShirtNumber:** Integer.
- **FirstEleven:** Boolen. Indicates if the player starts the matches with the first eleven.
- **Team:** ForeignKey. Team the player belongs to.

### Team

- **Name:** String. Is Unique
- **flagImage:** String.
  > **Note:** This is an URL
- **teamCrest:** String.
  > **Note:** This is an URL

### TechnicalStaff

- **FirstName:** String.
- **LastName:** String.
- **BirthDate:** Date.
- **nationality:** String.
- **Rol:** String, it has specific choices.
- **Team:** ForeignKey. Team the staff belongs to.

## LocalSetup

Once you clone this repo, you need to do the following to make it work:

### 1. Virtual Environment

We recommend creating a virtual environment to manage your dependencies in a better way. In the root folder(where you find .gitignore and README.md files) of the project execute:

If you don't have virtualenv:

```
pip install virtualenv
```

Create venv:

```
virtualenv venv
```

Activate it:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

### 2. Project settings

For the project settings, first you need to setup a database server. You can guide from this tutorial [Setup Postgres with django](https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8) specially in the "Setting up a database server" section. Most changes are related to the settings.py file for the project.

After setting up your environment and db server, in the SoccerTournament directory(where the manage.py is), execute the following command to populate you database with sample data:

```
python manage.py loaddata SoccerTournamentApp/fixtures/data.json
```

### 3. Execution:

In the SoccerTournament directory(where the manage.py is), in the terminal execute:

```
python manage.py runserver
```

Make sure your localhost and port 8000 are free, otherwise the app will not execute.
Open your browser on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
