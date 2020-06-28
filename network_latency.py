#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from tcp_latency import measure_latency
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/metrics', methods=['GET'])
def metrics():
    google_latency = measure_latency(host='google.com')
    return "python_network_latency_google {}\n".format(google_latency[0])


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run(host='0.0.0.0', port=8000)

