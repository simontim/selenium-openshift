FROM centos:7

MAINTAINER simontim <simone.mastrodonato@telecomitalia.it>

EXPOSE 4444 5555
#utente
RUN useradd seluser --shell /bin/bash --create-home && \
    mkdir -p /opt/selenium && \
    chown seluser:seluser /opt/selenium
#aggiornamento
#RUN yum update -y

#browser e utility (provare solo openjdk-8-jre-headless)
RUN yum install -y firefox wget tar java-1.8.0-openjdk 

#installi il display
RUN wget http://vault.centos.org/6.2/os/x86_64/Packages/xorg-x11-server-Xvfb-1.10.4-6.el6.x86_64.rpm && \
    yum localinstall -y xorg-x11-server-Xvfb-1.10.4-6.el6.x86_64.rpm && \
    rm -f xorg-x11-server-Xvfb-1.10.4-6.el6.x86_64.rpm

#installi i driver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz && \
    tar -xzvf geckodriver-v0.19.1-linux64.tar.gz && \
    mv geckodriver /usr/bin && \
    rm geckodriver-v0.19.1-linux64.tar.gz

#scarichi selenium server 3.9
RUN wget http://selenium-release.storage.googleapis.com/3.9/selenium-server-standalone-3.9.0.jar -O /opt/selenium/standalone.jar && \
    chmod 777 /opt/selenium/standalone.jar
    
#passi all'utente 
USER seluser
#lanci il server con il display davanti
CMD ["java", "-jar", "/opt/selenium/standalone.jar"]
