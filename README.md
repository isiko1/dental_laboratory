# Dental Laboratory – Database <br>
Inspired from my time working in the dental profession when dental laboratory work was recorded in a paper book. I doubt this 
practice is still in use with the technology available today. To assist companies that may have not moved form the practice of paper records in chosng an IT system for their needs, I have chosen to produce a dental laboratory database for my project. <br>
# UX <br>
A basic design to capture all the information that generally accompanies a dental laboratory prescription, it also allows the user to make modifications to contents of the database as necessary. Designed with simplicity for the user in mind, on opening the database the user arrives on the home page and this is also the sign in page. At the base of the sign in 
is the option for a new user to register or if the user wishes to, can click on Register on the navigation bar at the top of the page. <br>
## User Story <br>
The main objective of this milestone project is CRUD and this requirement aligns very well with the function of the
dental laboratory recording system whether it is in paper form or digital.<br>
As a user Type| I want to perform an action |So that I can achieve a goal|Type of Action|
--------------|----------------------------|----------------------------|---------------|
Dental Technician| View and Navigate | See outstanding patient Jobs| Read |
Dental Technician| View and Navigate | See all Patients and Jobs| Read |
Any User | View and Navigate | See outstanding patient Jobs | Read |
Dental Technician | Add new patients | Maintain a record of new jobs | Create|
Dental Technician | Add new patients | Maintain a record of new jobs | Create|
Any User | Add new Jobs and Patient Type| Maintain accurate Job specifications and Patient types |Create|
Dental Technician| Add new Jobs and Patient Type| Maintain accurate Job specifications and Patient types |Create|
Dental Technician|Edit Database contents| Maintain accurate data| Update|
All Users|Edit Database contents| Maintain accurate data| Update|
Dental Technician|Delete Database contents| Compliance with data protection laws and ability for data cleansing| Delete|
All Users|Delete Database contents| Compliance with data protection laws and ability for data cleansing| Delete|
___
# Features <br>
## Home Page <br>
*Home*<br>
*Patients*<br>
*New Patients*<br>
*Manage Jobs*<br>
*Manage Type*<br>
*Log Out*<br>
*Sign In*<br>
*Register*<br>
## Home<br>
* On opening the database the user is immediately directed to the homepage that requires the user to sign in. If the user is not registered, there is the option to register at the bottom of the sign in form. Alternatively, the user can click on the Register option at the top right of the navigation bar or the top right below the database name.
Unfortunately, at this stage any user can bypass the sign in and go directly into the features. Sign in functionality requires further improvement and is mentioned in the features left to be implemented section of this README.
However, the sign in form is functional and is built in to provide an insight of the intended security build required to gain access to the database. <br>
## Patients <br>
* On successful sign in, the user is directed to the Patients page which displays all the patients currently in the database. The heading is "Current Patients" and directly below this is the list showing the patients full names followed by their dates of birth. To the left are dropdown arrows, when selected will display the dental job required and the date it should be completed by. Next to the dropdown arrows are the edit buttons, when selected will display all the selected patient's details for editing as required. The completion button when selected will delete the patient and all their details from the database. <br>
## New Patients <br>
* Select this option when creating a new patient, the user will be directed to the Add patient form where they are required to enter the full name of the patient and their details. The form will not be submitted without a full name being entered and there are various prompts to help the user as they complete the form. <br>
## Manage Jobs <br>
* Select this option to view all the dental appliances(job names) available in the database. On arriving at the page the user is presented with the list of jobs and can edit, delete or add Job names to the database by selecting the appropriate buttons accordingly. <br>
## Manage types <br>
* Select this option to view all the patient types available in the database. On arriving at the page the user is presented with the list of patient types and can edit, delete or add patient types to the database by selecting the appropriate buttons accordingly. <br>
## Log Out <br>
* When selected the user will be redirected to the home page which should display the Sign In form and will receive confirmation they have logged out. <br>
## Register <br>
* Selecting this option the user will be presented with a registration form just like the Sign in form, if the user is already registered there is the option at the bottom of the form to Sign in. <br>
# Features Left to Implement <br>
The database has scope for a wide range of functionality firstly, great potential as a cloud based b2b application linked directly to the dental practices. <br>
*Future additions:* <br>
* i.	Billing and address information <br>
* ii.	Dental appliance design page with a link to a virtual description and assisted designing of the appliance <br>
* iii.	Virtual assistant Live chat functionality <br>
* iv.	Alert function for overdue or jobs close to the appointment date <br>
* v.	Timeout after a period of inactivity and also implement user seesion cookies <br>
* vi.	Social Media and Contact Links<br>
* vii.	Log out and Sign functionality require further development<br>
* viii.	Registered Dental Practices Allocated database – (The dental practice would be identified by a unique number allocated during registration and when the unique number is entered the database would open displaying only patients from that particular practice.) <br>
* ix.	Add archive storage function for patients and all jobs completed <br>
*  x.   Further error handling and defensive coding around to catch errors and to avoid maliciuos inserts that would crash the application
*  xi.  Password reset link and email notification

