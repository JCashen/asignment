# Game Review App

### Resources:
* Presentation: https://drive.google.com/drive/folders/1l0UabMEmIxZCMybOGpOZ7pdD992q2xq7?usp=sharing
* Git Project Board: https://github.com/users/JCashen/projects/2


## Contents
* [Brief](#brief)
   * [Additional Requirements](#additional-requirements)
   * [My Approach](#my-approach)
* [Architecture](#architecture)
   * [Database Structure](#database-structure)
   * [CI Pipeline](#ci-pipeline)
* [Project Tracking](#project-tracking)
* [Risk Assessment](#risk-assessment)
* [Testing](#testing)
* [Front-End Design](#front-end-design)
* [Known Issues](#known-issues)
* [Future Improvements](#future-improvements)
* [Authors](#authors)

## Brief
The brief for this project was for us to create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

### Additional Requirements
In addition to what has been set out in the brief, I am also required to include the following:
* A Trello board
* A relational database, consisting of at least two tables that model a relationship
* Clear documentation of the design phase, app architecture and risk assessment
* A python-based functional application that follows best practices and design principles
* Test suites for the application, which will include automated tests for validation of the application
* A front-end website, created using Flask
* Code integrated into a Version Control System which will be built through a CI server and deployed to a cloud-based virtual machine

### My Approach
To complete these requirements i decided to create a games review app which allows the user to:
* Create a review for games that are on the site:
* View and update their review
* Delete their review
* Read all reviews left by themselves and others


## Architecture
### Database Structure
Below is an entity relationship diagram (ERD) showing the structure of the database.

![ERD][erd1]

As shown in the ERD, this app includes a 1 to many relationship this is because 1 game can have many reviews.

### CI Pipeline
![ci][ci]

Pictured above is the continuous integration pipeline.


## Project Tracking
GITHUB was used to track the progress of the project as seen on this board: https://github.com/users/JCashen/projects/2
this board contains the Scope, user stories and what has been completed from the scope.

## Risk Assessment
The risk assessment for this project can be found here: https://docs.google.com/spreadsheets/d/1YecfPLMsuUKFU-JJGClkGe4hGCTGjVRufPJmL98_vfk/edit?usp=sharing


## Testing
pytest is used to run unit tests on the app. this was used as it includes a coverage chart which allows the user to see how much of the program has been tested.


![coverage][coverage]


## Front-End Design
below is a screen grab of the home page of the design which when first ran looks very empty.

![home][home]

The user is able to add stuff to the home page though by clicking on the add link which takes them to an add page where they can fill out the form and click submit to add a review to the home page and database.

![add][add]

once redirected the user can see thier review on the homepage

![homeafteradd][homeafteradd]

now under the review is an update and delete button if the user hits update it takes them to a page where they can update and if they click delete it deleted the review entirely.

![update][update]


## Authors
Joshua Cashen

[erd1]: https://i.imgur.com/vp6uuh4.jpg
[ci]: https://i.imgur.com/O7s7DkY.png
[coverage]: https://i.imgur.com/orV6J8P.jpg
[home]: https://i.imgur.com/aAbAnCN.jpg
[add]: https://i.imgur.com/tBNdQoT.jpg
[update]: https://i.imgur.com/4Tqp5ab.jpg
[homeafteradd]: https://i.imgur.com/jaLXGjR.jpg
