import json
import csv

def sort_by_brightness(star):
    return star["brightness"]

with open('constellations.json', 'r') as json_file:
    data = json.load(json_file)

sorting_order = {
    "Orion": sort_by_brightness,
    "Ursa Major": sort_by_brightness,
    "Cygnus": sort_by_brightness
}

for constellation in data["constellations"]:
    constellation["brightest_stars"].sort(key=sorting_order[constellation["latin_name"]])


fields = ['star_name', 'brightness', 'constellation_name', \
          'latin_name', 'abbreviation', 'area', 'neighboring_constellations']


with open('stars.csv', 'w') as out_file:
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

writer = csv.DictWriter(res_csv, fieldnames=fields, delimiter=';')
writer.writeheader()
for row in data["constellations"]:
    row["brightest_stars"] = ", ".join([star["name"] for star in row["brightest_stars"]])
    row["neighboring_constellations"] = ", ".join(row["neighboring_constellations"])
    writer.writerow(row)