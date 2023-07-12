import flask
from startup_name_generator.name_generator import name
from werkzeug.middleware.proxy_fix import ProxyFix


app = flask.Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)


@app.route('/')
def main_page():
    startup_name = name()
    return flask.render_template('index.html', startup_name=startup_name)

@app.route('/favicon.ico')
def favicon():
    return flask.send_from_directory('static', 'favicon.ico')

if __name__ == '__main__':
    app.run('127.0.0.1', port=8005, threaded=True)
