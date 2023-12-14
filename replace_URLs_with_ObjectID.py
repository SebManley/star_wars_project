import requests
import pymongo
import starship_pilot


client = pymongo.MongoClient()

db = client['starwars']

class replace_pilot_urls(Starship_Pilots):

    def __init__(self):
        super().__init__()

    def replace_urls(self):
        for starship in self.list:
            pilot_urls = starship.get("pilots", [])
            pilot_objectids = []
            for pilot_url in pilot_urls:
                character = db.characters.find_one({"url": pilot_url})
                if character:
                    pilot_objectids.append(character["_id"])
            starship["pilots"] = pilot_objectids
        return self.list


