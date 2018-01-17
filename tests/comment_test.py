import unittest

import requests
import HtmlTestRunner

import app.comments_helper as comments_helper


class CommentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("1. setupclass method called \n")
        cls.base_url = 'http://jsonplaceholder.typicode.com/'
        cls.comments_url = cls.base_url + 'comments/'

    @classmethod
    def tearDownClass(cls):
        print("3. teardownclass method called \n")
        comments_helper.clean_up()

    # @unittest.skip
    def setUp(self):
        print('2. setUp method called \n')
        data = {
            "name": 'John Snou',
            "email": "test@gmail.com",
            "body": "bla-bla"}
        requests.delete(self.comments_url + '499')
        self.comment = comments_helper.create_comment(self.comments_url, data)
        print('this is comment in setup method: ', self.comment)

    @unittest.skip
    def tearDown(self):
        print("4. teardown method called \n")
        requests.delete(self.comments_url)

    @unittest.skip
    def test_get_comments(self):
        response = requests.get(self.comments_url)
        self.assertEqual(response.status_code, 200)
        comments = response.json()
        for comment in comments:
            self.assertNotEqual(comment['body'], None)

    @unittest.skip
    def test_comment_creation(self):
        original_comment = {'name': 'Lora', 'email': 'test@i.ua', 'body': 'my first comment'}
        response = requests.post(self.comments_url, original_comment)
        self.assertEqual(response.status_code, 201)

        new_comment = response.json()

    @unittest.skip
    def test_get_comment(self):
        response = requests.get(self.comments_url + str(self.comment['id']))
        new_comment = response.json()
        print("---------------------------------")
        print(self.comment)
        print("---------------------------------")
        print(new_comment)
        print("---------------------------------")
        self.assertEqual(new_comment["name"], self.comment["name"])
        self.assertEqual(new_comment['body'], self.comment['body'])


if __name__ == '__main__':
    unittest.main(verbosity=3, testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
