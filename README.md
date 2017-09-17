# Davis Haupt - Penn Labs Practical

Live demo at [https://davishaupt-pennlabspractical.herokuapp.com](https://davishaupt-pennlabspractical.herokuapp.com). 
You can use the provided form to add new elements and view the contents of the database, 
or query the API directly with an API browser like [Postman](https://www.getpostman.com/) to access all the endpoints.

## Stack:
- Language: Python
- Web Framework: [Flask](http://flask.pocoo.org/)
    - Flask is a relatively simple framework with not much overhead, 
    so I was able to easily define API routes and their intended behavior without much boilerplate code.
- ORM: [SQLAlchemy](https://www.sqlalchemy.org/)
    - I have a bunch of experience with Django and its ORM, and SQLAlchemy allowed me to stay away from raw SQL requests
    without the overhead/boilerplate that Django would require 
    (again, this also influenced my choice of Flask as a web framework).
- Database: [PostgreSQL](https://www.postgresql.org/)
    - The Postgres extension for Heroku is very straightforward, 
    and using a SQL database allowed me to easily query the database and verify that the app was working properly.
- Hosting Service: [Heroku](https://www.heroku.com/home)
    - Heroku's deployment process is really simple: just push to a remote Git repository, 
    and your app is pushed live to a server.

## API Endpoints
Important note: both requests and responses for the API are in JSON format.

Along with all the API endpoints in the specification, 
there are some addional endpoints which help with the usability of the API:

- `GET` `/list/:listId/cards`
    - URL Parameters
        - `listId`: ID of the list whose cards to display
    - Given a `listId`, return all of the cards associated with the list.
- `GET` `/list/all/cards`
    - Return all lists with their associated cards.
    
- `GET` `/lists`
    - Return all lists (without their associated cards).
    
- `POST` `/editcard/:cardId`
    - URL Parameters
        - `cardId`: ID of the card to update
    - JSON Parameters:
        - `title`
        - `description`
    
## Notable Files
- `app.py`: Contains the API routes and the functions that define their behavior.
- `models.py`: Definitions for the Card and List entities and associated helper functions.
