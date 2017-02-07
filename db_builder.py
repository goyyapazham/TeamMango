from pymongo import MongoClient
import csv

server = MongoClient("127.0.0.1")
db = server.TeamMango
c = db.students

f = open("peeps.csv", "r")
pdata = csv.DictReader(f)

g = open("courses.csv", "r")
cdata = csv.DictReader(g)

for peep in pdata:
    d = {}
    d['name'] = peep['name']
    d['age'] = int(peep['age'])
    d['id'] = int(peep['id'])
    d['courses'] = {}
    for course in cdata:
        if course['id'] == peep['id']:
            d['courses'][course['code'] = int(course['mark'])
    g.seek(0)
    #print d
    c.insert_one(d)

f.close()
g.close()

for student in c.students:
    sum = 0
    for key,value in student['courses']:
        sum += value
    avg = sum*1.0 / (len(student['courses']))
    print "Name: %s\nID: %d\nAverage: %f\n"%(student['name'], student['id'], avg)
                         

