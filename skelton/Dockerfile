FROM docker-dev.artifactory.tmna-devops.com/tdspds/tdspds-mlops-wandb:0.1.0-feature-2073-v1.13

WORKDIR /opt/ml/code

COPY conf/. /opt/ml/code/conf/.
RUN chmod +x /opt/ml/code/conf/*
 
COPY src/. /opt/ml/code/src/
RUN chmod +x /opt/ml/code/src/*

COPY utilities/. /opt/ml/code/utilities/

COPY requirements.txt requirements.txt
RUN chmod 755 /opt/ml/code/requirements.txt
RUN pip install  -r requirements.txt

ENTRYPOINT ["/bin/sh", "src/main.sh"]
