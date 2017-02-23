What problem does virtualenv solve? If you like Python as much as I do, chances are
you want to use it for other projects besides Flask-based web applications.  But the
more projects you have, the more likely it is that you will be working with different
versions of Python itself, or at least different versions of Python libraries. Let’s face it:
quite often libraries break backwards compatibility, and it’s unlikely that any serious
application will have zero dependencies.  So what do you do if two or more of your
projects have conflicting dependencies?
Virtualenv  to  the  rescue!   Virtualenv  enables  multiple  side-by-side  installations  of
Python, one for each project.  It doesn’t actually install separate copies of Python, but
it does provide a clever way to keep different project environments isolated. Let’s see
how virtualenv works.
If you are on Mac OS X or Linux, chances are that the following command will work
for you:

generic pip as admin.
sudo pip install virtualenv

debian / ubuntu
$ sudo apt-get install python-virtualenv

windows: easyinstall


$ mkdir myproject
$ cd myproject
$ virtualenv venv
New python executable in venv/bin/python
Installing setuptools, pip............done.

Now, whenever you want to work on a project, you only have to activate the corre-
sponding environment. On OS X and Linux, do the following:
$ . venv/bin/activate

If you are a Windows user, the following command is for you:
$ venv\Scripts\activate

Either way, you should now be using your virtualenv (notice how the prompt of your
shell has changed to show the active environment).
And if you want to go back to the real world, use the following command:

$ deactivate


con virtual env activado:
(venv)$ pip install flask

sin virtual env: sudo pip install flask

pro dev install:

$ git clone http://github.com/pallets/flask.git
Initialized empty Git repository in ~/dev/flask/.git/
$ cd flask
$ virtualenv venv
New python executable in venv/bin/python
Installing setuptools, pip............done.
$ . venv/bin/activate
$ python setup.py develop
...
Finished processing dependencies for Flask
