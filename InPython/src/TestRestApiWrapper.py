import unittest
import json
from run import app

class TestRestApiWrapper(unittest.TestCase):

    def test_get(self):
        tester = app.test_client(self)
        response = tester.get('/')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['Message'], 'Fine')



if __name__ == '__main__':
    unittest.main()