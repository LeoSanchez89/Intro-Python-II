from room import Room
from player import Player

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
#

# Make a new player object that is currently in the 'outside' room.
name = None
while not name:
    name = input("PLease Enter Your Name: ")
me = Player(name, "outside")

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
    print(f'\n Current Location: {room[me.current_room].name}.\n "{room[me.current_room].description}"')
    move = False
    while not move:

        make_move = input("\n Enter a direction to move in (n, s, e, w) or enter q to quit: ")
        
        if make_move == "q":
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