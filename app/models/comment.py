class Comment(object):

    def __init__(self, post_id, id_, name, email, body):
        self.post_id = post_id
        self.id = id_
        self.name = name
        self.email = email
        self.body = body

    def get_dict(self):
        full_dict = self.__dict__
        return {key: full_dict[key] for key in full_dict if full_dict[key] is not None}

    def set_id(self):
        self.id = id
