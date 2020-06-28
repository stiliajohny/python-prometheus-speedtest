FROM python:3
ADD ./network_latency.py /
RUN pip install tcp_latency flask 
CMD [ "python", "./network_latency.py" ] ]
EXPOSE 8000/tcp
