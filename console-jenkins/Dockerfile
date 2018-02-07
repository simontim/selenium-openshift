FROM registry.access.redhat.com/openshift3/jenkins-2-rhel7
USER root

#-----------------------#
# Strumenti di sistema  #
#-----------------------#

RUN curl https://bootstrap.pypa.io/get-pip.py -o /home/get-pip.py && \
    python /home/get-pip.py && \
    pip install virtualenv && \
    pip install virtualenvwrapper &&  \
    yum install -y wget && \
    yum install -y bzip2

USER 1001

CMD ["/usr/libexec/s2i/run"]
