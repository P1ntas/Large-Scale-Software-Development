FROM python:3.8.3-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN mkdir -p usr/src/dinasore-ua

WORKDIR /usr/src/dinasore-ua


COPY communication ./communication
COPY opc_ua ./opc_ua
COPY core ./core
COPY data_model_fboot ./data_model_fboot
COPY tests ./tests
COPY requirements.txt ./
COPY resources ./resources

RUN pip3 install -r requirements.txt

# Make the ports available to the world outside this container
EXPOSE 61499 4840

#RUN python tests/__init__.py

CMD ["python", "core/main.py"]
