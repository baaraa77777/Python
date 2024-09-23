capitals = {
    "Nepal": "Kathmandu",
    "France": "Paris"
}

#nesting list in a dictionary
cities = {
    "Nepal": ["Birtamode", "Kathmandu", "Pokhara"],
    "France": ["Paris", "Lille"]
}

#nesting dictionary in a dictionary
visit_cities ={
    "Nepal": {"cities_visited":["Birtamode", "Kathmandu", "Pokhara"], "total_visits": 23},
    "France": {"cities_visited":["Paris", "Lille"], "total_visits": 2}}

#Nesting dictionary in a list
travel_log =[
    {
        "country":"Nepal", 
        "cities":["Birtamode", "Kathmandu", "Pokhara"], 
        "visits": 23
    },
    {
        "country":"France",
        "cities_visited":["Paris", "Lille"], 
        "total_visits": 2
    }
]

def add_new_country(count, visit, city):
    new_country = {}
    new_country["country"] = count
    new_country["cities_visited"] = city
    new_country["total_visits"] = visit
    travel_log.append(new_country)
    

visit = 2
add_new_country("Russia", 2, ["moscow", "Saint Petersburg"])

print(travel_log)