import flask
from startup_name_generator.name_generator import name
from startup_name_generator.name_generator import name_with_description


app = flask.Flask(__name__)


@app.route('/')
def main_page():
    #startup_name = name()
    startup_name, description = name_with_description()
    return flask.render_template('index.html', startup_name=startup_name, description=description)

@app.route('/favicon.ico')
def favicon():
    return flask.send_from_directory('static', 'favicon.ico')

if __name__ == '__main__':
    app.run('0.0.0.0', port=8005, threaded=True)
