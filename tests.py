# from starship_pilots import *
from swapi_call import *
import unittest


class TestYourClassInitialization(unittest.TestCase):

    def test_default_swapi_base_url(self):
        instance = StarWarsAPI()
        self.assertEqual(instance.swapi_base_url, 'https://swapi.dev/api/',
                         "Default swapi_base_url is not set correctly")

    def test_custom_swapi_base_url(self):
        custom_url = 'https://custom-swapi-url.com/api/'
        instance = StarWarsAPI(swapi_base_url=custom_url)
        self.assertEqual(instance.swapi_base_url, custom_url,
                         "Custom swapi_base_url is not set correctly")


if __name__ == '__main__':
    unittest.main()

# class TestStarshipPilotsInitialization(unittest.TestCase):
#
#     def test_starship_pilots_list(self):
#         # Assuming get_starships_data is a function that returns a sample starships data
#         def mock_get_starships_data():
#             return {'results': [
#                 {'name': 'Starship1', 'pilots': ['Pilot1', 'Pilot2']},
#                 {'name': 'Starship2', 'pilots': ['Pilot3', 'Pilot4']},
#             ]}
#
#         # Monkey-patching the get_starships_data function to return the mock data
#         with unittest.mock.patch('starship_pilots.get_starships_data', side_effect=mock_get_starships_data):
#             starship_pilots = Starship_Pilots()
#
#         expected_list = [
#             {'Starship1': ['Pilot1', 'Pilot2']},
#             {'Starship2': ['Pilot3', 'Pilot4']},
#             # Add more expected data as needed
#         ]
#
#         self.assertEqual(starship_pilots.list, expected_list,
#                          "Starship_Pilots list is not initialized correctly")
