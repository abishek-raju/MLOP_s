FROM ubuntu:18.04
RUN apt-get update -y \
    && apt-get install -y python3-pip python3.7 build-essential \
    && pip3 install --upgrade pip
COPY requirements.txt requirements.txt
COPY templates templates
RUN pip install -r requirements.txt
EXPOSE 5000
COPY flask_app.py flask_app.py
COPY inference.py inference.py
COPY app.py app.py
RUN mkdir upload_folder
RUN mkdir static
ENTRYPOINT ["python3"]
CMD ["flask_app.py"]
# CMD ["app.py"]
# CMD gunicorn flask_app:app