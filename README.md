# Dental Laboratory – Database
Inspired from my time working in the dental profession when dental laboratory work was recorded in a paper book. I doubt this 
practice is still in use with the technology available today. To assist companies that may have not moved form the practice of paper records in chosng an IT system for their needs, I have chosen to produce a dental laboratory database for my project.  
# UX
A basic design to capture all the information that generally accompanies a dental laboratory prescription, it also allows the user to make modifications to contents of the database as necessary. Designed with simplicity for the user in mind, on opening the database the home page is also the sign in page. At the base of the sign in 
is the option for a new user to register  or if the user wishes to, can click on Register on the navigation bar at the top of the page.

## User Story
The main objective of this milestone project is the CRUD oepration and this basically aligns with the function of the
dental laboratory recording system whether it is in paper form or digital.

As a user Type| I want to perform an action |So that I can achieve a goal|Type of Action|
--------------|----------------------------|----------------------------|---------------|
Dental Technician| View and Navigate | See outstanding patient Jobs| Read |
Dental Technician| View and Navigate | See all Patients and Jobs| Read |
Any User | View and Navigate | See outstanding patient Jobs | Read |
Dental Technician | Add new patients | Maintain a record of new jobs | Create|
Dental Technician | Add new patients | Maintain a record of new jobs | Create|
Any User | Add new Jobs and Patient Type| Maintain accurate Job specifications and Patient types |Create|
Dental Technician| Add new Jobs and Patient Type| Maintain accurate Job specifications and Patient types |Create|
# Features

## Home

* The display format function buttons, patient name and date of birth
Dropdown display is appointment date, (due date) for the appliance to be fitted and the name of the appliance.
The appliances are requested from the dentist and on arrival of the request the patient is added to the database using the New patient tab. When the Job is returned and fitted on the appointment date then the patient is deleted when selecting the Done button. Any amendments can also be made by selecting the edit button.

## Jobs

* The requested appliance is a job for the dental technician and on the new patient form, there is a dropdown list of various jobs that are ubiquitously requested. When designing the database allowance has been made for jobs that are not commonly requested and these can be added to the database using the add job function by selecting the Manage Jobs in the navbar.

## Manage Jobs

* The display format function buttons and name of the appliance and at the base of the form is the add job button.

## Type

* In the dental profession there are patient types to determine the cost of treatment that can be afforded. The most common patient types are NHS or Private.  There is a limit charge which is set by the government that can be afforded to an NHS patient irrespective of the treatment supplied.  There are also no charges for certain treatment for children and under eighteens who are still in full time education.  Just as the requested jobs, an allowance has been made for any patient types that may have been overlooked in the design or that may appear later on and these can be added to the database using the add type function by selecting Manage Types in the navbar.

## Manage Type

The display format function buttons and patient type and at the base of the form is the add type button.

# Features Left to Implement

The database has scope for a wide range of functionality firstly great potential as a cloud based b2b application linked directly to the dental practices.  Future additions:

* i.	Registration form

* ii.	Billing and address information

* iii.	Dental appliance design page with a link to a virtual description and assisted designing of the appliance

* iv.	Virtual assistant Live chat functionality

* v.	Alert function for overdue or jobs close to the appointment date

* vi.	Timeout after a period of inactivity

* vii.	Social Media and Contact Links

* viii.	Log out functionality

* ix.	Registered Dental Practices Allocated database – (The dental practice would be identified by a unique number allocated during registration and when the unique number is entered the database would open displaying only patients from that particular practice.)

*  x.	Add archive storage function for patients and all jobs completed

*  xi.  Further error handling around the IDs in app.py to catch errors and to avoid maliciuos inserts that would crash the application

*  xi.  Password reset link

# Technologies used

* HTML
* CSS 
* Javascript
* Python and Flask
* MongoDB
* JQuery
* Materialize

# Testing

At each stage of a new function and template the code was tested running through the browser to check for errors. The errors were picked up in jinja and werkzeug and also in the terminal window. Any errors were then corrected before running the code again through the browser. 
Various background features and colours were tested as well as styling using the browser and the inspect window. On right clicking and selecting inspect, one can choose the various platform views i.e iphone 6, Ipad or Desktop etc.
Responsive testing for mobile view was carried out using the inspect window.
There were quite a few errors when trying to deploy to heroku and these were corrected as they were highlighted resulting in several commits titled "Modified". Please see the process and resolution of these errors below.

