'''
This module defines the object sin the game world
'''
# This will help translate a directional command into an index in map_data[X]['travel']
travel_directions = {'N': 0, 'E': 1, 'S': 2, 'W': 3, 'U': 4, 'D': 5, 'X': 6}

# Map Data is indexed by Room Number and has stuff within
game_map = {
    '1': {
        'name': 'BRIDGE',
        'short_desc': 'YOU ARE ON A BRIDGE',
        'long_desc': 'YOU ARE STANDING ON A LONG BRIDGE THAT LEADS NORTH TO A CASTLE.',
        'travel': [2, 0, 0, 0, 0, 0, 0],
        'bonus_points': 0,
        'image' : 'castle_mockup.jpg'
    },
    '2': {
        'name': 'GREAT HALL',
        'short_desc': 'YOU ARE IN THE GREAT HALL',
        'long_desc': 'YOU ARE STANDING IN A GREAT HALL, THERE IS A ROOM TO THE EAST. YOU CAN SEE WHAT LOOKS LIKE A BEAR INSIDE.',
        'travel': [0, 3, 1, 6, 4, 0, 0],
        'bonus_points': 0,
        'image' : 'great_hall.jpg'
    },
    '3': {
        'name': 'TROPHY ROOM',
        'short_desc': 'YOU ARE IN THE TROPHY ROOM',
        'long_desc': 'YOU ARE STANDING IN THE TROPHY ROOM, THERE IS 9-FOOT GRIZZLY BEAR STANDING ON IT\'S HIND LEGS LOOKING RIGHT AT YOU. LUCKILY YOU QUICKLY REALIZE IT\'S STUFFED.',
        'travel': [0, 0, 0, 2, 0, 5, 0],
        'bonus_points': 0,
        'image': 'trophy_room.jpg'
    },
    '4': {
        'name': 'BELL TOWER',
        'short_desc': 'YOU ARE IN THE BELL TOWER',
        'long_desc': 'YOU HAVE FOUND A WAY TO CLIMB THE WALLS OF THE GREAT HALL AND NOW FIND YOURSELF IN THE BELL TOWER. THERE IS BUT ONE DIRECTION TO GO.',
        'travel': [0, 0, 0, 0, 0, 2, 0],
        'bonus_points': 25,
        'image':'bell_tower.jpg'
    },
    '5': {
        'name': 'DUNGEON',
        'short_desc': 'YOU ARE IN THE DUNGEON',
        'long_desc': 'YOU ARE IN A DIMLY LIT DUNGEON. YOU ARE SURROUNDED BY DOZENS OF BROKEN PINBALL MACHINES.',
        'travel': [0, 0, 0, 0, 3, 0, 0],
        'bonus_points': -100,
        'image':'dungeon.jpg'
    },
    '6': {
        'name': 'LOUNGE',
        'short_desc': 'YOU ARE IN THE PALACE LOUNGE',
        'long_desc': 'YOU ARE IN THE PALACE LOUNGE. YOU HEAR A SITAR PLAYING.',
        'travel': [0, 2, 0, 0, 0, 0, 0],
        'bonus_points': 0,
        'image':'lounge.jpg'
    }
}


obstacles = {
    '1': {
        'name': 'STEEL DOOR',
        'short_desc': 'LOCKED STEEL DOOR',
        'long_desc': 'THE PASSAGE IS BLOCKED BY A HEAVY STEEL DOOR',
        'defeated_by': [1],  # Object ID that will overcome this obstacle
        'replaced_by': [0]  # Object is not replaced, effectively disappears from gameplay
    },
    '2': {
        'name': 'WOOD DOOR',
        'short_desc': 'LOCKED WOODEN DOOR',
        'long_desc': 'THE PASSAGE IS BLOCKED BY A VERY HEAVY WOODEN DOOR',
        'defeated_by': [1, 2],
        'replaced_by': [0]
    },
    '3': {
        'name': 'DRAGON',
        'short_desc': 'LARGE DRAGON',
        'long_desc': 'A FIRE-BREATHING DRAGON, VERY MENACING AND VERY DEADLY',
        'defeated_by': [2, 3],   # Object IDs that will overcome this obstacle
        'replaced_by': [3]  # Object that is swapped in, once obstacle is defeated
    },
    '4': {
        'name': 'DEAD DRAGON',
        'short_desc': 'LARGE DEAD DRAGON',
        'long_desc': 'LIES THE DEAD BODY OF A LARGE DRAGON',
        'defeated_by': [0],  # Object is simply present in gameplay, need not be defeated
        'replaced_by': [(4, 10)]  # Object that is swapped in after second parameter of turns
    },
    '5': {
        'name': 'ROTTING CARCASS ',
        'short_desc': 'LARGE ROTTING CARCASS ',
        'long_desc': 'LIES THE ROTTING CARCASS OF WHAT APPEARS TO HAVE BEEN A LARGE DRAGON',
        'defeated_by': [0],
        'replaced_by': [-1]  # Indicates it is still in gameplay, and will remain in this state for duration
    }
}


objects = {
    '1': {
        'name': 'WOODEN KEY',
        'description': 'A WOODEN KEY CARVED FROM ROCK MAPLE, THE CRAFTSMANSHIP IS SUBLIME',
        'useful_on': [2],  # Object ID(s) here
        'reusable': True
    },
    '2': {
        'name': 'SKELETON KEY',
        'description': 'A SKELETON KEY THAT IS SHAPED LIKE AN ACTUAL HUMAN SKELETON (ONLY MUCH SMALLER)',
        'useful_on': [1, 2],  # Object ID(s) here
        'reusable': True
    },
    '3': {
        'name': 'LONG SWORD',
        'description': 'A LONG SWORD FORGED FROM VALYRIAN STEEL AND HAS AN EXCEPTIONALLY KEEN EDGE',
        'used_on': [3],
        'reusable': True
    },
    '4': {
        'name': 'BATTLE AXE',
        'description': 'A FORMIDABLE BATTLE AXE WITH A DOUBLE EDGED BLADE OF REGULAR STEEL (NOT THAT VALYRIAN STUFF)',
        'used_on': [3],
        'reusable': True
    },
    '5': {
        'name': 'HAM SANDWICH',
        'description': 'A HAM ON RYE WITH LETTUCE, TOMATO AND A MUSTARD-LIKE SPREAD. LOOKS DELICIOUS',
        'used_on': [-1],  # -1 Represents the player? Maybe?
        'reusable': False
    }
}
