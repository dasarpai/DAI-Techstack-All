import jinja2 as jijna2
env = jijna2.Environment()
template = env.from_string("Hello {{ name }}!") 
print(template.render(name="World"))    