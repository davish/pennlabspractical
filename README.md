# Davis Haupt - Penn Labs Practical

Live demo at [https://davishaupt-pennlabspractical.herokuapp.com](https://davishaupt-pennlabspractical.herokuapp.com). 
You can use the provided form to add new elements and view the contents of the database, 
or query the API directly with an API browser like [Postman](https://www.getpostman.com/) to access all the endpoints.

## Stack:
- Language: Python
- Web Framework: [Flask](http://flask.pocoo.org/)
- ORM: [SQLAlchemy](https://www.sqlalchemy.org/)
- Database: [PostgreSQL](https://www.postgresql.org/)
- Hosting Service: [Heroku](https://www.heroku.com/home)


Along with all the API endpoints in the specification, 
there are some addional endpoints which help with the usability of the API:

- `GET` `/list/:listId/cards`
    - Given a `listId`, return all of the cards associated with the list.
- `GET` `/list/all/cards`
    - Return all lists with their associated cards.
    
- `GET` `/lists`
    - Return all lists (without their associated cards).
