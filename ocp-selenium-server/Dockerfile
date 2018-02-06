FROM registry.access.redhat.com/openshift3/ose

MAINTAINER simontim <simone.mastrodonato@telecomitalia.it>

EXPOSE 4444 5555

#aggiorna il sistema
RUN yum update -y

#installi browser e utility
RUN yum install -y firefox wget tar openjdk-7-jre-headless 

#installi il display
RUN wget http://vault.centos.org/6.2/os/x86_64/Packages/xorg-x11-server-Xvfb-1.10.4-6.el6.x86_64.rpm && \
    yum localinstall -y xorg-x11-server-Xvfb-1.10.4-6.el6.x86_64.rpm && \
    rm -f xorg-x11-server-Xvfb-1.10.4-6.el6.x86_64.rpm

#installi i driver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz && \
    tar -xzvf geckodriver-v0.19.1-linux64.tar.gz && \
    mv geckodriver /usr/bin && \
    rm geckodriver-v0.19.1-linux64.tar.gz

#scarichi selenium server 3.81
RUN wget http://selenium-release.storage.googleapis.com/3.9/selenium-server-standalone-3.9.0.jar && \
    mv selenium-server-standalone-3.9.0.jar /usr/bin && \
    rm selenium-server-standalone-3.9.0.jar
#assegni i permessi al'utente 1001
USER 1001
#lanci il server con il display davanti
CMD ["java", "-jar", "selenium-server-standalone-3.9.0.jar"]
