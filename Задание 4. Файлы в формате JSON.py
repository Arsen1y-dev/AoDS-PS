import json
import csv

with open('constellations.json', 'r') as json_file:
    data = json.load(json_file)

# Задание порядка сортировки по яркости для каждого созвездия
sorting_order = {
    "Orion": lambda star: star["brightness"],
    "Ursa Major": lambda star: star["brightness"],
    "Cygnus": lambda star: star["brightness"]
}

# Сортировка ярчайших звезд для каждого созвездия
for constellation in data["constellations"]:
    constellation["brightest_stars"].sort(key=sorting_order[constellation["latin_name"]])


fields = ['star_name', 'brightness', 'constellation_name', 'latin_name', 'abbreviation', 'area', 'neighboring_constellations']
with open('stars.csv', 'w', newline='') as out_file:
    writer = csv.DictWriter(out_file, fieldnames=fields, delimiter=',')
    writer.writeheader()
    for constellation in data["constellations"]:
        for star in constellation["brightest_stars"]:
            writer.writerow({
                'star_name': star["name"],
                'brightness': star["brightness"],
                'constellation_name': constellation["latin_name"],
                'latin_name': constellation["latin_name"],
                'abbreviation': constellation["abbreviation"],
                'area': constellation["area"],
                'neighboring_constellations': ', '.join(constellation["neighboring_constellations"])
            })
