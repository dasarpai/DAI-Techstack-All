class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population    
    def __repr__(self):
        return f'Country({self.name}, {self.population})'

country_list = [
                Country('Taiwan', 24_000_000),
                Country('Portugal', 10_000_000), 
                Country('Netherlands', 17_500_000), 
                Country('Nigeria', 198_000_000), 
                Country('Jordan', 10_000_000), 
                Country('Nepal', 30_000_000), 
                Country('Niger', 24_000_000), 
                Country('Japan', 128_000_000)
]

iso = [('Taiwan', 'iso24000000'), ('Portugal', 'iso10000000'), ('Netherlands', 'iso17500000'), ('Nigeria', 'iso198000000'), ('Jordan', 'iso10000000'), ('Nepal', 'iso30000000'), ('Niger', 'iso24000000'), ('Japan', 'iso128000000')]