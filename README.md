<a id="idtext"></a>

# 🎮 Console Logs 🎮
![App Screenshot](https://img.shields.io/badge/version-v1.0-green)

![App Screenshot](https://img.shields.io/badge/-WORK%20IN%20PROGRESS..-orange)

## Developers 
- [Ali Ali](https://github.com/alibeniaminali) 
- [Thor Refoy](https://github.com/thor-r) 
- [Peter Bid](https://github.com/PeterBid)

## Overview
![App Screenshot](https://i.imgur.com/0e46Gey.png)
![App Screenshot](https://i.imgur.com/JUxgukl.jpg)

## Table of Contents
- [Concept](#concept)
  - [Get started](#get-started)
  - [Project Brief](#project-brief)
- [Technologies Used](#technologies-used)
 - [Installation instructions](#installation-instructions)
- [Planning and Wireframes](#planning-and-wireframes)
- [General Approach](#general-approach)
 - [Day 1-7](#day-1)
- [Unsolved Problems](#unsolved-problems)
- [Features Wish List](#features-wish-list)
- [Key Learnings](#key-learnings)
- [Author](#authors)

## Concept
A full-stack desktop application developed during my last week at the General Assembly Software Engineering Course.
Console Logs is a social media platform, where people can share and upload video clips of gaming footage related to specific games, and allows other users to comment on them.

## Timeline
- 7 days

## Get started 
#### You can register to the website or if you would like to experience the website with seeded data in it, you can log with the following:
- Email : ali4@email.com
- Password : sei61-pass

## Project Brief
- One week to plan, build, and test our final project with a focus on cementing the learning from the past 11 weeks and showing off our new Python skills.
- Build a full-stack application by making your own backend and your own front-end
- Use a Python Django API using Django REST Framework to serve your data from a Postgres database
- Consume your API with a separate front-end built with React
- Be a complete product which most likely means multiple relationships and CRUD functionality for at least a couple of models
## Technologies Used
### Database:
- [x]  PostgreSQL
### Backend:
- [x]  Python
- [x]  Django
### Frontend:
- [x]  JavaScript (ES6)
- [x]  React.js
- [x]  HTML5
- [x]  CSS3 + SASS
- [x]  React Bootstrap
### Dependencies:
- [x]  djangorestframework
- [x]  pyjwt
- [x]  python-dotenv
- [x]  psycopg2-binary
- [x]  Axios
- [x]  react-router-dom
- [x]  JSONWebToken
### Development Tools:
- [x]  VS Code
- [x]  Git + GitHub
- [x]  Insomnia
- [x]  TablePlus
- [x]  Heroku
- [x]  pylint
- [x]  Figma
- [x]  Cloudinary
## Installation instructions
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
9. Start front-end server: `yarn start`</br>

[Back to the top ⬆️](#idtext)

## Planning and Wireframes
### Front End
![App Screenshot](https://i.imgur.com/djOFgsb.png)
### Back End
#### Database Entity Relationship Diagram
![App Screenshot](https://i.imgur.com/g0xnq0B.png)
## General Approach
### Day 1
- We spent the first day going through different ideas and concepts and one of my teammates suggested we try and create a website similar to [twitch.tv](https://www.twitch.tv/), but with a much cleaner UI.
- My partners and I began by mocking up a basic wireframe and planning the look of our website by using Figma. (above)
- We next created an entity relationship diagram (ERD) for our database tables and relationships (above).
- We followed an Agile system for starting each day with a standup for three of us, followed by a standup for the group leaders of each group on the course.
### Day 2
- We decided to work together on the backend, where one of us was typing the code, while the other two were going through the plan, looking for typos, making sure all the models were connected correctly and looking into our notes if needed.
- We started out by scaffolding the backend, adding the PostgreSQL database, writing seeds, and installing dependencies. All of this went surprisingly smoothly, which showed us we had come a long way from our first projects.
- Using Django, we set up the "apps" for the games, media, comments, genres, and authentication. Then we wrote the models, URLs, and views for all of these.
#### Game models
- `app_name.ModelName` details the relationship with the foreign table. In our case `genres.Genre`
- `related_name` field specifies the games will show as when querying the foreign table (in our case `genres`)
- We also reformat the individual record string on the admin site so it's easier for us when adding our seeds and seeing the names of our games.
![App Screenshot](https://i.imgur.com/xol6IYv.png)
#### Serializers
- Next, we began writing serializers for each app only as needed, and adding additional RESTful routes and serializers.
![App Screenshot](https://i.imgur.com/cDvM4zv.png)
![App Screenshot](https://i.imgur.com/yND7Knt.png)
#### Game views
- `Game.objects.all()` makes request to the database for all entries in the games table
- Then, we populated our games, using our `PopulatedGameSerializer`
![App Screenshot](https://i.imgur.com/yAhQmET.png)

[Back to the top ⬆️](#idtext)

### Day 3 & 4
- We spent those two days finishing our backend, adding all the functionality and authentication, testing each RESTful route using Insomnia as well as Django's built-in admin page.
![App Screenshot](https://i.imgur.com/J7iEDxY.png)
- Sending a POST request on Insomnia to Login
![App Screenshot](https://i.imgur.com/cJnyFbu.png)
### Day 5, 6 & 7
- We started Day 5 by adding a React front end to our project and divided up the router and component setup.
- For styling we decided to use [React Bootstrap](https://react-bootstrap.github.io/)
- I designed the logo and the nav bar and moved on to the Front End authentication.
- After that I start styling both `Login `and `Registration` forms
![App Screenshot](https://i.imgur.com/CPpLVP4.png)
![App Screenshot](https://i.imgur.com/N2tsYAi.png)
- On the next day, I added the styling on the Home/Index page and displayed the games in separate cards. I also added a hover effect so when the user is going through each game the card scales up.
![App Screenshot](https://i.imgur.com/FDMVbN3.png)
- After that, I styled our Footer and added the links to our GitHub repositories and LinkedIn.
![App Screenshot](https://i.imgur.com/hbcBuUP.png)
- On the last day I spent most of my time styling all the individual video info pages and adding avatars to the users that left a comment.
![App Screenshot](https://i.imgur.com/EU5bSuA.png)
- Then I moved onto styling the Upload form page.
![App Screenshot](https://i.imgur.com/8zDsLZw.png)

[Back to the top ⬆️](#idtext)

## Unsolved Problems
- ![App Screenshot](https://img.shields.io/badge/-NOT%20DEPLOYED-red)
- We didn't have enough time to style the user's Profile page
- We also couldn’t format the timestamp to show the upload day properly
- We tried to display the 5 most viewed videos ,but the function didn’t work properly as every time we refresh the page, new videos appeared

## Challenges and Wins
### Challenges
Working with Django felt pretty straight forward at the beginning, as we were able to see our work visually in the admin site. Once our database got bigger the challenges that we had were to create each model and to create the relashionships between them.

GitHub - We didn't set up our branches properly at the beginning and we were not able to push any changes, so the owner of the repository had to copy all of the changes we made each day and apply it to the development branch, so we can then pull the changes that he made. We thought that this will save us time, but at the end I think this took away a lot of valuable time. In the next projects I will always make sure that we have everything set up properly before I start building.

### Wins
I think we worked well as a team and considering that we had a small amount of time we were able to create a website that is visually appealing and clean. 

On previous projects we were always working with images upload, but never videoclips. I am happy that we were managed to do that for this project and users can upload videos and also have playback speed, download and picture in picture settings available.

- ![App Screenshot](https://i.imgur.com/0SPFrS8.png)

## Features Wish List
- Users can like/dislike video
- Users can save the video and find it in their private profile page
- Users can share the video with their friends on Social media

## Key Learnings
- I had a lot of fun during this project and enjoyed working as a team. This project helped me understand the importance of setting up the backend properly and following our schedule step by step so we don't run into major issues later on. I also solidified my Front End skills and also working with React Bootstrap components.</br>

[Back to the top ⬆️](#idtext)

## Authors
- LinkedIn - [Ali Ali](https://www.linkedin.com/in/alibeniaminali/)
- Email - alibeniaminali@gmail.com

 [Back to the top ⬆️](#idtext)
 



