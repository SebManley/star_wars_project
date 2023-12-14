import requests
import pymongo
import starship_pilot


client = pymongo.MongoClient()

db = client['starwars']

class replace_pilot_urls(Starship_Pilots):

    def __init__(self):
        super().__init__()

    def replace_urls(self):
        pilot_names = []
        for pilot in self.list:
            for pilot_url in pilot:
                if len(pilot[pilot_url]) >= 1:
                    pilot_details = requests.get(pilot[pilot_url])
                    json_pilot_details = pilot_details.json()
                    pilot_names.append({json_pilot_details['starships']: json_pilot_details['name']})

        pilot_objectids = []
        for pilot in pilot_names:
            character = db.characters.find_one({"name": pilot}, {"_id": 1})
            if character:
                pilot_objectids.append(character["_id"])




