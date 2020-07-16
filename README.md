# cookiecutter-django-star-ratings

Details of the repo:

1) OVERVIEW: I am a noob learning django.  I have been building small django apps using online tutorials.  I am now using cookiecutter-django because of the advanced boilerplate + customized authentication mechanism.

2) PURPOSE OF THIS REPO: Provide a copy of tutorial files for review by the django-star-ratings project.

3) PROBLEM: Cookiecutter-django + django-star-ratings results in the following error message:

[15/Jul/2020 21:11:16] "POST /ratings/13/12/ HTTP/1.1" 403 2513
Forbidden (CSRF token missing or incorrect.): /ratings/13/12/
WARNING 2020-07-15 21:11:17,018 log 6472 139995847243520 Forbidden (CSRF token missing or incorrect.): /ratings/13/12/

4) BASIC DESCRIPTION:

a) I am able to build a simple to do app using VANILLA DJANGO + DEFAULT DJANGO AUTH MECHANISMS + DJANGO-STANDAR-RATING package without a problems.  Star ratings works great for authenticated and public users perfectly as per config options.  

b) When I build the same todo app using COOKIECUTTER-DJANGO + COOKIECUTTER-DJANGO-AUTH + DJANGO-STAR-RATINGS package, everything renders perfectly but when a rating is clicked, server logs show the following error:

[15/Jul/2020 21:11:16] "POST /ratings/13/12/ HTTP/1.1" 403 2513
Forbidden (CSRF token missing or incorrect.): /ratings/13/12/
WARNING 2020-07-15 21:11:17,018 log 6472 139995847243520 Forbidden (CSRF token missing or incorrect.): /ratings/13/12/

The reason for using cookiecutter-django is primarily because of their customized authentication mechanism as noobs should not be reinventing security.  Cookiecutter-django seems to have a nice customized auth mechanism that takes into account dev concern as seen in various django talks.

5) INSTRUCTIONS 

a) proj_tut15_ratings <-- full set of tutorial files including a vanilla cookiecutter-django install + my simple todo app called "app_todo".

b) This is a vanilla cookiecutter-django install, I just added the TODO app icon in the top menu.

c) I am using Postgres as the database for the install.

d) Perhaps the easiest way to get this running is to:

* Download the files.

* Maybe the easiest way to get this repo up and running is:

Pip install the requirements from cookiecutter-django-star-ratings/proj_tut15_ratings/requirements/ as appropriate and point it to the database of your choice.

e) Once you are logged in as a user, select the todo app, create some todo items.  Click the UPDATE button to see the star rating.

f) Please note this does not use the default django auth mechanisms but the customized cookiecutter-django project authentication.

6) REFERENCES:

a) Cookiecutter-django:  https://github.com/pydanny/cookiecutter-django

b) Django-star-ratings: https://github.com/wildfish/django-star-ratings/issues

c) My todo app is located here:  https://github.com/aykaramba/cookiecutter-django-star-ratings/tree/master/proj_tut15_ratings/proj_tut15_ratings/app_todo

It was written based on a couple of tutorials online.

7) ATTEMPTS AT RESOLUTION

Basically, after I wrote the todo app on the cookiecutter-django config and noticed the csrf issue, I went back and:

a) Rewrote the app from scratch using a brand new plain django install using the default django auth mechanisms.  The django-star-ratings app worked perfectly.  I was able to configure it to only allow ratings for signed in users or the public.  Works great.

b) Then, I did a fresh install of cookiecutter-django so that no files were polluted from my learning process.  I ported the todo app from the working vanilla django setup and update the app to use the cookiecutter-django authentication mechanism.

In earlier attempts to get django-star-ratings to work with cookiecutter-django I thought I was doing something wrong with either my todo app config or the django-star-ratings config.  Having started with a vanilla cookicutter-django setup + todo app (ported from working copy) + updated auth mechanism to cookiecutter-django, I was able to replicate the csrf error message from above.

8) CURRENT STATUS OF ISSUE

The csrf error strongly suggests that this is most likely an issue with my attempt to use the cookiecutter-django auth mechanism.  However, as I have managed to get django-star-ratings to work with vanilla django auth, it is possible that the way cookiecutter-django auth handles csrf tokens is opaque to django-star ratings.

I am too noob to be able to drill down into this any further at this point.
