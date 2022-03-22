# Console Logs
Developed by [Ali Ali](https://github.com/alibeniaminali), [Thor Refoy](https://github.com/thor-r) & [Peter Bid](https://github.com/PeterBid)

## Overview 
- A full-stack desktop app developed during my last week at General Assembly Software Engineering Course. 
- Console Logs is a social media platform, where people can share and upload video clips of gaming footage related to specific games, and allows other users to comment on them.

## Timeline :
- 7 days

## Project Brief :
- One week to plan, build, and test our final project with a focus on cementing the learning from the past 11 weeks and showing off our new Python skills.
- Build a full-stack application by making your own backend and your own front-end
- Use a Python Django API using Django REST Framework to serve your data from a Postgres database
- Consume your API with a separate front-end built with React
- Be a complete product which most likely means multiple relationships and CRUD functionality for at least a couple of models

## Technologies Used :
### Database:
- [x] PostgresSQL
### Backend:
- [x] Python
- [x] Django
### Frontend:
- [x] JavaScript (ES6)
- [x] React.js
- [x] HTML5
- [x] CSS3 + SASS
- [x] React Bootstrap
### Dependencies:
- [x] djangorestframework
- [x] pyjwt
- [x] python-dotenv
- [x] psycopg2-binary
- [x] Axios
- [x] react-router-dom
- [x] JSONWebToken
### Development Tools:
- [x] VS Code
- [x] Git + GitHub
- [x] Insomnia
- [x] TablePlus
- [x] Heroku
- [x] pylint
- [x] Figma

## Installation instructions :
1. Install back-end dependencies: `pipenv`
2. Enter virtual environment shell: `pipenv shell`
3. Make Migrations: `python manage.py makemigrations`
4. Migrate: `python manage.py migrate`
5. Seed your database following this order:
- `python manage.py loaddata jwt_auth/seeds.json`
- `python manage.py loaddata projects/seeds.json`
- `python manage.py loaddata group_members/seeds.json`
- `python manage.py loaddata tickets/seeds.json`
- `python manage.py loaddata comments/seeds.json`
6. Start back-end server: `python manage.py runserver`
7. Change into front-end directory: `cd client`
8. Install front-end dependencies: `yarn`
9. Start front-end server: `yarn start`

## User Stories and Wireframes :
