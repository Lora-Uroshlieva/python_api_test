class Post(object):

    def __init__(self, user_id, id_, title, body):
        self.userId = user_id
        self.id = id_
        self.title = title
        self.body = body

    def __str__(self):
        return 'Post: ' + self.title + '\n Text: ' + self.body

    def set_id(self, id_):
        self.id = id_

    def get_dict(self):
        full_dict = self.__dict__
        return {key: full_dict[key] for key in full_dict if full_dict[key] is not None}
