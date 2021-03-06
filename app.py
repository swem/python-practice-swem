import os
from flask import Flask
import pttdata

app = Flask(__name__)

@app.route('/')
def hello():
    return 'ptt online user: '+str(pttdata.getOnlineUserNumber())

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
