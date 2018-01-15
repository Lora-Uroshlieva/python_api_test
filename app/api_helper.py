import requests


class JsonplaceholderRestApi:

    def __init__(self):
        self.host = 'jsonplaceholder.typicode.com'
        self.base_url = "http://{}/".format(self.host)
        self.url_comments = self.base_url + "comments/"

    def create_comment(self, comment):
        response = requests.post(self.base_url, data=comment.get_dict())
        return response.json()

    def get_comment(self, comment):
        response = requests.get(self.url_comments + comment.id)
        return response.json()

    def get_comments(self):
        response = requests.get(self.url_comments)
        return response.json()

    def remove_comment(self, comment):
        response = requests.delete(self.url_comments + str(comment.id))
        return response.json()
