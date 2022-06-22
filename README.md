# Project vecindarioyakwa

## By Kelly Kiiru

## Description

A Simple django project that lets users join neighbourhoods thar interest them. If their neighbourhood is not in the database, they can add it and other members can.
Members of a particular neighbourhood can add business and posts to be seen by all.

## Table of Content

+ [Description](#description)
+ [Setup/Installation Requirements](setup&installationrequirements)
+ [BDD & TDD](#bdd&tdd)
+ [UserStory](#userstory)
+ [Technology & Tools](#technology&tools)
+ [Reference](#reference)
+ [Licence](#licence)
+ [Authors Info](#authors-info)




## Setup Installations Requirements
   * To run the application, in your terminal:

    1. Clone this [github repo] (https://github.com/KellyKiiru/django-ip4.git)
    2. Create a virtual environment
    3. Read the requirements file and Install all the requirements. Or run pip3 install -r requirements.txt to automatically install all the requirements
    4. Run server depending on your python interpreter
  
#### Prerequisites

You must have git, django, postgres and python3.8+ installed in your pc.
To install django and Postgres, you can use the following commands:

#django
$ pip install django

#postgres
$ sudo apt-get install postgresql postgresql-contrib libpq-dev

### Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 


### Deployment environment
* Heroku

## BDD

|        User Requirements             |           Input                            |           Output                                    |
|--------------------------------------|----------------------------------------- --|-----------------------------------------------------|
| View neighbourhoods                  | Go to the home page                        | Neighbourhoods by other users will be displayed     |
| Add your neighbourhoods              | Click on add hood to add your neighbourhood| Your neighbourhood will be displayed                |
| Add businesses to neighbourhoods     | Click on add business to add a business    | Neighbourhoods' business will be displayed          |
| Add posts in neighbourhood           | Click on add post                          | Fill in a form to add posts for neighbourhood       |
| Search for businesses                | Use search bar to search for business      | Fill in a form to add posts for neighbourhood       |
| Join a neighbourhood                 | Click on join hood to join                 | You will be added as a member of that neighbourhood |




## TDD

To test the app, run this command in the terminal;

`$ python3 manage.py test`


## User Story
* View projects by other users. 
* User signs up and logs in.
* User edits their profile
* Add projects.
* User can give his rating for projects they desire to rate.

### Technology & Tools
* Python
* Django
* HTML
* CSS
* Django-Bootstrap5
* Postgres
* Javascript
* Pip
* Heroku

## Reference

* [Setting up Postgres, SQLAlchemy, and Alembic](https://realpython.com/django-by-example-part-2-postgres-sqlalchemy-and-alembic/)
* [django for Beginners](https://djangoforbeginners.com/introduction/)


## License

MIT License

Copyright (c) 2022 `Kelly Kiiru` 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Authors Contact Details

* [Email](infowithkiiru@gmail.com)
* [LinkedIn](https://www.linkedin.com/in/kiiru-ryan-15a852231/)

