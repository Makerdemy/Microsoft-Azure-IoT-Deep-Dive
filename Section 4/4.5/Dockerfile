FROM arm32v7/python:2

COPY PI4 IoT Edge Gateway ./

RUN pip install --no-cache-dir rpi.gpio

CMD [ "python", "./PI4 IoT Edge Gateway" ]
