'''
Expected output:
The capital city of Netherlands is Amsterdam
The capital city of Nigeria is Abuja
The capital city of Jordan is Amman
The capital city of Nepal is Kathmandu
The capital city of Niger is Niamey
The capital city of Japan is Tokyo
'''

countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
capitals = ['Amsterdam', 'Abuja', 'Amman', 'Kathmandu', 'Niamey', 'Tokyo']

from itertools import zip_longest
for country, capital in zip_longest(countries, capitals, fillvalue='Unknown'):   
    print(f'The capital city of {country} is {capital}')

pairs = list(zip(countries, capitals))
ctr, cap = zip(*pairs)