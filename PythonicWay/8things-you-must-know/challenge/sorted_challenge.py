class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population    
    def __repr__(self):
        return f'Country({self.name}, {self.population})'
    def __eq__(self, other):
        return f'Country({self.name}, {self.population})' == f'Country({other.name}, {other.population})'

country_list = [
                Country('Taiwan', '24000000iso'),
                Country('Portugal', '10000000iso'), 
                Country('netherlands', '17500000iso'), 
                Country('nigeria', '198000000iso'), 
                Country('jordan', '10000000iso'), 
                Country('nepal', '30000000iso'), 
                Country('niger', '24000000iso'), 
                Country('japan', '128000000iso')
]

def get_sorted():
    """Return the country list so that it is sorted first by population 
    and then alphabetically by country name.""" 
    pass # Replace this line with your solution