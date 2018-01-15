class User(object):

    def __init__(self, id_, full_name, username, email, address, phone, website, company):
        self.id = id_
        self.full_name = full_name
        self.username = username
        self.email = email
        self.address = address
        self.phone = phone
        self.website = website
        self.company = company

    def __str__(self):
        return 'User ' + self.full_name + 'with phone ' + self.phone

    def set_id(self, id_):
        self.id = id_

    def get_dict(self):
        full_dict = self.__dict__
        return {key: full_dict[key] for key in full_dict if full_dict[key] is not None}
