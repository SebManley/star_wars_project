import requests
import pymongo
import starship_pilot


client = pymongo.MongoClient()

db = client['starwars']

class replace_pilot_urls(Starship_Pilots):

    def __init__(self):
        super().__init__()

    def pilot_ids(self):
        pilot_names = []
        for starships in self.list:
            pilots = starships.values()
            if len(starships[pilots]) >= 1:
                driver_dict = {starships: []}
                for pilot in pilots:
                    pilot_details = requests.get(pilot)
                    json_pilot_details = pilot_details.json()
                    driver_dict[starships].append(json_pilot_details['name'])
                pilot_names.append(driver_dict)

        pilot_objectids = []
        for starship in pilot_names:
            pilot_ids_dict = {starship: []}
            name_list = starship.values()
            for name in name_list:
                character = db.characters.find_one({"name": name}, {"_id": 1})
                if character:
                    pilot_ids_dict[starship].append(character["_id"])
            pilot_objectids.append(pilot_ids_dict)




