FROM ubuntu:18.04

RUN apt-get update && apt-get -y upgrade \
  && apt-get install -y --no-install-recommends \
    git \
    wget \
    g++ \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh \
    && echo "Running $(conda --version)" && \
    conda init bash && \
    . /root/.bashrc && \
    conda update conda

COPY environment.yml environment.yml
RUN conda env create -f environment.yml

COPY templates templates
COPY static static
COPY upload_folder upload_folder
COPY __init__.py __init__.py
COPY flask_app.py flask_app.py
COPY inference.py inference.py


RUN echo "source activate mlops_env" > ~/.bashrc
ENV PATH /opt/conda/envs/mlops_env/bin:$PATH
# RUN pip install gunicorn
EXPOSE 5000
ENTRYPOINT [ "/bin/bash", "-l", "-c" ]
# CMD gunicorn -b 0.0.0.0:5000 flask_app:app
CMD ["python","flask_app.py"]
# CMD ["gunicorn", "--timeout", "1000", "--workers=1","-b", "0.0.0.0:5000","--log-level", "debug", "manage","flask_app.wsgi:app"]