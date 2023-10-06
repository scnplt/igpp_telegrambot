import os
import requests

from flask import Flask
from constants import *

app = Flask(__name__)

@app.route('/username/<username>')
def get_pp_hd_link(username):
    req_url = "{}/?username={}".format(BASE_URL, username)
    req = requests.get(req_url, headers=HEADERS)

    if req.status_code != 200:
        return 'Error: {}'.format(req.status_code)

    return req.json()['data']['user']['profile_pic_url_hd']

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
