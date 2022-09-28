# Farm Fresh

## Introduction



## Table of Contents

* [Conception](#Conception)
  * [Project Scope](#Project-Scope)
  * [Basic Wireframe Design](#Basic-Wireframe-Design)
  * [Agile](#Agile)

* [Project Setup](#Project-Setup)
  * [Installing Django and supporting libraries](#Installing-Django-and-supporting-libraries)
  * [Create new Django project and app](#Create-new-Django-project-and-app)
  * [Django Allauth](#django-allauth)
    * [Required Django Allauth settings](#required-django-allauth-settings)
  * [Deployment on Heroku](#Deployment-on-Heroku)
    * [Steps to create Heroku App](#Steps-to-create-Heroku-App)
    * [Setting up Config Vars](#Setting-up-Config-Vars)
    * [Wiring up the Database](#Wiring-up-the-Database)
    * [Cloudinary Setup](Cloudinary-Setup)
    * [Deployment](#Deployment)

* [Deployment Testing](#Deployment-Testing)

* [Features - Existing Features](#features---existing-features)

* [MVT Architecture](#MVT-Architecture)
  * [Models](#Models)
  * [Views](#Views)
  * [Templates](#Templates)

* [Access Control](#Access-Control)

* [Features - Features Left To Implement](#features---features-left-to-impliment)

* [Testing](#Testing)
  * [Manual Testing](#Manual-Testing)
  * [Validator Testing](#Validator-Testing)
    * [Initial Validator Tests](#Initial-Validator-Tests)
    * [Final Validator Tests](#Final-Validator-Tests)
  * [Unfixed Bugs](#Unfixed-Bugs)

* [Credits](#Credits)
  * [Content](#Content)
  * [Media](#media)


## Conception

My thinking was that given the requirements of the project, it would be very beneficial to formulate some kind of plan which would lay out the basic scope and design of my project in order to have some kind of structure with which to work with in order to avoid missing any crucial steps during construction and make the whole construction process as efficient as possible.

I made use of the following resources in order to plan and visualise my project, named Farm Fresh:
 - I made use of [Lucidchart](https://www.lucidchart.com/pages/) to design flowcharts in order to visualise the scope of my ideas and thought processes.
 - I also made use [Lucidchart](https://www.lucidchart.com/pages/) to plan my use of Agile methodology and common practices, taught to me by Code Institute.
 - [Lucidchart](https://www.lucidchart.com/pages/) has a ERD diagram template which I used to plan Ocean Basket's model.
 - I made use of [Balsamiq](https://balsamiq.com/) in order to create a basic wireframe design for Ocean Basket's webpages.


 ### Project Scope


### Basic Wireframe Design

Once I had the basic scope and logic in place, I then proceeded to design a visual representation of what is needed for the basic functionality of the project from a user's point of view and how I would represent that.



### Agile

I made use of agile common practises as described in the Code Institute tutorials. I did my best to come up with a complete layout of my agile plan from the get go but will make decisions in logical stages and update my diagrams and processes as the project develops, while documenting everything as the build progressed.

This is how I approached the challenge:

1. After reading the project requirements and the User's goal for the project idea that I had selected, I came up with the project's user goal, themes and epics.
2. From the epic's I derived the various user stories and built on this as the project developed.
3. Once I had created some user stories, I then came up with the relevant tasks for each user story.
4. After creating some stucture and scope for how to approach the task at hand, I started recording all my processes on Github:
    - I created user story templates on Github for efficiency in the Agile process.
    - I made use of Github issues to create and manage my user stories and for future defects if they arise.
    - I also came up with user story acceptance criteria which I added to the user stories on Github issues.
    - I allocated each user story with user story points, just as good practice.
    - A product backlog was also created using Github milestones, and managed throughout the development of the project in order to structure my development process.
    - As the build developed I would make refinements to the backlog.
    - I also created an iteration milestone on Github for use in this project as a timebox.
    - I made use of MoSCow prioritization by creating labels on Github and allocating them to the relevant user stories.
    - I created a Kanban board for use as an information radiator in this project by using "projects" on Github.


## Project Setup

After completing the basic conception of my idea and designing some basic structure to it, I then proceeded to setting up my IDE for the project using the steps recommended by Code Institute, namely:
1. Install Django
2. Create new Django project and app
3. Install Django Allauth

### Installing Django and supporting libraries

1. Install Django version 3.2 which is the Long Term Support version of Django and recommended by Code Institute for the use on our projects.

### Create new Django project and app

1. Create new blank Django project and name it farm_fresh.
2. Migrate changes to database after creating the project
3. Test if project is working correctly.

### Django Allauth

Opposed to building my own authentication system, allauth already has all the features I'll need for the site and it's completely customizable and will allow me to add even more functionality later on. Additionally, it's open-source so it's backed by millions of developers who keep it secure and up-to-date and it's unlikely that I would be able to create something better without a ton of extra development time.

#### Required Django Allauth settings

1. The request context processor, `'django.template.context_processors.request'`, allows allauth and django itself to access the HTTP request object in the templates, i.e. to access request.user or request.user.email in the django templates. It's required because the allauth templates use the request object frequently.
2. The authentication backend, `'allauth.account.auth_backends.AuthenticationBackend'`, in the setting.py file of the Farm Fresh project allows users to log into the store via their email address.
3. The other back-end, `'django.contrib.auth.backends.ModelBackend'` handles superusers logging into the admin which allauth doesn't handle. So I deferred to the default django Code for that.
4. The apps I added to the installed apps in the setting.py file of the Farm Fresh project, are allauth itself and these two: `'allauth.account'`, which is the allauth app that allows all the basic user account functionality like logging in and out, user registration and password resets. `'allauth.socialaccount'` which specifically handles logging in via social media providers like Facebook and Google.
5. The contrib.sites app and the site _id setting I added to the setting.py file of the Farm Fresh project, are used by the social account app to create the proper callback URLs when connecting via social media accounts.
6. I also created a path called accounts in the project level `urls.py` file and used it to include all the Django Allauth urls. I did this manually to keep everything consistent with the version of django that I have used.

## Access Control

I have created a few users which will be helpfull for testing the project:

**Superuser**

I created a Superuser in order to access the admin functions of Django. The Superuser is also what I use to create employees, as it is now a new employee can register his or her self the same way as a customer and with the Superuser logged in, one can allocate the "is Staff" property on the admin site.

 Credentials:
   - Username: **farmfreshowner**
   - Email: **joaorodrigues1@gmx.de**
   - Password: **FreshProduce45** (case sensitive)

# Testing

## Manual Testing

- After creating the `farm_fresh` project in Gitpod, I tested it buy running the application and recieved visual confirmation that the application is working successfully from Django.

**Image Placeholder**

## Validator Testing

- I Made use of the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/) for the CSS file and the official [W3C validator](https://validator.w3.org/) for all HTML file testing.
- I made use of [PEP8 online checker](http://pep8online.com/) to validate all python code.

## Unfixed Bugs

None that I am aware of.

## Credits

### Content

 - All flowcharts and ERD diagrams used in this project were designed by making use of [Lucidchart](https://www.lucidchart.com/pages/).
 - All wireframes used in this project were designed by making use of [Balsamiq](https://balsamiq.com/).
 - I learned how to use `inline code blocks` in a Markdown file on [RIP Tutorial](https://riptutorial.com/markdown/example/1802/inline-code).
 - Git commit message best practices taken from [How to Write Good Commit Messages: A Practical Git Guide](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/)
 - I made extensive use of Code Institute's learning content and tutorials throughout the project for revision as well as usefull content for my readme file.
 - I made extensive use of the Django Allauth documentation for most aspects of setting up authorisation for this project.
