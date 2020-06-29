#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from tcp_latency import measure_latency
import flask
import speedtest
from hurry.filesize import size, si

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/metrics', methods=['GET'])
def metrics():
    st = speedtest.Speedtest()
    download = size(st.download(), system=si)
    upload = size(st.upload(), system=si)
    servernames = []
    st.get_servers(servernames)
    latency = st.results.ping

    print(latency)
    print(download)
    print(upload)
    print(st.results.ping)

    return (
        "python_network_latency_speedtest " + str(latency) +
        "\npython_network_upload_speedtest " + str(upload) +
        "\npython_network_download_speedtest " + str(download) +
        "\n"
    )


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run(host='0.0.0.0', port=8000)

