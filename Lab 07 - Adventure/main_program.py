#!/usr/bin/env python3
#adventure quest
#James Allen
#11/20/17

room_list = []

room = ["You have made your way into the dungeon you see an exit to the south"
        , None, None, 1, None]
room_list.append(room)
room = ["You step into the north hall you see exits west, east, and a way further into the hall",
        0, 3, 7, 2]
room_list.append(room)
room = ["Northwest Room", None, 1, 4, None]
room_list.append(room)
room = ["Northeast Room", None, None, 5, 1]
room_list.append(room)
room = ["West Hallway", 2, None, 6, None]
room_list.append(room)
room = ["East Hallway", 3, None, 8, None]
room_list.append(room)
room = ["Southwest Room", 4, 7, None, None]
room_list.append(room)
room = ["South Hallway", 1, 8, 9, 6]
room_list.append(room)
room = ["Southeast Room", 5, None, None, 7]
room_list.append(room)
room = ["South Room", 7, None, None, None]
current_room = 0
