from pymongo import MongoClient

server = MongoClient("149.89.161.100")
db = server.TeamMango
c = db.students

courses = open("courses.csv").read().strip().split("\n")[1:]
peeps = open("peeps.csv").read().strip().split("\n")[1:]
