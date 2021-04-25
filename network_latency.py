#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from flask import Flask
import speedtest
from hurry.filesize import size, si

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/metrics', methods=['GET'])
def metrics():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    download_speed = s.download()
    upload_speed = s.upload()
    ping_speed = str (s.results.ping)
    return '''
        python_network_latency_speedtest {ping}</br>
        python_network_upload_speedtest {upload} </br>
        python_network_download_speedtest {download}
        '''.format(upload=upload_speed, download=download_speed, ping=ping_speed)


@app.route('/', methods=['GET'])
def root():

    return '''
        <html>
            <head>
                <title>Network Stats Exporter</title>
            <head>
            <body>
                <h1>Network Stats Exporter</h1>
                <a href="./metrics">Metrics</a>
                <hr>
                <h3> Python application written in order to export upload, download and ping speeds </br>
                Author <b> John Stilia </b> </h3>
            </body>
        </html>
        '''


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run(host='0.0.0.0', port=8000)
