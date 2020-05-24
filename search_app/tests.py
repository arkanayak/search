import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock
from utils.search_query import get_author_api, search
from mock import patch

requests = Mock()


class TestApiSearch(unittest.TestCase):
    def log_request(self, url):
        print(f'Making a request to {url}.')
        print('Request received!')
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {"author": "Paul Kalanithi"}
        requests.get.side_effect = [Timeout, response_mock]
        return response_mock

    def test_get_author_api(self):
        requests.get.side_effect = self.log_request
        assert get_author_api(53)['author'] == 'Paul Kalanithi'

    def test_search(self):
        return_val = [
            {
                "id": 0,
                "summary": "The Book in Three Sentences: Practicing meditation and mindfulness will make you at least "
                           "10 percent happier. Being mindful doesn’t change the problems in your life, "
                           "but mindfulness does help you respond to your problems rather than react to them. "
                           "Mindfulness helps you realize that striving for success is fine as long as you accept "
                           "that the outcome is outside your control.",
            },
            {
                "id": 48,
                "summary": "The Book in Three Sentences: Finding something important and meaningful in your life is "
                           "the most productive use of your time and energy. This is true because every life has "
                           "problems associated with it and finding meaning in your life will help you sustain the "
                           "effort needed to overcome the particular problems you face. Thus, we can say that the key "
                           "to living a good life is not giving a fuck about more things, but rather, giving a fuck "
                           "only about the things that align with your personal values.",
            },
            {
                "id": 7,
                "summary": "The Book in Three Sentences: Everything in life is an invention. If you choose to look at "
                           "your life in a new way, then suddenly your problems fade away. One of the best ways to do "
                           "this is to focus on the possibilities surrounding you in any situation rather than "
                           "slipping into the default mode of measuring and comparing your life to others.",
            }
        ]
        with patch('utils.search_query.search', return_value=return_val):
            ret = search('is your problems', 3)
            self.assertEqual(ret, return_val)


if __name__ == '__main__':
    unittest.main()
