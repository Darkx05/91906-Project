# this file allows the full code to run

from website import app_creation

app = app_creation()

if __name__ == '__main__':
    app.run(debug=True)
