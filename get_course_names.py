import json
import lxml
from lxml import html
import requests
import re

#code to pull down a list of course names

courses_json = '''{"name": "Bolton University Courses","size": 20,"children": ['''
for num in range(0, 99999):
	url = 'http://courses.bolton.ac.uk/Details/Index/' + str(num)
	#get the html page at url
        page = requests.get(url)
        #parse the html into a tree
	tree = lxml.html.fromstring(page.text)
        titles = tree.xpath('//title/text()')
        title = titles[0]
        if title.find("Search For a Course") == -1:
		courses_json += '''{"name":"''' + title + '''","size": 20},'''
        	courses_json += ''']},'''
        	print(title)
	else:
        	print (url + "is not a course URL")
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
