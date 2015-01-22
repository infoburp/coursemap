import json
import lxml
from lxml import html
import requests
import re

number = 1
#make root node
nodes='''{"nodes":[{"name":"Bolton University","group":1},'''
links='"links":['
#make node for each subject, linked to root node
#make node for each level, linked to subject node
#make node for each course, linked to level node
subjects = [68,42,46,40,79,43,50,80,45,59,44,53,54,66,49,58,57,47,77,48,67,39,75,76]
subject_names = ["Foundation","Art","Biology","Business and Law","Chemistry","Civil Engineering","Early Years","Media","Design Technology","Distance Learning","Engineering","Computing","Health","Materials Research","Mathematics","Off Campus Overseas ","Off Campus UK","Psychology","Renewable Energy","Sport","Education","English","Top-up","University-wide"]
subject_number = 1
for subject in subjects:
	nodes += '''{"name":"''' + subject_names[subject_number-1] + '''","group":2},'''
	links += '''{"source":''' + str(subject_number) + ''',"target":0,"value":1},'''
	levels = [15,16,17,19,18,20]
	level_names = ["Undergraduate","Postgraduate","Further Education","Professional Development (Undergraduate Level)","Professional Development (Postgraduate Level)","Professional Development (Further Education Level)"]
	level_number = 1
	for level in levels:
		nodes += '''{"name":"''' + level_names[level_number-1] + '''","group":4},'''
		links += '''{"source":''' + str(level_number + len(subjects)) + ''',"target":'''+ str(subject_number) +''',"value":1},'''
		attendances=[13,14,15]
		course_number = 1
		for attendance in attendances:
			payload = {'SubjectAreaID': subject, 'StudyLevelID': level, 'AttendenceID': attendance}
			r = requests.post("http://courses.bolton.ac.uk/", data=payload)
			print("Getting (" + str(subject) + "," + str(level) + "," + str(attendance) + ")" + " " + str(number) + " of " + str(len(subjects) * (len(levels) * len(attendances))))
			tree = lxml.html.fromstring(r.text)
		        paragraphs = tree.xpath('//a/text()')
			#81>a.length
			for x in range(81,len(paragraphs)-8):
				nodes+='''{"nodes":[{"name":"''' + paragraphs[x] + '''","group":5},'''
				links += '''{"source":''' + str(level_number + len(subjects)) + ''',"target":'''+ str(len(levels) + len(subjects) + course_number) +''',"value":1},'''
				number += 1
			course_number += 1
		level_number += 1
	subject_number += 1
#remove the last commas
nodes = nodes[:-1]
links = links[:-1]

json_string = nodes + '],' + links + ']}'
#remove invalid chars
out = ''.join([x for x in json_string if ord(x) < 128])
out = out.rstrip('\r\n')
out = re.sub( '\s+', ' ', out ).strip()

#print the json string
print(out)

#write the json to a file
with open('graph.json', 'w') as file_:
    file_.write(out)