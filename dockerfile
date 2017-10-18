FROM registry.bj.tusimple.ai:5043/service/dataset_backend_base:latest

COPY . /

EXPOSE 5002

RUN pip install -r requirements.txt && \
    pip install gunicorn

CMD gunicorn -c config/dataset-backend.conf app:app
