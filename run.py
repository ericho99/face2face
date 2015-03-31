#!flask/bin/python
from app import app
import sys
from testing import face2faceTest

# import os
# from flask import Flask

if __name__ == '__main__':
    cmd_args = sys.argv
    if len(cmd_args) > 1 and cmd_args[1] == "test":
        #do a test; facilitated by a pass right now
        pass
    app.run(debug=True)
    