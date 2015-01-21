import json
import lxml
from lxml import html
import requests

class Module:
    def __init__(self, module_id):
        self.module_id = module_id    # instance variable unique to each instance
        #download the data for this module and insert it into the relevant fields, returning a Module object
        #calculate the module detail url
        url = "https://modules.bolton.ac.uk/" + module_id
        #get the html page at url
        page = requests.get(url)
        #parse the html into a tree
        tree = lxml.html.fromstring(page.text)
        #extract the relevant data, adding it to the Module object
        #module id
        self.id = module_id
        paragraphs = tree.xpath('//p/text()')
        header4s = tree.xpath('//h4/text()')
        dds = tree.xpath('//dd/text()')
        tables = tree.xpath('//table/text()')
        #module title
        self.title = header4s[0]
        #Credits
        self.credits = dds[0]
        #Level
        self.level = dds[1]
        #Type
        self.type = dds[2]
        #Duration
        self.duration = dds[3]
        #Trimester 3?
        self.trim3 = dds[4]
        #ECTS
        self.ects = dds[5]
        #Marking Scheme
        self.marking = dds[6]
        #Pass Mark
        self.pass_mark = paragraphs[0]
        #Delivery Type
        self.delivery_type = paragraphs[1]
        #Pre-Requisites
        self.pre_requisites = paragraphs[2]
        #Co-Requisites
        self.co_requisites = paragraphs[3]
        #Barred Combinations
        self.barred_combinations = paragraphs[4]
        #Module Outline
        self.outline = paragraphs[5] + "  " + paragraphs[6]
        #Indicative Content
        #self.indicative_content = tables[0]
        #Learning Outcomes
        #self.learning_outcomes = tables[1]
        #Learning And Teaching Strategy
        self.learning_and_teaching_strategy = paragraphs[7]
        #Learning & Teaching Methods
        #self.learning_and_teaching_methods = tables[2]
        #Formative Assessment Strategy
        self.formative_assessment_strategy = paragraphs[8]
        #Summative Assessment Strategy
        self.summative_assessment_strategy = paragraphs[9]
        #Summative Assessments
        #self.summative_assessments = tables[3]
        #Learning Resources
        #self.learning_resources = tables[4]
        #Feedback to Students
        self.student_feedback = paragraphs[10]

