from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
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
#items in rooms

# room['outside'].items = [Item("empty", "nothing to see here...")]
room['foyer'].items = [Item("bandana", "A dusty, tattered, old red bandana.")]
room['overlook'].items = [Item("flashlight", "Beat up, but still functional...it could be useful."), Item("sword", "It's definitely seen better days, but a sword is a sword.")]
room['narrow'].items = [Item("coins", "Looks like somebody dropped a few gold coins in a hurry...")]
room['treasure'].items = [Item("bones", "Someone made off with the treasure...but at what cost?")]

# Make a new player object that is currently in the 'outside' room.
name = None
while not name:
    name = input("PLease Enter Your Name: ")
me = Player(name, "outside")
print(f'\n Welcome, {me.name.capitalize()}! Your adventure begins!')
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
end_game = False
while not end_game:

    # def room_info(arg):
    #     for key, value in arg.items():
    #         if key == me.current_room:
    #             print(f'Current Location: {value.name}.\n "{value.description}"')
    # room_info(room)

    print(f'\n Current Location: {room[me.current_room].name}.\n \n"{room[me.current_room].description}"')

    # item search
    search = True
    while search:

        browse = input('\n Search room for items? (y/n) [or i to access inventory]: ')

        if browse == "y" and room[me.current_room].items != None and room[me.current_room].items:
            for item in room[me.current_room].items:
                print(f'\n You look around and find: {item.name} - {item.description}\n')
            # logic for picking up items
            pickup = True
            while pickup:
                get_item = input('Enter "get/take [item name]" to pickup item, or c to cancel: ')
                action = get_item.lower().split(" ")
                if action[0] == "c":
                    pickup = False
                elif action[0] == "get" or action[0] == "take":
                    found = False
                    for item in room[me.current_room].items:
                        if action[1] == item.name:
                            found = True
                            me.inventory.append(item)
                            room[me.current_room].items.remove(item)
                            print(f'\n You picked up "{action[1]}!"\n')
                    if found == False:
                        print("\n Item could not be found. Try again.\n")
                else:
                    # pickup = False
                    print('\n Invalid Input.\n')        
            # search = False 
        elif browse == "i":
            if me.inventory:
                check_inv = True
                while check_inv:
                    print('\n INVENTORY:')
                    for item in me.inventory:
                        print(f'\n{item.name} - {item.description}')
                    item_drop = input('\n Enter "drop [item name]" to drop item, or c to cancel: ')
                    drop_action = item_drop.lower().split(" ")
                    if drop_action[0] == "c":
                        check_inv = False
                    elif drop_action[0] == "drop":
                        found = False
                        for item in me.inventory:
                            if drop_action[1] == item.name:
                                found = True
                                me.inventory.remove(item)
                                room[me.current_room].items.append(item)
                                print(f'\n You dropped "{drop_action[1]}!"\n')
                        if found == False:
                            print("\n Item could not be found. Try again.\n")
                    else:
                         print('\n Invalid Input.\n')
            else:
                print('\n There are no items in your inventory.\n')
                check_inv = False
        elif browse == "n":
            search = False
        elif room[me.current_room].items == None or not room[me.current_room].items and browse == "y":
            print(f'\n You look around, but find nothing...')
            search = False
        else:
            print("\n Invalid input. Please try again")

    # move in a direction
    move = False
    while not move:
        
        make_move = input("\n Enter a direction to move in (n, s, e, w) or enter q to quit: ")
        
        if make_move == "q":
            print("\n Game Over!!!")
            end_game = True
            move = True
        elif make_move != "n" and make_move != "s" and make_move != "e" and make_move != "w":
            print("\n Not a valid direciton. Please try again.\n")
        else:
            move = True

    if make_move == "n":
        if room[me.current_room].n_to == None:
            print("\n Hmm...looks like a dead end.\n")
        else:
            for key, value in room.items():
                if value == room[me.current_room].n_to:
                    me.current_room = key
            
    if make_move == "s":
        if room[me.current_room].s_to == None:
            print("\n Hmm...looks like a dead end.\n")
        else:
            for key, value in room.items():
                if value == room[me.current_room].s_to:
                    me.current_room = key

    if make_move == "e":
        if room[me.current_room].e_to == None:
            print("\n Hmm...looks like a dead end.\n")
        else:
            for key, value in room.items():
                if value == room[me.current_room].e_to:
                    me.current_room = key

    if make_move == "w":
        if room[me.current_room].w_to == None:
            print("\n Hmm...looks like a dead end.\n")
        else:
            for key, value in room.items():
                if value == room[me.current_room].w_to:
                    me.current_room = key