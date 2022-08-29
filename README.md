# Sharetness

Hi CS50, I'm Alejandro Ferrera, I'm from Cuba but I'm living in Chile right now. I am a software engenieer student from an institute here in Chile. I'm here today to present my Final Project. The idea behind this project is to create a forum for fitness people. People here can create rooms with diferent topics and share some ideas in chat. The project was created on Django, I wanted to learn django because Python is my favorite language and django is the most required framework by employers.

## Users system
For users manipulation (Login, Logout, Sessions) I used the default django user model with some modifications, and I create a superuser that can use the admin panel.

## Models
For database I used SQLite default version in Django and I created different models to handles the database. (Rooms, Topics and messages). The relation was between this tables are implicity in django models.

## Forms
I used the form model almost all the time for the CRUD functions.

## Style
For style I used bootstrap 4 and crispy-form filter for the forms. Also some basic CSS.

## Business Rules
The business logic is simple, I added a logic for delete a message if this message was created in more than one minute, thanks to django documentation for that example :D.
