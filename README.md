# Dental Laboratory – Database
Inspired from my time working in the dental profession, I chose to produce a dental laboratory database that records dental appliances produced in the dental laboratory.  
# UX
A recording system of work produced and despatched from a dental laboratory. The user logs on using a username and password to access the database. The sign in page has password authentication. Once logged in the user Is taken to home page which has a list of patients.
# Features
# Home
The display format function buttons, patient name and date of birth
Dropdown display is appointment date, (due date) for the appliance to be fitted and the name of the appliance.
The appliances are requested from the dentist and on arrival of the request the patient is added to the database using the New patient tab. When the Job is returned and fitted on the appointment date then the patient is deleted when selecting the Done button. Any amendments can also be made by selecting the edit button.
# Jobs
The requested appliance is a job for the dental technician and on the new patient form, there is a dropdown list of various jobs that are ubiquitously requested. When designing the database allowance has been made for jobs that are not commonly requested and these can be added to the database using the add job function by selecting the Manage Jobs in the navbar.
# Manage Jobs
The display format function buttons and name of the appliance and at the base of the form is the add job button.
# Type
In the dental profession there are patient types to determine the cost of treatment that can be afforded. The most common patient types are NHS or Private.  There is a limit charge which is set by the government that can be afforded to an NHS patient irrespective of the treatment supplied.  There are also no charges for certain treatment for children and under eighteens who are still in full time education.  Just as the requested jobs, an allowance has been made for any patient types that may have been overlooked in the design or that may appear later on and these can be added to the database using the add type function by selecting Manage Types in the navbar.
# Manage Type
The display format function buttons and patient type and at the base of the form is the add type button.
# Features Left to Implement
The database has scope for a wide range of functionality firstly great potential as a cloud based b2b application linked directly to the dental practices.  Future additions:
i.	Registration form
ii.	Billing and address information
iii.	Dental appliance design page with a link to a virtual description and assisted designing of the appliance
iv.	Virtual assistant Live chat functionality
v.	Alert function for overdue or jobs close to the appointment date
vi.	Timeout after a period of inactivity
vii.	Social Media and Contact Links
viii.	Log out functionality
ix.	Registered Dental Practices Allocated database – (The dental practice would be identified by a unique number allocated during registration and when the unique number is entered the database would open displaying only patients from that particular practice.)
x.	Add archive storage function for patients and all jobs completed

# Technologies used
HTML, CSS, Javascript, Python and Flask, MongoDB, JQuery, Materialize
# Testing
At each stage of a new function and template the code was tested running through the browser to check for errors. The errors were picked up in jinja and werkzeug and also in the terminal window. Any errors were then corrected before running the code again through the browser. 
Various background features and colours were tested as well as styling using the browser and the inspect window. On right clicking and selecting inspect, one can choose the various platform views i.e iphone 6, Ipad or Desktop etc.
Responsive testing for mobile view was carried out using the inspect window.
# Deployment
There a live version deployed in Heroku.
# Credits
Code used and modified from:
i.	Python Flask Tutorial - https://www.youtube.com/watch?v=UIJKdCIEXUQ
ii.	Mini Project Tutorial – Datacentric Module
# Acknowledgements
The layout of the database was inspired by the Mini Project Tutorial. Thanks to my mentor code institute for the valuable advice and suggestions. 
