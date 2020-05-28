# py_ver == "3.6.9"
import flask


app = flask.Flask(__name__)


@app.route("/colour")
def set_colour():
    return """
            <html>
            <script>
            window.changeColour = function() {
            document.body.style.backgroundColor = location.hash.replace('#', '');
            document.getElementsByName("text")[0].innerHTML = decodeURI(location.hash.replace('#', ''));
            }
            </script>
            <body>
            <p name="text"></p>
            <div style="height:100vh" onmousemove=changeColour()></div>
            </body>
            </html>
            """


@app.route('/send_proxy_request')
def send_proxy_request():
    return """
            <html>
                <title>What to GET</title>
                <body>
                    <form action="/proxy_get">
                        Enter URL: <input name="url" type="text" />
                        <input name="submit" type="submit">
                    </form>
                </body>
            </html>
"""


import requests


@app.route('/proxy_get')
def proxy_get():
    url = flask.request.args.get('url')
    if url.startswith(('http://', 'https://')):
        result = requests.get(url)
        return "%s" % result.text
    else:
        return flask.redirect('/send_proxy_request')


if __name__ == '__main__':
    app.run()
