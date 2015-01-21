import json
from lxml import html
import requests

class Module:
    #module id
    str id
    #form url for module html page
    str url = "https://modules.bolton.ac.uk/" + id
    #module title
    str title
    #Credits
    str credits
    #Level
    str level
    #Type
    str type
    #Duration
    str duration
    #Trimester 3?
    str trim3
    #ECTS
    str ects
    #Marking Scheme
    str marking
    #Pass Mark
    str pass_mark
    #Delivery Type
    str delivery_type
    #Pre-Requisites
    str pre_requisites
    #Co-Requisites
    str co_requisites
    #Barred Combinations
    str barred_combinations
    #Module Outline
    str outline
    #Indicative Content
    str indicative_content
    #Learning Outcomes
    str learning_outcomes
    #Learning And Teaching Strategy
    str learning_and_teaching_strategy
    #Learning & Teaching Methods
    str learning_and_teaching_methods
    #Formative Assessment Strategy
    str formative_assessment_strategy
    #Summative Assessment Strategy
    str summative_assessment_strategy
    #Summative Assessments
    str summative_assessments
    #Learning Resources
    str learning_resources
    #Feedback to Students
    str student_feedback

def module_get(module_id):
    #download the data for this module and insert it into the relevant fields, returning a Module object
    #create the Module object ready for population
    Module module
    #calculate the module detail url
    str url = "https://modules.bolton.ac.uk/" + module_id
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
    paragraphs = tree.xpath('//p/text()')
    header4s = tree.xpath('//h4/text()')
    dds = tree.xpath('//dd/text()')
    tables = tree.xpath('//table/text()')
    #module title
    module.title = header4s[0]
    #Credits
    module.credits = dds[0]
    #Level
    module.level = dds[1]
    #Type
    module.type = dds[2]
    #Duration
    module.duration = dds[3]
    #Trimester 3?
    module.trim3 = dds[4]
    #ECTS
    module.ects = dds[5]
    #Marking Scheme
    module.marking = dds[6]
    #Pass Mark
    module.pass_mark = paragraphs[0]
    #Delivery Type
    module.delivery_type = paragraphs[1]
    #Pre-Requisites
    module.pre_requisites = paragraphs[2]
    #Co-Requisites
    module.co_requisites = paragraphs[3]
    #Barred Combinations
    module.barred_combinations = paragraphs[4]
    #Module Outline
    module.outline = paragraphs[5] + "  " + paragraphs[6]
    #Indicative Content
    module.indicative_content = tables[0]
    #Learning Outcomes
    module.learning_outcomes = tables[1]
    #Learning And Teaching Strategy
    module.learning_and_teaching_strategy = paragraphs[7]
    #Learning & Teaching Methods
    module.learning_and_teaching_methods = tables[2]
    #Formative Assessment Strategy
    module.formative_assessment_strategy = paragraphs[8]
    #Summative Assessment Strategy
    module.summative_assessment_strategy = paragraphs[9]
    #Summative Assessments
    module.summative_assessments = tables[3]
    #Learning Resources
    module.learning_resources = tables[4]
    #Feedback to Students
    module.student_feedback = paragraphs[10]
    #return the Module object
    return module

