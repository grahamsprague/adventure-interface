'''
This module allows navigation
'''
import adventure_api.game_data

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

    _potential_room = adventure_api.game_data.game_map[str(_loc)]['travel'][adventure_api.game_data.travel_directions[str(_dir)]]

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
    return adventure_api.game_data.game_map[my_id]