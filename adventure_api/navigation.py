'''
This is a doc string
'''


def move_action(_loc, _dir):
    '''
    This function will evaluate a proposed move. Send it the player's current room and
    the direction to go (N, S, E, W, U or D). The module will evaluate if the direction
    can be traveled or not.

    Returns a dictionary with 3 keys:
      start_room (INT)
      move_result (PASS|FAIL)
      current_room (INT)

    :return:
    '''

    _data = {}
    _data['start_room'] = _loc

    _potential_room = map_data[str(_loc)]['travel'][travel_directions[str(_dir)]]

    if _potential_room:
        _data['move_result'] = 'PASS'
        _data['current_room'] = _potential_room
    else:
        _data['move_result'] = 'FAIL'
        _data['current_room'] = _loc

    return _data


def get_room(my_id):
    '''
    This function returns dict for a given room id.
    '''
    return map_data[my_id]


# This will help translate a directional command into an index in map_data[X]['travel']
travel_directions = {'N': 0, 'E': 1, 'S': 2, 'W': 3, 'U': 4, 'D': 5, 'X': 6}

# Map Data is indexed by Room Number then has stuff within
map_data = {
    '1': {
        'name': 'BRIDGE',
        'short_desc': 'YOU ARE ON A BRIDGE',
        'long_desc': 'YOU ARE STANDING ON A LONG BRIDGE THAT LEADS NORTH TO A CASTLE',
        'travel': [2, 0, 0, 0, 0, 0, 0],
        'image': 'castle_mockup.jpg'
    },
    '2': {
        'name': 'GREAT HALL',
        'short_desc': 'YOU ARE IN THE GREAT HALL',
        'long_desc': 'YOU ARE STANDING IN A GREAT HALL, THERE IS A ROOM TO THE EAST. YOU CAN SEE WHAT LOOKS LIKE A BEAR INSIDE.',
        'travel': [0, 3, 1, 0, 4, 0, 0],
        'image': 'castle_great_hall.jpg'
    },
    '3': {
        'name': 'TROPHY ROOM',
        'short_desc': 'YOU ARE IN THE TROPHY ROOM',
        'long_desc': 'YOU ARE STANDING IN THE TROPHY ROOM, THERE IS 9-FOOT GRIZZLY BEAR STANDING ON IT\'S HIND LEGS LOOKING RIGHT AT YOU. LUCKILY YOU QUICKLY REALIZE IT\'S STUFFED.',
        'travel': [0, 0, 0, 2, 0, 5, 0],
        'image': 'trophy_room.jpg'
    },
    '4': {
        'name': 'BELL TOWER',
        'short_desc': 'YOU ARE IN THE BELL TOWER',
        'long_desc': 'YOU HAVE FOUND A WAY TO CLIMB THE WALLS OF THE GREAT HALL AND NOW FIND YOURSELF IN THE BELL TOWER. THERE IS BUT ONE DIRECTION TO GO',
        'travel': [0, 0, 0, 0, 0, 2, 0],
        'image': 'bell_tower.jpg'
    },
    '5': {
        'name': 'DUNGEON',
        'short_desc': 'YOU ARE IN THE DUNGEON',
        'long_desc': 'YOU ARE IN A DIMLY LIT DUNGEON. YOU ARE SURROUNDED BY DOZENS OF BROKEN PINBALL MACHINES.',
        'travel': [0, 0, 0, 0, 3, 0, 0],
        'image': 'dungeon.jpg'
    }
}


obstacles_def = {

    '0':{
        'name': 'DOOR',
        'short_desc': 'DOOR',
        'long_desc': 'DOOR.',
        'pass' : None
    },

    '1':{
        'name': 'LOCKED DOOR',
        'short_desc': 'LOCKED DOOR',
        'long_desc': 'LOCKED DOOR, REQUIRES A KEY TO UNLOCK.',
        'pass' : 4 #skeleton key object id
    },

    '2':{
        'name': 'GOBBLIN',
        'short_desc': 'SKINNY GOBBLIN',
        'long_desc': 'GOBLIN IS BLOCKING THE WAY, HE LOOKS FRAIL.',
        'pass' : 5 #sword
    },

    '3':{
        'name': 'DEAD GOBBLIN',
        'short_desc': 'DEAD SKINNY GOBBLIN',
        'long_desc': 'GOBLIN IS DEAD AND POSES NO THREAT.',
        'pass' : None
    }
}

obstacles = [
    # assigns an obstacle to a room, direction and, obstacle
    # room, direction, (obstable def: initial, secondary)
    # room 1, north door, (goblin, dead goblin)
    [1,1,(2,3)],
]


