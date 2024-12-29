#good_messages.py
from jinja2 import Environment, FileSystemLoader
MAX_SCORE = 100
TEST_NAME = "Python Challenge"
students = [
{"name":"Willow", "score":100},
{"name":"Cordelia", "score":85},
{"name":"Oz", "score":95},
]

env = Environment (loader= FileSystemLoader("templates/")) 

template = env.get_template("good.txt") 


for student in students:
    name = student["name"]
    filename = f"output/message_{name.lower()}.txt"
    content = template.render(
        student,
        MAX_SCORE=MAX_SCORE,
        TEST_NAME=TEST_NAME,
    )
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
        print(f"Created {filename}")
