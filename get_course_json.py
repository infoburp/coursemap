import json
from lxml import html
import requests

class Module:
    #module id
    str id
    #form url for module html page
    url = "https://modules.bolton.ac.uk/" + id
    #get module html page
    page = requests.get(module)
    tree = html.fromstring(page.text)
    #module code
    str code;
    #module year
    str year;
    #module title
    str title;
    #Credits
    str credits;
    #Level
    str level;
    #Type
    str type;
    #Duration
    str duration;
    #Trimester 3?
    str trim3;
    #ECTS
    str ects;
    #Marking Scheme
    str marking;
    #Pass Mark
    str pass_mark;
    #Delivery Type
    str delivery_type;
    #Pre-Requisites
    str pre_requisites;
    #Co-Requisites
    str co_requisites;
    #Barred Combinations
    str barred_combinations;
    #Module Outline
    str outline;
    #Indicative Content
    str indicative_content;
    #Learning Outcomes
    str learning_outcomes;
    #Learning And Teaching Strategy
    str learning_and_teaching_strategy;
    #Learning & Teaching Methods
    str learning_and_teaching_methods;
    #Formative Assessment Strategy
    str formative_assessment_strategy;
    #Summative Assessment Strategy
    str summative_assessment_strategy;
    #Summative Assessments
    str summative_assessments;
    #Learning Resources
    str learning_resources;
    #Feedback to Students
    str student_feedback;

def module_get(module_id):
    #download the data for this module and insert it into the relevant fields, returning a Module object
    #create the Module object ready for population
    Module module
    #calculate the module detail url
    url = "https://modules.bolton.ac.uk/" + module_id
    #get the html page at url
    page = requests.get(url)
    #parse the html into a tree
    tree = html.fromstring(page.text)
    #extract the relevant data, adding it to the Module object
    #module id
    module.id = module_id
    #form url for module html page
    module.url = url
    #get module html page
    page = requests.get(module)
    tree = html.fromstring(page.text)
    #module code
    module.code;
    #module year
    module.year;
    #module title
    module.title;
    #Credits
    module.credits;
    #Level
    module.level;
    #Type
    module.type;
    #Duration
    module.duration;
    #Trimester 3?
    module.trim3;
    #ECTS
    module.ects;
    #Marking Scheme
    module.marking;
    #Pass Mark
    module.pass_mark;
    #Delivery Type
    module.delivery_type;
    #Pre-Requisites
    module.pre_requisites;
    #Co-Requisites
    module.co_requisites;
    #Barred Combinations
    module.barred_combinations;
    #Module Outline
    module.outline;
    #Indicative Content
    module.indicative_content;
    #Learning Outcomes
    module.learning_outcomes;
    #Learning And Teaching Strategy
    module.learning_and_teaching_strategy;
    #Learning & Teaching Methods
    module.learning_and_teaching_methods;
    #Formative Assessment Strategy
    module.formative_assessment_strategy;
    #Summative Assessment Strategy
    module.summative_assessment_strategy;
    #Summative Assessments
    module.summative_assessments;
    #Learning Resources
    module.learning_resources;
    #Feedback to Students
    module.student_feedback;
    #return the Module object
    return module

def parseJson(module):
    #translate the module data into a json string portion

#course title
str course_title = "Computing & Website Development HND/BSc (Hons)"

#array of modules in course
modules=
[
"CPU4000",
"CPU4003",
"CPU4005",
"CPU4001",
"CPU4002",
"CPU4004",
"CPU5001",
"CPU5002",
"CPU5003",
"CPU5000",
"CPU5004",
"CPU5005",
"CPU6000",
"CPU6001",
"CPU6002",
"CPU6004",
"CPU6003",
"CPU6005"]

#stitch together json modules under a root "course name" node
str json_string =
'{"name":' + course title + '","children":['

#add a json string for each module in this course
for module_code in module_codes:
  Module module = module_get(module_code)
  json_string += parse_json(module)

#close the json string
json_string += "]}"

#print the json string
print(json_string)
