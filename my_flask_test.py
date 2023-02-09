'''
Flask file to define routes
'''
import json
from flask import Flask

import adventure_api.navigation

app = Flask(__name__)

@app.route("/")
def hello_world():
    '''
    testing main route
    '''
    return "<p>Hello, World!</p>"

@app.route("/adventure/<myparam>")
def adventure(myparam):
    '''
    main navigation route
    '''
    myparam_arr = myparam.split(',')
    result = adventure_api.navigation.move_action(int(myparam_arr[0]), str(myparam_arr[1]))
    return json.dumps(result)

@app.route("/room/<room_id>")
def room(room_id):
    '''
    route to get room details fo rthe current room
    '''
    result = adventure_api.navigation.get_room(str(room_id))
    return json.dumps(result)

@app.route('/static')
def static_file(path):
    '''
    route for all static files like html, css, js
    '''
    return app.send_static_file(path)

