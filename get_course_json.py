import json
from lxml import html
import requests

class Module:
    #module id
    str id
    #form url for module html page
    str url = "https://modules.bolton.ac.uk/" + id
    #module code
    str code
    #module year
    str year
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
    #module code
    module.code =
    #module year
    module.year =
    #module title
    module.title =
    #Credits
    module.credits =
    #Level
    module.level =
    #Type
    module.type =
    #Duration
    module.duration =
    #Trimester 3?
    module.trim3 =
    #ECTS
    module.ects =
    #Marking Scheme
    module.marking =
    #Pass Mark
    module.pass_mark =
    #Delivery Type
    module.delivery_type =
    #Pre-Requisites
    module.pre_requisites =
    #Co-Requisites
    module.co_requisites =
    #Barred Combinations
    module.barred_combinations =
    #Module Outline
    module.outline =
    #Indicative Content
    module.indicative_content =
    #Learning Outcomes
    module.learning_outcomes =
    #Learning And Teaching Strategy
    module.learning_and_teaching_strategy =
    #Learning & Teaching Methods
    module.learning_and_teaching_methods =
    #Formative Assessment Strategy
    module.formative_assessment_strategy =
    #Summative Assessment Strategy
    module.summative_assessment_strategy =
    #Summative Assessments
    module.summative_assessments =
    #Learning Resources
    module.learning_resources = 
    #Feedback to Students
    module.student_feedback =
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
    module_json += '{"name": "This Module requires you to attend particular classes or events at particular times and in particular locations.","size": 20}]},
    module_json += '{"name": "Pre-Requisites","size": 20,"children": ['
    #loop to add all pre-requisites
    module_json += '{"name": "None Specified","size": 20}'
    module_json += ']},'
    module_json += '{"name": "Co-Requisites","size": 20,"children": ['
    #loop to add all co-requisites
                            {"name": "None Specified","size": 20}
    module_json += ']},'
    module_json += '{"name": "Barred Combinations","size": 20,"children": ['
    #loop to add all barred combinations
                            {
                                "name": "None Specified",
                                "size": 20
                            }
                        ]
                    },
    module_json += '{"name": "Module Outline","size": 20,"children": ['
                            {"name": "This module will introduce you to the principles of good design, layout and development practices for the creation of websites, focusing strongly on web accessibility and user experience issues for all users, but especially looking at those who may have ability impairments and developing solutions to assist them in their browsing experience in line with the University’s policy on diversity. You will learn how to layout and develop a website using Hyper Text Markup Language (HTML) and JavaScript to add functionality and interactivity to your website. You will also learn how to incorporate CSS (Cascading Style Sheets) to enhance the usability, layout and presentation of a website. You will learn about the issues of copyright on the web and you will have an understanding of how you can avoid becoming both a culprit and a victim of copyright theft.",
                                "size": 20
                            },
                            {
                                "name": "Bolton values: Taught (T), Developed (D) and Assessed (A).",
                                "size": 20
                            }
                        ]
                    },
    module_json += '{"name": "Indicative Content","size": 20,"children": ['
                        #loop to insert all indicative content items
                            {
                                "name": "Analysis and evaluation of website design",
                                "size": 20
                            },
                            {
                                "name": "Copyright and the Internet",
                                "size": 20
                            },
                            {
                                "name": "User experience",
                                "size": 20
                            },
                            {
                                "name": "Website accessibility",
                                "size": 20
                            },
                            {
                                "name": "Website production software",
                                "size": 20
                            },
                            {
                                "name": "Hypertext Markup Language (HTML)",
                                "size": 20
                            },
                            {
                                "name": "Cascading Style Sheets (CSS)",
                                "size": 20
                            },
                            {
                                "name": "Javascript (JS)",
                                "size": 20
                            },
                            {
                                "name": "Domain Name Systems (DNS)",
                                "size": 20
                            },
                            {
                                "name": "File Transfer Protocol (FTP)",
                                "size": 20
                            },
                            {
                                "name": "Web Hosting systems",
                                "size": 20
                            },
                            {
                                "name": "Online marketing techniques",
                                "size": 20
                            }
                        ]
                    },
    module_json += '{"name": "Learning Outcomes","size": 20,"children": ['
                        #loop to insert all learning outcome items
                            {
                                "name": "display knowledge and understanding of Internet structure, applications and services.",
                                "size": 20
                            },
                            {
                                "name": "design a website that is easy to use by a variety of different user groups.",
                                "size": 20
                            },
                            {
                                "name": "select and use appropriate software packages to design and produce a simple website.",
                                "size": 20
                            },
                            {
                                "name": "create a series of web pages that present information, graphics and provide hypertext links to other documents within your website and on the Internet.",
                                "size": 20
                            },
                            {
                                "name": "incorporate HTML, CSS and JavaScript into your website in order to enhance the presentation, layout and quality of the site’s content.",
                                "size": 20
                            }
                        ]
                    },
    module_json += '{"name": "Learning And Teaching Strategy","size": 20,"children": ['
                            {"name": "A blended learning approach is used in the module which means that you will attend sessions face-to-face and also use online learning. You will attend lectures, seminars and tutorials so that you learn the theoretical content and also have demonstrations and practical hands-on sessions so that you can develop and practice the skills needed to devise your own website. There will also be online sources and activities so that you can explore topics of interest and have online discussions with peers and your tutor. You will also use the internet-based applications to conduct advanced searches. You will also use the internet to find appropriate websites to evaluate prior to creating your own website.",
                                "size": 20},
                            {
                                "name": "Learning & Teaching Methods",
                                "size": 20,
                                "children": [
                                    {
                                        "name": "Hours",
                                        "size": 20,
                                        "children": [
                                            {
                                                "name": "67.5 scheduled",
                                                "size": 67.5
                                            },
                                            {
                                                "name": "132.5 independant",
                                                "size": 132.5
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "name": "Formative Assessment Strategy",
                        "size": 20,
                        "children": [
                            {
                                "name": "The timetabled online activity support is intended to provide a mechanism to allow you to gain on-going feedback on the work you are preparing throughout the module. Online tools such as discussion forums and/or wikis will be used to support these activities. You will be able to discuss your work with staff prior to assessment deadlines – this discussion will take place face-to-face and online.",
                                "size": 20
                            }
                        ]
                    },
                    {
                        "name": "Summative Assessment Strategy",
                        "size": 20,
                        "children": [
                            {
                                "name": "There are two items of assessment on which you will be graded and the grades for them will determine your overall grade for the module. In the first, you will write a technical report based upon a case study to demonstrate your achievement of the learning outcomes for the module. In the second, you will analyse a case study and develop a website using the skills you have learned throughout the module. You will also write a report on how you achieved your final design. This work will be assessed by the module academic team and feedback will be provided on the work.",
                                "size": 20
                            }
                        ]
                    },
                    {
                        "name": "Summative Assessments",
                        "size": 20,
                        "children": [
                        #loop to add all summative assessment items
                            {
                                "name": "Case study report (50%)",
                                "size": 50
                            },
                            {
                                "name": "Production of website based on HTML/CSS (50%)",
                                "size": 50
                            },
                            {"name": "Learning Resources","size": 20,"children": ['
                                #loop to add all learning resources
                                    {
                                        "name": "Krug S (2005) Don't Make Me Think!: A Common Sense Approach to Web Usability. 2nd ed. New Riders.",
                                        "size": 20
                                    },
                                    {
                                        "name": "Lawson, Bruce (2010) Introducing HTML 5. 1st ed. New Riders.",
                                        "size": 20
                                    },
                                    {
                                        "name": "McFarland, David Sawyer (2009) CSS: The Missing Manual. 2nd ed. Pogue Press.",
                                        "size": 20
                                    },
                                    {
                                        "name": "Osborn, Jeremy and AGI Creative Team (2010) Dreamweaver CS5 Digital Classroom. John Wiley & Sons.",
                                        "size": 20
                                    },
                                    {
                                        "name": "Robbins JN (2007) Learning Web Design: A Beginner's Guide to (X)HTML, StyleSheets, and Web Graphics. 3rd ed. O'Reilly.",
                                        "size": 20
                                    },
                                    {
                                        "name": "Robson, Elisabeth (2012) Head First HTML. 2nd ed. O'Reilly Media.",
                                        "size": 20
                                    },
                                    {
                                        "name": "Teague, Jason Cranford (2010) CSS3: Visual QuickStart Guide. 5th ed. Peachpit Press.",
                                        "size": 20
                                    }
                                ]
                            },
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