# Technologies used

* HTML - Used for page content
* CSS - Used for styling and visual effect
* Javascript - Used for automation for the functions built in the forms
* Python and Flask - For simplicity 
* MongoDB - Used for Storage and extraction of data.
* JQuery - For the DOM manipulation and handlig events
* Materialize - Used for design and layout

# Testing

At each stage of a new function and template the code was tested running through the browser to check for errors. The errors were picked up in jinja and werkzeug and also in the terminal window. Any errors were then corrected before running the code again through the browser. 
Various background features and colours were tested as well as styling using the browser and the inspect window. On right clicking and selecting inspect, one can choose the various platform views i.e iphone 6, Ipad or Desktop etc.
Responsive testing for mobile view was carried out using the inspect window.
There were quite a few errors when trying to deploy to heroku and these were corrected as they were highlighted resulting in several commits titled "Modified". Please see a snippet of the heroku error below.
* SyntaxError: EOL while scanning string literal
gitpod /workspace/dental_laboratory $ heroku ps:scale web=1
 ›   Warning: heroku update available from 7.39.5 to 7.41.1.
Scaling dynos... done, now running web at 1:Free
gitpod /workspace/dental_laboratory $ heroku logs --tail
 ›   Warning: heroku update available from 7.39.5 to 7.41.1.

During the testing the binding of the edit type routing there were a few 405, 302, 403 errors and i had to refer to wikepedia in order to address these.<br>
After going through each code in the edittype html, base.html and app.py to no avail I created a clone database [git.hub](https://github.com/isiko1/dental_laboratory2) to copy the original coding onto so that it could be retrieved once the error had been identified. <br>
HTML was checked using [W3C] (https://validator.w3.org/) the URI checker was a new feature i used to see if it could identify the connection issues as well as using direct input for the .html pages.
In the end the errors were manually identified and corrected through patience, determination and persistence by going through and changing various codes and pushing to github as each error was resolved. <br>
# Deployment <br>
There is a live version deployed in Heroku. [heroku](https://dental-laboratory.herokuapp.com/) <br>
# Credits <br>
Some of the code used in this project was adapted and modified from: <br>
* i.	Python Flask Tutorial - [youtube](https://www.youtube.com/watch?v=UIJKdCIEXUQ) <br>
* ii.	Mini Project Tutorial – Code Institute Datacentric Module <br>
# Media <br>
The background image was obtained from free detal laboratory images at [bing](https://www.bing.com/images/search?q=dental+laboratory+free+images&qpvt=dental+laboratory+free+images&FORM=IGRE) <br>
# Acknowledgements<br>
The layout of the database was inspired by the Mini Project Tutorial. Thanks to my mentor for the valuable advice and suggestions. 
The user story lay-out was adapted from my later "Hangout"