* *gitpod /workspace/dental_laboratory $ python3 app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 244-990-707
127.0.0.1 - - [19/May/2020 19:11:37] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [19/May/2020 19:11:39] "GET /add_patient HTTP/1.1" 500 -
Traceback (most recent call last):
  File "/workspace/.pip-modules/lib/python3.8/site-packages/flask/app.py", line 2464, in __call__
    return self.wsgi_app(environ, start_response)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/flask/app.py", line 2450, in wsgi_app
    response = self.handle_exception(e)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/flask/app.py", line 1867, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/workspace/.pip-modules/lib/python3.8/site-packages/flask/app.py", line 2447, in wsgi_app
    response = self.full_dispatch_request()
  File "/workspace/.pip-modules/lib/python3.8/site-packages/flask/app.py", line 1952, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/flask/app.py", line 1821, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/workspace/.pip-modules/lib/python3.8/site-packages/flask/app.py", line 1950, in full_dispatch_request
    rv = self.dispatch_request()
  File "/workspace/.pip-modules/lib/python3.8/site-packages/flask/app.py", line 1936, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/workspace/dental_laboratory/app.py", line 41, in add_patient
    return render_template('addpatient.html', jobs=mongo.db.jobs.find(),
NameError: name 'mongo' is not defined
127.0.0.1 - - [19/May/2020 19:11:39] "GET /add_patient?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 200 -
127.0.0.1 - - [19/May/2020 19:11:39] "GET /add_patient?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 200 -
127.0.0.1 - - [19/May/2020 19:11:39] "GET /add_patient?__debugger__=yes&cmd=resource&f=jquery.js HTTP/1.1" 200 -
127.0.0.1 - - [19/May/2020 19:11:40] "GET /add_patient?__debugger__=yes&cmd=resource&f=ubuntu.ttf HTTP/1.1" 200 -
127.0.0.1 - - [19/May/2020 19:11:40] "GET /add_patient?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 200 -
127.0.0.1 - - [19/May/2020 19:11:40] "GET /add_patient?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 200 -
 * Detected change in '/workspace/dental_laboratory/app.py', reloading
 * Restarting with stat
  File "/workspace/dental_laboratory/app.py", line 15
    app.config['mongo = PyMongo(app)
                                   ^
SyntaxError: EOL while scanning string literal
gitpod /workspace/dental_laboratory $ heroku ps:scale web=1
 ›   Warning: heroku update available from 7.39.5 to 7.41.1.
Scaling dynos... done, now running web at 1:Free
gitpod /workspace/dental_laboratory $ heroku logs --tail
 ›   Warning: heroku update available from 7.39.5 to 7.41.1.
2020-05-19T18:39:55.991245+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T18:39:55.991245+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T18:39:55.991384+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T18:39:55.991386+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 144, in init_app
2020-05-19T18:39:55.991551+00:00 app[web.1]: "You must specify a URI or set the MONGO_URI Flask config variable",
2020-05-19T18:39:55.991568+00:00 app[web.1]: ValueError: You must specify a URI or set the MONGO_URI Flask config variable
2020-05-19T18:47:56.000000+00:00 app[api]: Build started by user lutersweg@hotmail.com
2020-05-19T18:48:28.690350+00:00 app[api]: Deploy 199002c5 by user lutersweg@hotmail.com
2020-05-19T18:48:28.690350+00:00 app[api]: Release v14 created by user lutersweg@hotmail.com
2020-05-19T18:48:29.926775+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T18:48:35.467623+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T18:48:35.374108+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T18:48:35.374174+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T18:48:35.374396+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T18:48:35.374429+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T18:48:35.374665+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T18:48:35.374698+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 144, in init_app
2020-05-19T18:48:35.374934+00:00 app[web.1]: "You must specify a URI or set the MONGO_URI Flask config variable",
2020-05-19T18:48:35.374976+00:00 app[web.1]: ValueError: You must specify a URI or set the MONGO_URI Flask config variable
2020-05-19T18:48:37.000000+00:00 app[api]: Build succeeded
2020-05-19T18:49:17.523586+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=291dab3a-e017-45c9-8b7b-98b3013a563d fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T18:49:18.120409+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=e77d6875-4d8f-4e11-911a-2c263f25db6c fwd="54.207.33.42" dyno= connect= service= status=503 bytes= protocol=http
2020-05-19T18:49:18.312193+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=dental-laboratory.herokuapp.com request_id=e72ea422-2fd5-45b2-8614-58c8ed1f3a15 fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T18:50:55.579697+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T18:51:01.605442+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T18:51:01.510746+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T18:51:01.510777+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T18:51:01.510990+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T18:51:01.511000+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T18:51:01.511243+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T18:51:01.511261+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 144, in init_app
2020-05-19T18:51:01.511519+00:00 app[web.1]: "You must specify a URI or set the MONGO_URI Flask config variable",
2020-05-19T18:51:01.511545+00:00 app[web.1]: ValueError: You must specify a URI or set the MONGO_URI Flask config variable
2020-05-19T19:05:51.028309+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=b44c4a21-b451-4810-99e1-22b9ffdb9582 fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:05:52.255122+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=dental-laboratory.herokuapp.com request_id=739d9c1e-6667-4edd-a754-ec1841702e96 fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:05:52.539412+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=badc7ed2-bed2-433a-9464-2bf310e54299 fwd="54.207.33.42" dyno= connect= service= status=503 bytes= protocol=http
2020-05-19T19:13:12.711300+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:13:18.627124+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:13:18.532973+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:13:18.532998+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:13:18.533107+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:13:18.533120+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:13:18.533250+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:13:18.533252+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 144, in init_app
2020-05-19T19:13:18.533391+00:00 app[web.1]: "You must specify a URI or set the MONGO_URI Flask config variable",
2020-05-19T19:13:18.533407+00:00 app[web.1]: ValueError: You must specify a URI or set the MONGO_URI Flask config variable
2020-05-19T19:17:38.546735+00:00 app[api]: Set IP config vars by user lutersweg@hotmail.com
2020-05-19T19:17:38.546735+00:00 app[api]: Release v15 created by user lutersweg@hotmail.com
2020-05-19T19:17:40.038542+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:17:46.410004+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:17:46.248971+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:17:46.248992+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:17:46.249261+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:17:46.249331+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:17:46.249777+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:17:46.249851+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 144, in init_app
2020-05-19T19:17:46.250238+00:00 app[web.1]: "You must specify a URI or set the MONGO_URI Flask config variable",
2020-05-19T19:17:46.250317+00:00 app[web.1]: ValueError: You must specify a URI or set the MONGO_URI Flask config variable
2020-05-19T19:18:19.200189+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=5983bc55-2bda-4b34-a245-0f1ae1431853 fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:18:19.785932+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=dental-laboratory.herokuapp.com request_id=a18f8201-3aa0-4d25-bf21-5af028aef17e fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:18:20.213185+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=5cd69577-28b6-4695-9bf4-8281eca2b3e4 fwd="3.101.0.4" dyno= connect= service= status=503 bytes= protocol=http
2020-05-19T19:23:39.723168+00:00 app[api]: Set SECRET_KEY config vars by user lutersweg@hotmail.com
2020-05-19T19:23:39.723168+00:00 app[api]: Release v16 created by user lutersweg@hotmail.com
2020-05-19T19:23:41.312173+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:23:48.018148+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:23:47.860235+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:23:47.860281+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:23:47.860393+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:23:47.860396+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:23:47.860536+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:23:47.860538+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 144, in init_app
2020-05-19T19:23:47.860689+00:00 app[web.1]: "You must specify a URI or set the MONGO_URI Flask config variable",
2020-05-19T19:23:47.860692+00:00 app[web.1]: ValueError: You must specify a URI or set the MONGO_URI Flask config variable
2020-05-19T19:24:30.631239+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=7ed89f28-200e-4cdb-bf0f-30eed84552be fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:24:31.451488+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=fb55d2db-1ce8-4cdb-bfae-f6d6e24378aa fwd="18.217.223.118" dyno= connect= service= status=503 bytes= protocol=http
2020-05-19T19:24:31.205418+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=dental-laboratory.herokuapp.com request_id=603f8438-d1c2-432b-81bd-9cf8db8ed578 fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:24:59.891787+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:25:05.421772+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:25:05.319516+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:25:05.319532+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:25:05.319730+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:25:05.319743+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:25:05.319918+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:25:05.319921+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 144, in init_app
2020-05-19T19:25:05.320064+00:00 app[web.1]: "You must specify a URI or set the MONGO_URI Flask config variable",
2020-05-19T19:25:05.320071+00:00 app[web.1]: ValueError: You must specify a URI or set the MONGO_URI Flask config variable
2020-05-19T19:26:44.831021+00:00 app[api]: Release v17 created by user lutersweg@hotmail.com
2020-05-19T19:26:44.831021+00:00 app[api]: Set SECRET_KEY config vars by user lutersweg@hotmail.com
2020-05-19T19:26:46.057574+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:26:51.870679+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:26:51.784861+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:26:51.784874+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:26:51.785036+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:26:51.785037+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:26:51.785217+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:26:51.785222+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 144, in init_app
2020-05-19T19:26:51.785379+00:00 app[web.1]: "You must specify a URI or set the MONGO_URI Flask config variable",
2020-05-19T19:26:51.785399+00:00 app[web.1]: ValueError: You must specify a URI or set the MONGO_URI Flask config variable
2020-05-19T19:27:39.107746+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=a1d603a0-c306-4d85-9cdd-e9c5606e7670 fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:27:39.953504+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=dental-laboratory.herokuapp.com request_id=ecb5eca9-fc3f-4f2d-acde-617b679e8587 fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:33:11.388165+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=685f2cff-a2ee-468b-8457-c88e4d404956 fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:33:11.973035+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=dental-laboratory.herokuapp.com request_id=10bffb0d-cc98-44ff-bff4-98f5337837bc fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:33:12.413285+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=ba3f76e2-7323-4c96-840c-54c6bba711da fwd="3.101.0.4" dyno= connect= service= status=503 bytes= protocol=http
^C
gitpod /workspace/dental_laboratory $ heroku logs --tail
 ›   Warning: heroku update available from 7.39.5 to 7.41.1.
2020-05-19T18:39:55.991386+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 144, in init_app
2020-05-19T18:39:55.991551+00:00 app[web.1]: "You must specify a URI or set the MONGO_URI Flask config variable",
2020-05-19T18:39:55.991568+00:00 app[web.1]: ValueError: You must specify a URI or set the MONGO_URI Flask config variable
2020-05-19T18:47:56.000000+00:00 app[api]: Build started by user lutersweg@hotmail.com
2020-05-19T18:48:28.690350+00:00 app[api]: Deploy 199002c5 by user lutersweg@hotmail.com
2020-05-19T18:48:28.690350+00:00 app[api]: Release v14 created by user lutersweg@hotmail.com
2020-05-19T18:48:29.926775+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T18:48:35.467623+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T18:48:35.374108+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T18:48:35.374174+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T18:48:35.374396+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T18:48:35.374429+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T18:48:35.374665+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T18:48:35.374698+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 144, in init_app
2020-05-19T18:48:35.374934+00:00 app[web.1]: "You must specify a URI or set the MONGO_URI Flask config variable",
2020-05-19T18:48:35.374976+00:00 app[web.1]: ValueError: You must specify a URI or set the MONGO_URI Flask config variable
2020-05-19T18:48:37.000000+00:00 app[api]: Build succeeded
2020-05-19T18:49:17.523586+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=291dab3a-e017-45c9-8b7b-98b3013a563d fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T18:49:18.120409+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=e77d6875-4d8f-4e11-911a-2c263f25db6c fwd="54.207.33.42" dyno= connect= service= status=503 bytes= protocol=http
2020-05-19T18:49:18.312193+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=dental-laboratory.herokuapp.com request_id=e72ea422-2fd5-45b2-8614-58c8ed1f3a15 fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T18:50:55.579697+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T18:51:01.605442+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T18:51:01.510746+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T18:51:01.510777+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T18:51:01.510990+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T18:51:01.511000+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T18:51:01.511243+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T18:51:01.511261+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 144, in init_app
2020-05-19T18:51:01.511519+00:00 app[web.1]: "You must specify a URI or set the MONGO_URI Flask config variable",
2020-05-19T18:51:01.511545+00:00 app[web.1]: ValueError: You must specify a URI or set the MONGO_URI Flask config variable
2020-05-19T19:05:51.028309+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=b44c4a21-b451-4810-99e1-22b9ffdb9582 fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:05:52.255122+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=dental-laboratory.herokuapp.com request_id=739d9c1e-6667-4edd-a754-ec1841702e96 fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:05:52.539412+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=badc7ed2-bed2-433a-9464-2bf310e54299 fwd="54.207.33.42" dyno= connect= service= status=503 bytes= protocol=http
2020-05-19T19:13:12.711300+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:13:18.627124+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:13:18.532973+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:13:18.532998+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:13:18.533107+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:13:18.533120+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:13:18.533250+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:13:18.533252+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 144, in init_app
2020-05-19T19:13:18.533391+00:00 app[web.1]: "You must specify a URI or set the MONGO_URI Flask config variable",
2020-05-19T19:13:18.533407+00:00 app[web.1]: ValueError: You must specify a URI or set the MONGO_URI Flask config variable
2020-05-19T19:17:38.546735+00:00 app[api]: Set IP config vars by user lutersweg@hotmail.com
2020-05-19T19:17:38.546735+00:00 app[api]: Release v15 created by user lutersweg@hotmail.com
2020-05-19T19:17:40.038542+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:17:46.410004+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:17:46.248971+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:17:46.248992+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:17:46.249261+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:17:46.249331+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:17:46.249777+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:17:46.249851+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 144, in init_app
2020-05-19T19:17:46.250238+00:00 app[web.1]: "You must specify a URI or set the MONGO_URI Flask config variable",
2020-05-19T19:17:46.250317+00:00 app[web.1]: ValueError: You must specify a URI or set the MONGO_URI Flask config variable
2020-05-19T19:18:19.200189+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=5983bc55-2bda-4b34-a245-0f1ae1431853 fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:18:19.785932+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=dental-laboratory.herokuapp.com request_id=a18f8201-3aa0-4d25-bf21-5af028aef17e fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:18:20.213185+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=5cd69577-28b6-4695-9bf4-8281eca2b3e4 fwd="3.101.0.4" dyno= connect= service= status=503 bytes= protocol=http
2020-05-19T19:23:39.723168+00:00 app[api]: Set SECRET_KEY config vars by user lutersweg@hotmail.com
2020-05-19T19:23:39.723168+00:00 app[api]: Release v16 created by user lutersweg@hotmail.com
2020-05-19T19:23:41.312173+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:23:48.018148+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:23:47.860235+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:23:47.860281+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:23:47.860393+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:23:47.860396+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:23:47.860536+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:23:47.860538+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 144, in init_app
2020-05-19T19:23:47.860689+00:00 app[web.1]: "You must specify a URI or set the MONGO_URI Flask config variable",
2020-05-19T19:23:47.860692+00:00 app[web.1]: ValueError: You must specify a URI or set the MONGO_URI Flask config variable
2020-05-19T19:24:30.631239+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=7ed89f28-200e-4cdb-bf0f-30eed84552be fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:24:31.451488+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=fb55d2db-1ce8-4cdb-bfae-f6d6e24378aa fwd="18.217.223.118" dyno= connect= service= status=503 bytes= protocol=http
2020-05-19T19:24:31.205418+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=dental-laboratory.herokuapp.com request_id=603f8438-d1c2-432b-81bd-9cf8db8ed578 fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:24:59.891787+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:25:05.421772+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:25:05.319516+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:25:05.319532+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:25:05.319730+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:25:05.319743+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:25:05.319918+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:25:05.319921+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 144, in init_app
2020-05-19T19:25:05.320064+00:00 app[web.1]: "You must specify a URI or set the MONGO_URI Flask config variable",
2020-05-19T19:25:05.320071+00:00 app[web.1]: ValueError: You must specify a URI or set the MONGO_URI Flask config variable
2020-05-19T19:26:44.831021+00:00 app[api]: Release v17 created by user lutersweg@hotmail.com
2020-05-19T19:26:44.831021+00:00 app[api]: Set SECRET_KEY config vars by user lutersweg@hotmail.com
2020-05-19T19:26:46.057574+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:26:51.870679+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:26:51.784861+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:26:51.784874+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:26:51.785036+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:26:51.785037+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:26:51.785217+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:26:51.785222+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 144, in init_app
2020-05-19T19:26:51.785379+00:00 app[web.1]: "You must specify a URI or set the MONGO_URI Flask config variable",
2020-05-19T19:26:51.785399+00:00 app[web.1]: ValueError: You must specify a URI or set the MONGO_URI Flask config variable
2020-05-19T19:27:39.107746+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=a1d603a0-c306-4d85-9cdd-e9c5606e7670 fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:27:39.953504+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=dental-laboratory.herokuapp.com request_id=ecb5eca9-fc3f-4f2d-acde-617b679e8587 fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:33:11.388165+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=685f2cff-a2ee-468b-8457-c88e4d404956 fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:33:11.973035+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=dental-laboratory.herokuapp.com request_id=10bffb0d-cc98-44ff-bff4-98f5337837bc fwd="90.202.46.200" dyno= connect= service= status=503 bytes= protocol=https
2020-05-19T19:33:12.413285+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=dental-laboratory.herokuapp.com request_id=ba3f76e2-7323-4c96-840c-54c6bba711da fwd="3.101.0.4" dyno= connect= service= status=503 bytes= protocol=http
2020-05-19T19:36:02.544991+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:36:08.547219+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:36:08.452919+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:36:08.452939+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:36:08.453058+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:36:08.453061+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:36:08.453205+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:36:08.453208+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 144, in init_app
2020-05-19T19:36:08.453384+00:00 app[web.1]: "You must specify a URI or set the MONGO_URI Flask config variable",
2020-05-19T19:36:08.453387+00:00 app[web.1]: ValueError: You must specify a URI or set the MONGO_URI Flask config variable
2020-05-19T19:38:18.567924+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:38:17.055018+00:00 app[api]: Release v18 created by user lutersweg@hotmail.com
2020-05-19T19:38:17.055018+00:00 app[api]: Set MONGO_URI config vars by user lutersweg@hotmail.com
2020-05-19T19:38:23.484545+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:38:23.416304+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:38:23.416319+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:38:23.416459+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:38:23.416459+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:38:23.416623+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:38:23.416624+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 147, in init_app
2020-05-19T19:38:23.416793+00:00 app[web.1]: parsed_uri = uri_parser.parse_uri(uri)
2020-05-19T19:38:23.416793+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/pymongo/uri_parser.py", line 396, in parse_uri
2020-05-19T19:38:23.417050+00:00 app[web.1]: "begin with '%s' or '%s'" % (SCHEME, SRV_SCHEME))
2020-05-19T19:38:23.417051+00:00 app[web.1]: pymongo.errors.InvalidURI: Invalid URI scheme: URI must begin with 'mongodb://' or 'mongodb+srv://'
2020-05-19T19:39:22.153024+00:00 app[api]: Release v19 created by user lutersweg@hotmail.com
2020-05-19T19:39:24.025069+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:39:22.153024+00:00 app[api]: Set MONGO_URI config vars by user lutersweg@hotmail.com
2020-05-19T19:39:29.550903+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:39:29.438093+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:39:29.438109+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:39:29.438246+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:39:29.438248+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:39:29.438420+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:39:29.438420+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 147, in init_app
2020-05-19T19:39:29.438586+00:00 app[web.1]: parsed_uri = uri_parser.parse_uri(uri)
2020-05-19T19:39:29.438588+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/pymongo/uri_parser.py", line 396, in parse_uri
2020-05-19T19:39:29.438831+00:00 app[web.1]: "begin with '%s' or '%s'" % (SCHEME, SRV_SCHEME))
2020-05-19T19:39:29.438849+00:00 app[web.1]: pymongo.errors.InvalidURI: Invalid URI scheme: URI must begin with 'mongodb://' or 'mongodb+srv://'
2020-05-19T19:39:38.865358+00:00 app[api]: Set SECRET_KEY config vars by user lutersweg@hotmail.com
2020-05-19T19:39:38.865358+00:00 app[api]: Release v20 created by user lutersweg@hotmail.com
2020-05-19T19:39:41.006865+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:39:47.022651+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:39:46.932762+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:39:46.932775+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:39:46.932915+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:39:46.932917+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:39:46.933090+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:39:46.933092+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 147, in init_app
2020-05-19T19:39:46.933259+00:00 app[web.1]: parsed_uri = uri_parser.parse_uri(uri)
2020-05-19T19:39:46.933261+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/pymongo/uri_parser.py", line 396, in parse_uri
2020-05-19T19:39:46.933504+00:00 app[web.1]: "begin with '%s' or '%s'" % (SCHEME, SRV_SCHEME))
2020-05-19T19:39:46.933506+00:00 app[web.1]: pymongo.errors.InvalidURI: Invalid URI scheme: URI must begin with 'mongodb://' or 'mongodb+srv://'
2020-05-19T19:41:07.216674+00:00 app[api]: Set MONGO_URI config vars by user lutersweg@hotmail.com
2020-05-19T19:41:07.216674+00:00 app[api]: Release v21 created by user lutersweg@hotmail.com
2020-05-19T19:41:08.734932+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:41:15.696592+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:41:15.551792+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:41:15.551815+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:41:15.552020+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:41:15.552058+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:41:15.552313+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:41:15.552351+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 147, in init_app
2020-05-19T19:41:15.552601+00:00 app[web.1]: parsed_uri = uri_parser.parse_uri(uri)
2020-05-19T19:41:15.552638+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/pymongo/uri_parser.py", line 396, in parse_uri
2020-05-19T19:41:15.553047+00:00 app[web.1]: "begin with '%s' or '%s'" % (SCHEME, SRV_SCHEME))
2020-05-19T19:41:15.553093+00:00 app[web.1]: pymongo.errors.InvalidURI: Invalid URI scheme: URI must begin with 'mongodb://' or 'mongodb+srv://'
2020-05-19T19:41:44.749914+00:00 app[api]: Release v22 created by user lutersweg@hotmail.com
2020-05-19T19:41:44.749914+00:00 app[api]: Set SECRET_KEY config vars by user lutersweg@hotmail.com
2020-05-19T19:41:46.262462+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:41:52.464366+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:41:52.359755+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:41:52.359775+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:41:52.359922+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:41:52.359924+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:41:52.360090+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:41:52.360108+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 147, in init_app
2020-05-19T19:41:52.360268+00:00 app[web.1]: parsed_uri = uri_parser.parse_uri(uri)
2020-05-19T19:41:52.360269+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/pymongo/uri_parser.py", line 396, in parse_uri
2020-05-19T19:41:52.360506+00:00 app[web.1]: "begin with '%s' or '%s'" % (SCHEME, SRV_SCHEME))
2020-05-19T19:41:52.360536+00:00 app[web.1]: pymongo.errors.InvalidURI: Invalid URI scheme: URI must begin with 'mongodb://' or 'mongodb+srv://'
2020-05-19T19:42:41.251241+00:00 app[api]: Set MONGO_URI config vars by user lutersweg@hotmail.com
2020-05-19T19:42:41.251241+00:00 app[api]: Release v23 created by user lutersweg@hotmail.com
2020-05-19T19:42:42.998015+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:42:48.911936+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:42:48.806470+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:42:48.806504+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:42:48.806610+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:42:48.806627+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:42:48.806757+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:42:48.806759+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 147, in init_app
2020-05-19T19:42:48.806897+00:00 app[web.1]: parsed_uri = uri_parser.parse_uri(uri)
2020-05-19T19:42:48.806899+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/pymongo/uri_parser.py", line 390, in parse_uri
2020-05-19T19:42:48.807097+00:00 app[web.1]: raise ConfigurationError('The "dnspython" module must be '
2020-05-19T19:42:48.807114+00:00 app[web.1]: pymongo.errors.ConfigurationError: The "dnspython" module must be installed to use mongodb+srv:// URIs
2020-05-19T19:42:53.336385+00:00 app[api]: Set SECRET_KEY config vars by user lutersweg@hotmail.com
2020-05-19T19:42:53.336385+00:00 app[api]: Release v24 created by user lutersweg@hotmail.com
2020-05-19T19:42:54.415422+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:42:59.223912+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:42:59.144299+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:42:59.144316+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:42:59.144443+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:42:59.144444+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:42:59.144583+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:42:59.144584+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 147, in init_app
2020-05-19T19:42:59.144732+00:00 app[web.1]: parsed_uri = uri_parser.parse_uri(uri)
2020-05-19T19:42:59.144732+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/pymongo/uri_parser.py", line 390, in parse_uri
2020-05-19T19:42:59.144936+00:00 app[web.1]: raise ConfigurationError('The "dnspython" module must be '
2020-05-19T19:42:59.144937+00:00 app[web.1]: pymongo.errors.ConfigurationError: The "dnspython" module must be installed to use mongodb+srv:// URIs
2020-05-19T19:47:18.454453+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:47:26.215718+00:00 heroku[web.1]: State changed from starting to crashed
2020-05-19T19:47:26.094297+00:00 app[web.1]: Traceback (most recent call last):
2020-05-19T19:47:26.094396+00:00 app[web.1]: File "app.py", line 15, in <module>
2020-05-19T19:47:26.094639+00:00 app[web.1]: mongo = PyMongo(app)
2020-05-19T19:47:26.094684+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 110, in __init__
2020-05-19T19:47:26.094899+00:00 app[web.1]: self.init_app(app, uri, *args, **kwargs)
2020-05-19T19:47:26.094925+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask_pymongo/__init__.py", line 147, in init_app
2020-05-19T19:47:26.095141+00:00 app[web.1]: parsed_uri = uri_parser.parse_uri(uri)
2020-05-19T19:47:26.095167+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/pymongo/uri_parser.py", line 390, in parse_uri
2020-05-19T19:47:26.095506+00:00 app[web.1]: raise ConfigurationError('The "dnspython" module must be '
2020-05-19T19:47:26.095542+00:00 app[web.1]: pymongo.errors.ConfigurationError: The "dnspython" module must be installed to use mongodb+srv:// URIs
2020-05-19T19:54:13.000000+00:00 app[api]: Build started by user lutersweg@hotmail.com
2020-05-19T19:54:49.957650+00:00 app[api]: Deploy 0315e029 by user lutersweg@hotmail.com
2020-05-19T19:54:49.957650+00:00 app[api]: Release v25 created by user lutersweg@hotmail.com
2020-05-19T19:54:51.228492+00:00 heroku[web.1]: State changed from crashed to starting
2020-05-19T19:54:57.225153+00:00 heroku[web.1]: State changed from starting to up
2020-05-19T19:54:56.890789+00:00 app[web.1]: * Serving Flask app "app" (lazy loading)
2020-05-19T19:54:56.890805+00:00 app[web.1]: * Environment: production
2020-05-19T19:54:56.890888+00:00 app[web.1]: WARNING: This is a development server. Do not use it in a production deployment.
2020-05-19T19:54:56.890931+00:00 app[web.1]: Use a production WSGI server instead.
2020-05-19T19:54:56.890962+00:00 app[web.1]: * Debug mode: on
2020-05-19T19:54:56.896413+00:00 app[web.1]: * Running on http://0000:34140/ (Press CTRL+C to quit)
2020-05-19T19:54:56.897209+00:00 app[web.1]: * Restarting with stat
2020-05-19T19:54:57.277215+00:00 app[web.1]: * Debugger is active!
2020-05-19T19:54:57.278769+00:00 app[web.1]: * Debugger PIN: 267-283-665
2020-05-19T19:54:58.000000+00:00 app[api]: Build succeeded
2020-05-19T19:56:28.905675+00:00 heroku[router]: at=info method=GET path="/" host=dental-laboratory.herokuapp.com request_id=c103b62f-dae4-432d-ac53-a193e94930d4 fwd="90.202.46.200" dyno=web.1 connect=3ms service=54ms status=200 bytes=3663 protocol=https
2020-05-19T19:56:28.900065+00:00 app[web.1]: 10.9.59.88 - - [19/May/2020 19:56:28] "GET / HTTP/1.1" 200 -
2020-05-19T19:56:29.005616+00:00 app[web.1]: 10.9.59.88 - - [19/May/2020 19:56:29] "GET /static/css/style.css HTTP/1.1" 200 -
2020-05-19T19:56:29.133380+00:00 app[web.1]: 10.9.59.88 - - [19/May/2020 19:56:29] "GET /static/images/imp.jpg HTTP/1.1" 200 -
2020-05-19T19:56:29.146822+00:00 heroku[router]: at=info method=GET path="/static/images/imp.jpg" host=dental-laboratory.herokuapp.com request_id=e43d9ccb-e259-44e0-84d2-e5a970453d9c fwd="90.202.46.200" dyno=web.1 connect=1ms service=12ms status=200 bytes=191243 protocol=https
2020-05-19T19:56:29.012009+00:00 heroku[router]: at=info method=GET path="/static/css/style.css" host=dental-laboratory.herokuapp.com request_id=d9798b52-d394-4b97-a2ba-4fe3b5a2d42a fwd="90.202.46.200" dyno=web.1 connect=1ms service=5ms status=200 bytes=910 protocol=https
2020-05-19T19:56:29.705875+00:00 heroku[router]: at=info method=GET path="/" host=dental-laboratory.herokuapp.com request_id=efdf687d-3c6a-460a-8d84-7f6cbebc4bb9 fwd="3.101.0.4" dyno=web.1 connect=1ms service=5ms status=200 bytes=3663 protocol=http
2020-05-19T19:56:29.700308+00:00 app[web.1]: 10.8.149.25 - - [19/May/2020 19:56:29] "GET / HTTP/1.1" 200 -
2020-05-19T19:56:29.714331+00:00 app[web.1]: 10.9.59.88 - - [19/May/2020 19:56:29] "GET /favicon.ico HTTP/1.1" 404 -
2020-05-19T19:56:29.719925+00:00 heroku[router]: at=info method=GET path="/favicon.ico" host=dental-laboratory.herokuapp.com request_id=cca6b886-44f9-42b3-b9c9-1a249e2a7d14 fwd="90.202.46.200" dyno=web.1 connect=1ms service=3ms status=404 bytes=394 protocol=https
2020-05-19T19:58:01.548709+00:00 heroku[router]: at=info method=GET path="/get_jobs" host=dental-laboratory.herokuapp.com request_id=6500ac6e-eef9-4521-9bdd-0903154e247e fwd="90.202.46.200" dyno=web.1 connect=0ms service=910ms status=200 bytes=6188 protocol=https
2020-05-19T19:58:01.545799+00:00 app[web.1]: 10.38.205.57 - - [19/May/2020 19:58:01] "GET /get_jobs HTTP/1.1" 200 -
2020-05-19T19:58:02.776298+00:00 app[web.1]: 10.12.135.75 - - [19/May/2020 19:58:02] "GET / HTTP/1.1" 200 -
2020-05-19T19:58:02.774473+00:00 heroku[router]: at=info method=GET path="/" host=dental-laboratory.herokuapp.com request_id=32b0b305-1040-4e85-8d96-6d2f61d90c08 fwd="54.207.33.42" dyno=web.1 connect=0ms service=6ms status=200 bytes=3663 protocol=http
2020-05-19T19:58:03.878440+00:00 app[web.1]: 10.38.205.57 - - [19/May/2020 19:58:03] "GET /add_patient HTTP/1.1" 200 -
2020-05-19T19:58:03.879845+00:00 heroku[router]: at=info method=GET path="/add_patient" host=dental-laboratory.herokuapp.com request_id=b88af1ca-0dbf-4eac-8053-a3f03cec2ebb fwd="90.202.46.200" dyno=web.1 connect=0ms service=151ms status=200 bytes=6287 protocol=https
2020-05-19T19:58:06.144571+00:00 heroku[router]: at=info method=GET path="/get_patients" host=dental-laboratory.herokuapp.com request_id=cae7a295-04e8-44b2-af14-b740c3da6781 fwd="90.202.46.200" dyno=web.1 connect=1ms service=80ms status=200 bytes=8616 protocol=https
2020-05-19T19:58:06.137294+00:00 app[web.1]: 10.11.191.99 - - [19/May/2020 19:58:06] "GET /get_patients HTTP/1.1" 200 -
2020-05-19T19:58:09.334766+00:00 app[web.1]: 10.11.191.99 - - [19/May/2020 19:58:09] "GET /login HTTP/1.1" 200 -
2020-05-19T19:58:09.342046+00:00 heroku[router]: at=info method=GET path="/login" host=dental-laboratory.herokuapp.com request_id=f0a04d2f-f40c-4449-97e9-40c7458b2dbb fwd="90.202.46.200" dyno=web.1 connect=0ms service=6ms status=200 bytes=3512 protocol=https
2020-05-19T19:58:32.845803+00:00 app[web.1]: 10.11.191.99 - - [19/May/2020 19:58:32] "POST /login HTTP/1.1" 200 -
2020-05-19T19:58:32.853115+00:00 heroku[router]: at=info method=POST path="/login" host=dental-laboratory.herokuapp.com request_id=f201d9d4-ed46-456a-a479-f32fdb80c86b fwd="90.202.46.200" dyno=web.1 connect=1ms service=6ms status=200 bytes=3643 protocol=https
2020-05-19T19:58:50.021713+00:00 app[web.1]: 10.11.191.99 - - [19/May/2020 19:58:50] "POST /login HTTP/1.1" 302 -
2020-05-19T19:58:50.177857+00:00 app[web.1]: 10.12.40.145 - - [19/May/2020 19:58:50] "GET /get_patients HTTP/1.1" 200 -
2020-05-19T19:58:50.028976+00:00 heroku[router]: at=info method=POST path="/login" host=dental-laboratory.herokuapp.com request_id=56718b72-10c3-4b54-a253-65ea208b53ee fwd="90.202.46.200" dyno=web.1 connect=1ms service=5ms status=302 bytes=694 protocol=https
2020-05-19T19:58:50.338114+00:00 app[web.1]: 10.12.40.145 - - [19/May/2020 19:58:50] "GET /static/css/style.css HTTP/1.1" 200 -
2020-05-19T19:58:50.567191+00:00 app[web.1]: 10.12.40.145 - - [19/May/2020 19:58:50] "GET /static/images/imp.jpg HTTP/1.1" 200 -
2020-05-19T19:58:50.177853+00:00 heroku[router]: at=info method=GET path="/get_patients" host=dental-laboratory.herokuapp.com request_id=f91a00f7-ffc4-4b62-9a98-8257c95a6f7b fwd="90.202.46.200" dyno=web.1 connect=0ms service=76ms status=200 bytes=8856 protocol=http
2020-05-19T19:58:50.338347+00:00 heroku[router]: at=info method=GET path="/static/css/style.css" host=dental-laboratory.herokuapp.com request_id=3e7e9e55-9da8-47df-8789-73ce9cf434ad fwd="90.202.46.200" dyno=web.1 connect=1ms service=4ms status=200 bytes=910 protocol=http
2020-05-19T19:58:50.573573+00:00 heroku[router]: at=info method=GET path="/static/images/imp.jpg" host=dental-laboratory.herokuapp.com request_id=21631124-ddca-4194-92e9-c436cbf6175b fwd="90.202.46.200" dyno=web.1 connect=0ms service=9ms status=200 bytes=191243 protocol=http
2020-05-19T19:58:50.940134+00:00 app[web.1]: 10.35.67.69 - - [19/May/2020 19:58:50] "GET /get_patients HTTP/1.1" 200 -
2020-05-19T19:58:50.941062+00:00 heroku[router]: at=info method=GET path="/get_patients" host=dental-laboratory.herokuapp.com request_id=00d8b126-e0c6-4b9f-a592-59350571fd22 fwd="54.207.33.42" dyno=web.1 connect=1ms service=73ms status=200 bytes=8616 protocol=http
2020-05-19T19:58:51.395657+00:00 app[web.1]: 10.12.40.145 - - [19/May/2020 19:58:51] "GET /favicon.ico HTTP/1.1" 404 -
2020-05-19T19:58:51.395648+00:00 heroku[router]: at=info method=GET path="/favicon.ico" host=dental-laboratory.herokuapp.com request_id=728aa6c4-9201-40eb-b2ed-2288953a174f fwd="90.202.46.200" dyno=web.1 connect=1ms service=4ms status=404 bytes=394 protocol=http
2020-05-19T19:58:59.503286+00:00 app[web.1]: 10.34.81.118 - - [19/May/2020 19:58:59] "GET / HTTP/1.1" 200 -
2020-05-19T19:58:59.506397+00:00 heroku[router]: at=info method=GET path="/" host=dental-laboratory.herokuapp.com request_id=0bc38dbf-33e8-40a5-bc11-7a86ad4e246f fwd="54.207.33.42" dyno=web.1 connect=0ms service=5ms status=200 bytes=3663 protocol=http
2020-05-19T19:59:00.453241+00:00 app[web.1]: 10.12.40.145 - - [19/May/2020 19:59:00] "GET /get_type HTTP/1.1" 200 -
2020-05-19T19:59:00.453523+00:00 heroku[router]: at=info method=GET path="/get_type" host=dental-laboratory.herokuapp.com request_id=9f3644f7-c113-44d3-a890-0c64081fe13a fwd="90.202.46.200" dyno=web.1 connect=0ms service=79ms status=200 bytes=5763 protocol=http

# Deployment

There is a live version deployed in Heroku. https://git.heroku.com/dental-laboratory.git

# Credits

Code used and modified from:

* i.	Python Flask Tutorial - https://www.youtube.com/watch?v=UIJKdCIEXUQ

* ii.	Mini Project Tutorial – Datacentric Module

# Media

The background image was obtained from free detal laboratory images at https://www.bing.com/images/search?q=dental+laboratory+free+images&qpvt=dental+laboratory+free+images&FORM=IGRE

# Acknowledgements

The layout of the database was inspired by the Mini Project Tutorial. Thanks to my mentor for the valuable advice and suggestions. 
