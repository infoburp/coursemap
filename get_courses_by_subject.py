import json
import lxml
from lxml import html
import requests
import re

json_string='''{"name": "Subjects","size":20,"children":['''
#loop for subjects
subjects = [68,42,46,40,79,43,50,80,45,59,44,53,54,66,49,58,57,47,77,48,67,39,75,76]
subject_names = ["Foundation","Art","Biology","Business and Law","Chemistry","Civil Engineering","Early Years","Media","Design Technology","Distance Learning","Engineering","Computing","Health","Materials Research","Mathematics","Off Campus Overseas ","Off Campus UK","Psychology","Renewable Energy","Sport","Education","English","Top-up","University-wide"]
subject_index = 0
for subject in subjects:
	json_string+='''{"name":''' + subject_names[subject_index] + ''',"size":20,"children":['''
	subject_index += 1
	#loop for levels
	json_string+='''{"name": "Study levels","size":20,"children":['''
	levels = [15,16,17,19,18,20]
	level_names = ["Undergraduate","Postgraduate","Further Education","Professional Development (Undergraduate Level)","Professional Development (Postgraduate Level)","Professional Development (Further Education Level)"]
	level_index = 0
	for level in levels:
		json_string+='''{"name":''' + level_names[level_index] + ''',"size":20,"children":['''
		level_index += 1
		#loop for attendance types
		attendances=[13,14,15]
		for attendance in attendances:
			payload = {'SubjectAreaID': subject, 'StudyLevelID': level, 'AttendenceID': attendance}
			r = requests.post("http://courses.bolton.ac.uk/", data=payload)
			print("Getting (" + subject + "," + level + "," + attendance + ")")
			tree = lxml.html.fromstring(r.text)
		        paragraphs = tree.xpath('//a/text()')
			#81>a.length
			for x in range(81,len(paragraphs)):
				json_string+='''{"name": "''' + paragraphs[x] + '''","size":20}'''
json_string+="]}]}]}]}"