def parse_json(module):
    #translate the module data into a json string portion
    module_json = '''{"name": "''' + module.id + '''","size": 20,"children": ['''
    module_json += '''{"name":"''' + module.title + '''","size": 60},'''
    #module_json += '''{"name": "Details","size": 20,"children": ['''
    #module_json += '''{"name": "Credits:''' + module.credits + '''","size": ''' + module.credits + '''},'''
    #module_json += '''{"name": "Level:''' + module.level + '''","size": 20},'''
    #module_json += '''{"name": "Type:''' + module.type + '''","size": 20},'''
    #module_json += '''{"name": "Duration:''' + module.duration + '''","size": ''' + module.duration + '''},'''
    #module_json += '''{"name": "Trimester 3?:''' + module.trim3 + '''","size": 20},'''
    #module_json += '''{"name": "ECTS:''' + module.ects + '''","size": ''' + module.ects + '''},'''
    #module_json += '''{"name": "Marking Scheme:''' + module.marking + '''","size": 100},'''
    #module_json += '''{"name": "Pass Mark:''' + module.pass_mark + '''","size": 20}'''
    #module_json += ''']},'''
    module_json += '''{"name": "Delivery Type","size": 20,"children": ['''
    module_json += '''{"name": "''' + module.delivery_type + '''","size": 20}]},'''
    module_json += '''{"name": "Pre-Requisites","size": 20,"children": ['''
    module_json += '''{"name": "''' + module.pre_requisites + '''","size": 20}'''
    module_json += ''']},'''
    module_json += '''{"name": "Co-Requisites","size": 20,"children": ['''
    module_json += '''{"name": "''' + module.co_requisites + '''","size": 20}'''
    module_json += ''']},'''
    module_json += '''{"name": "Barred Combinations","size": 20,"children": ['''
    module_json += '''{"name": "''' + module.barred_combinations + '''","size": 20}'''
    module_json += ''']},'''
    module_json += '''{"name": "Module Outline","size": 20,"children": ['''
    module_json += '''{"name": "'''+ module.outline + '''","size": 20}'''
    module_json += ''']},'''
    #module_json += '''{"name": "Indicative Content","size": 20,"children": ['''
    #loop to insert all indicative content items
    #idicatives = module.indicative_content.xpath('//td/text()')
    #only insert tds that are text, not just a number
    #for indicative in indicatives:
        #if indicative is not just a number:
        #if re.match("^[0-9 ]+$", indicative) is False:
            #module_json += '''{"name": "''' + indicative + '''","size": 20},'''
            #module_json += ''']},'''
            #remove trailing comma on last indicative

    #module_json += '''{"name": "Learning Outcomes","size": 20,"children": ['''
    #loop to insert all learning outcome items
    #outcomes = module.learning_outcomes.xpath('//td/text()')
    #only insert tds that are text, not just a number
    #for outcome in outcomes:
        #if outcome is not just a number:
        #if re.match("^[0-9 ]+$", outcome) is False:
            #module_json += '''{"name": "''' + outcome + '''","size": 20},'''
            #module_json += ''']},'''
            #remove trailing comma on last outcome
    #module_json += ''']},'''
    module_json += '''{"name": "Learning And Teaching Strategy","size": 20,"children": ['''
    module_json += '''{"name": "''' + module.learning_and_teaching_strategy + '''","size": 20},'''
    #module_json += '''{"name": "Learning & Teaching Methods","size": 20,"children": ['''
    #module_json += '''{"name": "Hours","size": 20,"children": ['''
    #hours = module.learning_and_teaching_methods.xpath('''//td/text()''')
    #scheduled = hours[2]
    #independant =  hours[5]
    #module_json += '''{"name": "''' + scheduled + ''' scheduled","size": ''' + scheduled + '''},'''
    #module_json += '''{"name": "''' + independant + ''' independant","size": ''' + independant + '''}'''
    #module_json += ''']},'''
    module_json += '''{"name": "Formative Assessment Strategy","size": 20,"children": ['''
    module_json += '''{"name": "''' + module.formative_assessment_strategy + '''","size": 20}'''
    module_json += ''']},'''
    module_json += '''{"name": "Summative Assessment Strategy","size": 20,"children": ['''
    module_json += '''{"name": "''' + module.summative_assessment_strategy + '''","size": 20}'''
    module_json += ''']}'''
    #module_json += '''{"name": "Summative Assessments","size": 20,"children": ['''
    #loop to add all summative assessment items
    #summative_rows = module.summative_assessments.xpath('''//tr/text()''')
    #for row in summative_rows:
        #summatives = row.xpath('//td/text()')
        #add summative details
        #KIS
        #module_json += '''{"name": "''' + summatives[2] + '''","size": 20'''
        #Description
        #module_json += '''{"name": "''' + summatives[3] + '''","size": 20'''
        #Learning Outcomes
        #module_json += '''{"name": "''' + summatives[4] + '''","size": 20'''
        #Marking Scheme
        #module_json += '''{"name": "''' + summatives[5] + '''","size": 20'''
        #Passmark
        #module_json += '''{"name": "''' + summatives[6] + '''","size": ''' + summatives[6]
        #KIS Weighting
        #module_json += '''{"name": "''' + summatives[7] + '''","size": 20'''
        #module_json += ''']},'''
        #remove trailing comma on last summative
    #module_json += ''']},'''
    #module_json += '''{"name": "Learning Resources","size": 20,"children": ['''
    #loop to add all learning resources
    #resources = module.learning_resources.xpath('//td/text()')
    #for resource in resources:
        #module_json += '''{"name": "''' + resource + '''","size": 20},'''
        #module_json += ''']},'''
    #remove trailing comma on last resource

    module_json += ''']},'''
    module_json += '''{"name": "Feedback to Students","size": 20,"children": ['''
    module_json += '''{"name": "''' + module.student_feedback + '''","size": 20}'''
    module_json += ''']}]},'''
    return module_json

#course title
course_title = "Computing & Website Development HND/BSc (Hons)"

#array of modules in course
module_codes = ["CPU4000","CPU4003","CPU4005","CPU4001","CPU4002","CPU4004","CPU5001","CPU5002","CPU5003","CPU5000","CPU5004","CPU5005","CPU6000","CPU6001","CPU6002","CPU6004","CPU6003","CPU6005"]

#stitch together json modules under a root "course name" node
json_string = '''{"name":"''' + course_title + '''","children":['''

#add a json string for each module in this course
for module_code in module_codes:
  json_string += parse_json(Module(module_code))

#close the json string
json_string += "]}"

#remove invalid chars
out = ''.join([x for x in json_string if ord(x) < 128])

#print the json string
print(json_string)

#write the json to a file
with open('sampledata.json', 'w') as file_:
    file_.write(out)