def parseJson(module):
    #translate the module data into a json string portion
    str module_json
    module_json += '{"name": "' + module.id + '","size": 20,"children": ['
    module_json += '{"name":"' + module.title + '","size": 20},'
    module_json += '{"name": "details:","size": 20,"children": ['
    module_json += '{"name": "Credits: ' + module.credits + '","size": ' + module.credits},
    module_json += '{"name": "Level: ' + module.level + '","size": 20},
    module_json += '{"name": "Type: ' + module.type + '","size": 20},
    module_json += '{"name": "Duration: ' + module.duration + '","size": ' + (module.duration * 10) + '},'
    module_json += '{"name": "Trimester 3?: ' + module.trim3 + '","size": 20},
    module_json += '{"name": "ECTS: ' + module.ects + '","size": 20},
    module_json += '{"name": "Marking Scheme: ' + module.marking + '","size": 100},
    module_json += '{"name": "Pass Mark: ' + module.pass_mark + '","size": 40}
    module_json += ']},'
    module_json += '{"name": "Delivery Type","size": 20,"children": ['
    module_json += '{"name": "' + module.delivery_type + '","size": 20}]},'
    module_json += '{"name": "Pre-Requisites","size": 20,"children": ['
    module_json += '{"name": "' + module.pre_requisites + '","size": 20}'
    module_json += ']},'
    module_json += '{"name": "Co-Requisites","size": 20,"children": ['
    module_json += '{"name": "' + module.co_requisites + '","size": 20}
    module_json += ']},'
    module_json += '{"name": "Barred Combinations","size": 20,"children": ['
    module_json += '{"name": "' + module.barred_combinations + '","size": 20}'
    module_json += ']},'
    module_json += '{"name": "Module Outline","size": 20,"children": ['
    module_json += '{"name": "'+ module.outline + '","size": 20}
    module_json += ']},'
    module_json += '{"name": "Indicative Content","size": 20,"children": ['
    #loop to insert all indicative content items
    idicatives = module.indicative_content.xpath('//td/text()')
    #only insert tds that are text, not just a number
    for inicative in indicatives:
        if indicative #is not just a number:
            module_json += '{"name": "' + indicative + '","size": 20},'
            module_json += ']},'
            #remove trailing comma on last indicative
            
    module_json += '{"name": "Learning Outcomes","size": 20,"children": ['
    #loop to insert all learning outcome items
                            #{
                            #    "name": "display knowledge and understanding of Internet structure, applications and services.",
                            #    "size": 20
                            #},
    module_json += ']},'
    module_json += '{"name": "Learning And Teaching Strategy","size": 20,"children": ['
    module_json += '{"name": "A blended learning approach is used in the module which means that you will attend sessions face-to-face and also use online learning. You will attend lectures, seminars and tutorials so that you learn the theoretical content and also have demonstrations and practical hands-on sessions so that you can develop and practice the skills needed to devise your own website. There will also be online sources and activities so that you can explore topics of interest and have online discussions with peers and your tutor. You will also use the internet-based applications to conduct advanced searches. You will also use the internet to find appropriate websites to evaluate prior to creating your own website.",
                                "size": 20},
    module_json += '{"name": "Learning & Teaching Methods","size": 20,"children": ['
    module_json += '{"name": "Hours","size": 20,"children": ['
                                            {
                                                "name": "67.5 scheduled",
                                                "size": 67.5
                                            },
                                            {
                                                "name": "132.5 independant",
                                                "size": 132.5
                                            }
    module_json += ']},'
    module_json += '{"name": "Formative Assessment Strategy","size": 20,"children": ['
    module_json += '{"name": "' + module.formative_assessment_strategy + '","size": 20}'
    module_json += ']},'
    module_json += '{"name": "Summative Assessment Strategy","size": 20,"children": ['
    module_json += '{"name": "' + module.summative_assessment_strategy + '","size": 20}'
    module_json += ']},'
    module_json += '{"name": "Summative Assessments","size": 20,"children": ['
                        #loop to add all summative assessment items
                            #{
                            #    "name": "Case study report (50%)",
                            #    "size": 50
                            #},

    module_json += ']},'
    module_json += '{"name": "Learning Resources","size": 20,"children": ['
                                #loop to add all learning resources
                                    #{
                                    #    "name": "Krug S (2005) Don't Make Me Think!: A Common Sense Approach to Web Usability. 2nd ed. New Riders.",
                                    #    "size": 20
                                    #},

    module_json += ']},'
    module_json += '{"name": "Feedback to Students","size": 20,"children": ['
    module_json += '{"name": "' + module.student_feedback + '","size": 20}'
    module_json += ']}]}]}'
    return module_json

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
