#good_messages.py
from jinja2 import Environment, FileSystemLoader
MAX_SCORE = 100
TEST_NAME = "Python Challenge"
students = [
{"name":"Willow", "score":100},
{"name":"Cordelia", "score":85},
{"name":"Oz", "score":95},
{"name":"Raven", "score":45},
{"name":"Percy", "score":65},
]

env = Environment (loader= FileSystemLoader("templates/")) 

template = env.get_template("export-temp.csv") 


for student in students:
    name = student["name"]
    filename = f"output/py_challenge.csv"
    context = {
        "students": students,
        "Max_Score": MAX_SCORE
    }


    with open(filename, "w", encoding="utf-8") as f:
        f.write(template.render(context))
        print(f"Created {filename}")
