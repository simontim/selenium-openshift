FROM registry.access.redhat.com/openshift3/ose

MAINTAINER simontim <simone.mastrodonato@telecomitalia.it>

EXPOSE 4444 5555

RUN yum update -y
#installi browser display 
RUN yum install -y firefox Xvfb wget tar
#driver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz && \
    tar -xzvf geckodriver-v0.19.1-linux64.tar.gz && \
    mv geckodriver /usr/bin && \
    rm geckodriver-v0.19.1-linux64.tar.gz

#scarichi selenium server 3.81

#assegni i permessi al'utente 1001
USER 1001
#lanci il server con il display davanti
CMD ["/bin/bash"]
