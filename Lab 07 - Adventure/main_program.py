#!/usr/bin/env python3
#adventure quest
#James Allen
#11/20/17
"""Draft of lab 7"""

room_list = []

room = ["You have made your way into the dungeon.", None, None, 1, None]
room_list.append(room)
room = ["You senter the hall, it is very bright and damp.", 0, 3, 7, 2]
room_list.append(room)
room = ["You enter a room full of strange markings.", None, 1, 4, None]
room_list.append(room)
room = ["You enter the room that is filled with urnhs.", None, None, 5, 1]
room_list.append(room)
room = ["You enter a damp and dimly lit hallway.", 2, None, 6, None]
room_list.append(room)
room = ["You enter a very brightly lit hallway.", 3, None, 8, None]
room_list.append(room)
room = ["You enter the room, there is a small stream.", 4, 7, None, None]
room_list.append(room)
room = ["You enter the hall, it is very bright, and damp.", 1, 8, 9, 6]
room_list.append(room)
room = ["You enter the room, there appears to be nothing.", 5, None, None, 7]
room_list.append(room)
room = ["You enter the final room.", 7, None, None, None]
room_list.append(room)
current_room = 0

done = False



while not done:
    print()
    print(room_list[current_room][0])
    if room_list[current_room][1] != None:
        print("\tThere is an exit to the North.")
    if room_list[current_room][2] != None:
        print("\tThere is an exit to the East.")
    if room_list[current_room][3] != None:
        print("\tThere is an exit to the South.")
    if room_list[current_room][4] != None:
        print("\tThere is an exit to the West.")
    usr_direction = input("What way do you want to go ")
    

    
    if usr_direction.lower()[0] == 'n':
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room
    if usr_direction.lower()[0] == 'e':
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room
    if usr_direction.lower()[0] == 's':
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room        
    if usr_direction.lower()[0] == 'w':
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room            