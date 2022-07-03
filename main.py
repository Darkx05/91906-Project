# imports
from flask import render_template
from website import app_creation

app = app_creation()

# this allows to run the flask file directly
if __name__ == '__main__':
    app.run(debug=True)
