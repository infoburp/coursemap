coursemap
=========

A map of the Computing & Website Development HND/BSc (Hons) course at Bolton University.
The code is general enough that it should work for other courses at Bolton,
but you'll have to put a list of the modules of your course into the modules array
in get_course_json.py. Then, running python get_course_json.py should print your json.
Paste this over sampledata.json.

If I can somehow get hold of a list of modules by course for all of the courses
at Bolton, I could improve this a lot, but I cannot currently find such a list...

prerequisites
=============
This code needs python, pip, lxml and requests. You can probably install these with this command:

sudo apt-get install python && sudo apt-get install pip && sudo pip install lxml && sudo pip install requests

Then edit get_course_json.py to include the modules you want to load in the modules array and run:

python get_course_json.py

The program should print json to the screen as described above.
