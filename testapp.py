from flask import Flask, request, abort, g, render_template


app = Flask(__name__)
app.config.update(
    VALID_HOSTS=['svnstats', 'crashdamage']
)


@app.before_request
def where_am_i_from():
    hostname = request.host.split('.')[0]
    if hostname not in app.config['VALID_HOSTS']:
        abort(404)
    g.host = hostname


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
