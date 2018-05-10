FROM registry.access.redhat.com/openshift3/jenkins-2-rhel7
USER root

#-----------------------#
# Strumenti di sistema  #
#-----------------------#

RUN curl https://bootstrap.pypa.io/get-pip.py -o /home/get-pip.py && \
    python /home/get-pip.py && \
    pip install virtualenv && \
    pip install virtualenvwrapper

RUN yum install wget

#installazione sonar-scanner senza plug-in
RUN mkdir /opt/sonar-scanner

#RUN wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.1.0.1141-linux.zip


#installazione plug-in sonar-scanner 
#RUN touch sonar.txt && \
#   echo sonar:2.7.1 >> sonar.txt
#RUN /usr/local/bin/install-plugins.sh sonar.txt

# https://github.com/openshift/jenkins/blob/master/2/contrib/jenkins/install-plugins.sh
# The format of 'plugins.txt. is:
#
# pluginId:pluginVersion

USER 1001

CMD ["/usr/libexec/s2i/run"]
