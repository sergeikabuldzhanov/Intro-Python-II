# Write a class to hold player information, e.g. what room they are in
# currently.


class Player(object):
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def get_item(self, item_name):
        for i in range(len(self.current_room.items)):
            if self.current_room.items[i].name.lower() == item_name.lower():
                picked_item = self.current_room.items[i]
                self.inventory.append(picked_item)
                picked_item.on_take()
                self.current_room.items.pop(i)
                return self
        print(f"There's no {item_name} in this room")

    def drop_item(self, item_name):
        for i in range(len(self.inventory)):
            if self.inventory[i].name == item_name:
                dropped_item = self.inventory[i]
                self.current_room.items.append(dropped_item)
                dropped_item.on_drop()
                self.inventory.pop(i)
                return self
        print(f"There's no {item_name} in your inventory")
