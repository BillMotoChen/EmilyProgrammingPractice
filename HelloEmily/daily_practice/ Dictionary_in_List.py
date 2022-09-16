travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

# Write the function that will allow new countries
# to be added to the travel_log.

def add_new_country(country_visited, time_visited, cities_visited):
    new_dict = {}
    new_dict["country"] = country_visited
    new_dict["visits"] = time_visited
    new_dict["cities"] = cities_visited
    travel_log.append(new_dict)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)