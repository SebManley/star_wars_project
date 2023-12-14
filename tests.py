from starship_pilots import *
from swapi_call import *
import unittest
from unittest.mock import patch


class TestSWAPICall(unittest.TestCase):

    def test_default_swapi_base_url(self):
        instance = StarWarsAPI()
        self.assertEqual(instance.swapi_base_url, 'https://swapi.dev/api/',
                         "Default swapi_base_url is not set correctly")

    def test_custom_swapi_base_url(self):
        custom_url = 'https://custom-swapi-url.com/api/'
        instance = StarWarsAPI(swapi_base_url=custom_url)
        self.assertEqual(instance.swapi_base_url, custom_url,
                         "Custom swapi_base_url is not set correctly")

    @patch('swapi_call.r.get')
    def test_get_starships_data(self, mock_get):
        # Mocking the response of the requests.get method
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = {'results': [{'name': 'Starship1'}, {'name': 'Starship2'}]}
        mock_get.return_value = mock_response

        # Creating an instance of Starship_Pilots
        star_wars_api = StarWarsAPI()

        # Calling the method we want to test
        result = star_wars_api.get_starships_data()

        # Assertions
        mock_get.assert_called_once_with('https://swapi.dev/api/starships/')
        self.assertEqual(result, {'results': [{'name': 'Starship1'}, {'name': 'Starship2'}]})


class TestStarshipPilotsInitialization(unittest.TestCase):

    @patch('starship_pilots.Starship_Pilots.get_starships_data')
    def test_starship_pilots_list(self, mock_get_starships_data):
        # Mocking the response of the get_starships_data method
        mock_get_starships_data.return_value = {'results': [
            {'name': 'Starship1', 'pilots': ['Pilot1', 'Pilot2']},
            {'name': 'Starship2', 'pilots': ['Pilot3', 'Pilot4']},
        ]}

        # Creating an instance of Starship_Pilots
        starship_pilots = Starship_Pilots()

        expected_list = [
            {'Starship1': ['Pilot1', 'Pilot2']},
            {'Starship2': ['Pilot3', 'Pilot4']},
        ]

        self.assertEqual(starship_pilots.list, expected_list,
                         "Starship_Pilots list is not initialized correctly")


if __name__ == '__main__':
    unittest.main()