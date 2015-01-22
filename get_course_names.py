import json
import lxml
from lxml import html
import requests
import re
import timeit

start = timeit.default_timer()
print("Starting scrape at:" + str(start))

#code to pull down a list of course names
total_scrape_time = 0
courses_json = '''{"name": "Bolton University Courses","size": 20,"children": ['''
for num in range(1, 1000):
	course_start = timeit.default_timer()
	url = 'http://courses.bolton.ac.uk/Details/Index/' + str(num+1000)
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
        	scrape_time = timeit.default_timer() - course_start
		print("Course scrape took " + str(timeit.default_timer() - course_start) + " (" + str(num) + "/1000)")
#remove the last comma
out_json = courses_json[:-1]

#close the json string
out_json += "]}"

#remove invalid chars
out = ''.join([x for x in out_json if ord(x) < 128])
out = out.rstrip('\r\n')
out = re.sub( '\s+', ' ', out ).strip()

#print the json string
print(out)

print("Saving to university_courses.json")

#write the json to a file
with open('university_courses.json', 'w') as file_:
    file_.write(out)

stop = timeit.default_timer()
print("Scrape finishes at: " + str(stop))
print("Scrape started at: " + str(start))

print("Total scrape time: " + str(stop-start))
