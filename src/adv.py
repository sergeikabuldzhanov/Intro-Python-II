from player import Player
from room import Room
from item import Item

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons", [Item("Sword", "Get them with the pointy bit")]),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Bob", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
keepGoing = True
while keepGoing:
    print("You are in", player.current_room.name)
    print(player.current_room.description)
    if len(player.current_room.items):
        print(player.current_room.items)
    command = input("What would you like to do?\n")
    command_arr = command.split()
    if len(command_arr) == 1:
        if command in ["n", "s", "w", "e"]:
            if getattr(player.current_room, f"{command}_to") != None:
                player.current_room = getattr(
                    player.current_room, f"{command}_to")
            else:
                print("Can't move in that direction!")
        if command in ["i", "inventory"]:
            print("You have the following items in your inventory", player.inventory)
    if len(command_arr) == 2:
        if command_arr[0] == "get":
            player.get_item(command_arr[1])
        if command_arr[0] == "drop":
            player.drop_item(command_arr[1])
