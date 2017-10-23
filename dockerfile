FROM registry.bj.tusimple.ai:5043/service/dataset_backend_base:latest

COPY . /

EXPOSE 5002

RUN pip install -r requirements.txt && \
    pip install gunicorn && \
    echo "bind = '0.0.0.0:5002'\nworkers = 17" > ./config/dataset-backend.conf && \
    mkdir /mnt/truenas

VOLUME [ "/mnt/truenas/" ]

CMD gunicorn -c config/dataset-backend.conf app:app
