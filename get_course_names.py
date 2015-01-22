import json
import lxml
from lxml import html
import requests
import re

#code to pull down a list of course names

courses_json = '''{"name": "Bolton University Courses","size": 20,"children": ['''
for num in range(1000, 9999):
	url = 'http://courses.bolton.ac.uk/Details/Index/' + str(num)
	#get the html page at url
        page = requests.get(url)
        #parse the html into a tree
	tree = lxml.html.fromstring(page.text)
        #extract the relevant data, adding it to the Module object
        #module id
        self.id = module_id
        titles = tree.xpath('//title/text()')
        title = titles[0]
        if title.find("Search For a Course") == -1:
		print (url + "is not a course URL")
	else:
        	courses_json += '''{"name":"''' + title + '''","size": 20},'''
        	courses_json += ''']},'''
        	print("Get module " + title)
#remove the last comma
courses_json = courses_json[:-1]

#close the json string
courses_json += "]}"

#remove invalid chars
out = ''.join([x for x in courses_json if ord(x) < 128])
out = out.rstrip('\r\n')
out = re.sub( '\s+', ' ', out ).strip()

#print the json string
print(courses_json)

#write the json to a file
with open('university_courses.json', 'w') as file_:
    file_.write(out)
