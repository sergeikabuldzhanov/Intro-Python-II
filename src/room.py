# Implement a class to hold room information. This should have name and
# description attributes.


class Room(object):
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def add_item(self, item):
        self.items += [item]

    def remove_item(self, item_name):
        self.items = [item in self.items if item_name != item.name]
