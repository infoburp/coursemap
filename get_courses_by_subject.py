import json
import lxml
from lxml import html
import requests
import re

json_string='''{"name": "Subjects","size":20,"children":['''
#loop for subjects
subjects = [68,42,46,40,79,43,50,80,45,59,44,53,54,66,49,58,57,47,77,48,67,39,75,76]
subject_names = [80]
subject_names[68] = "Foundation"
subject_names[42] = "Art"
subject_names[46] = "Biology"
subject_names[40] = "Business and Law"
subject_names[79] = "Chemistry"
subject_names[43] = "Civil Engineering"
subject_names[50] = "Early Years"
subject_names[80] = "Media"
subject_names[45] = "Design Technology"
subject_names[59] = "Distance Learning"
subject_names[44] = "Engineering"
subject_names[53] = "Computing"
subject_names[54] = "Health"
subject_names[66] = "Materials Research"
subject_names[49] = "Mathematics"
subject_names[58] = "Off Campus Overseas"
subject_names[57] = "Off Campus UK"
subject_names[47] = "Psychology"
subject_names[77] = "Renewable Energy"
subject_names[48] = "Sport"
subject_names[67] = "Education"
subject_names[39] = "English"
subject_names[75] = "Top-up"
subject_names[76] = "University-wide"
for subject in subjects:
	json_string+='''{"name":''' + subject_names[subject] + ''',"size":20,"children":['''
	#loop for levels
	json_string+='''{"name": "Study levels","size":20,"children":['''
	levels = [15,16,17,19,18,20]
	level_names=[20]
	level_names[15] = "Undergraduate"
	level_names[16] = "Postgraduate"
	level_names[17] = "Further Education"
	level_names[19] = "Professional Development (Undergraduate Level)"
	level_names[18] = "Professional Development (Postgraduate Level)"
	level_names[20] = "Professional Development (Further Education Level)"
	for level in levels:
		json_string+='''{"name": level_names[level],"size":20,"children":['''
		#loop for attendance types
		attendances=[13,14,15]
		for attendance in attendances:
			payload = {'SubjectAreaID': subject, 'StudyLevelID': level, 'AttendenceID': attendance}
			r = requests.post("http://courses.bolton.ac.uk/", data=payload)
			print(r.text)
json_string+="]}]}]}]}"
