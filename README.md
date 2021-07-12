# Setup
The first thing to do is to clone the repository:

$ git clone https://github.com/29Sagar/Assignment.git
$ cd AssignmentProject
Create a virtual environment to install dependencies in and activate it:

$ virtualenv env
$ source env/bin/activate
Then install the dependencies:

(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.

Once pip has finished downloading the dependencies:

(env)$ python manage.py makemigration

(env)$ python manage.py migrate

(env)$ python manage.py runserver

And navigate to http://127.0.0.1:8000

Also view the Solution Pdf.
