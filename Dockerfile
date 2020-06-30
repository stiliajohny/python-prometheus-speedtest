FROM python:3.8-slim-buster

# Copy script over
COPY ./network_latency.py /
# Install dependencies:
COPY ./requiments.txt /
RUN pip install -r requirements.txt

CMD [ "python", "./network_latency.py" ] ]
EXPOSE 8000/tcp
