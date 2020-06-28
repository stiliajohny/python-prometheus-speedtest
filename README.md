# Prometheus Network Latency check

Basic Script to monitor latency towards the google.com website.
It outputs a Prometheus compatible output
run `curl localhost:8000/metrics` after following the instructions below


## How to Use
- Activate the virtualenv ( `source ./bin/activate`)
- Run the script `python ./network_latency.py`
- to get results `curl localhost:8000`
- To build the Container run
  - `docker build -t CONTAINER_NAME:vX.Y ./Dockerfile`
- To Run the container
  - `docker run -p 8000:8000/tcp ./CONTAINERNAME:vX.Y`

---

### Grafana example ( using Prometheus for DataStore )
![grafana example](./assets/grafana.png)
