FROM centos:7

MAINTAINER simontim <simone.mastrodonato@telecomitalia.it>

#utente
RUN useradd --user-group --shell /bin/false --create-home seluser
    
#aggiornamento
RUN yum update -y

#browser e utility (da provare openjdk-8-jre-headless)
RUN yum install -y firefox wget tar java-1.8.0-openjdk which

#installi il display
RUN yum install -y Xvfb

#installi i driver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz && \
    tar -xzvf geckodriver-v0.19.1-linux64.tar.gz && \
    mv geckodriver /usr/bin && \
    rm geckodriver-v0.19.1-linux64.tar.gz

#scarichi selenium server 3.9
RUN wget http://selenium-release.storage.googleapis.com/3.9/selenium-server-standalone-3.9.0.jar -O /home/seluser/standalone.jar && \
    chmod 777 /home/seluser/standalone.jar && \
    chown -R seluser:0 /home/seluser && \
    chgrp -R 0 /home

EXPOSE 4444 5555

USER seluser

ENV DISPLAY=:99

CMD ["xvfb-run", "java", "-jar", "/home/seluser/standalone.jar"]
