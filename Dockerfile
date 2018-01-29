FROM registry.access.redhat.com/openshift3/jenkins-2-rhel7
USER root
#-------------------#
# Selenium          #
#-------------------#

RUN curl https://bootstrap.pypa.io/get-pip.py -o /home/get-pip.py && \
    python /home/get-pip.py && \
    pip install virtualenv && \
    pip install virtualenvwrapper &&  \
    pip install selenium && \
    yum install -y wget

#-------------------#
# Driver            #
#-------------------#

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz && \
    tar -xzvf geckodriver-v0.19.1-linux64.tar.gz && \
    mv geckodriver /usr/bin && \
    rm geckodriver-v0.19.1-linux64.tar.gz
    
RUN wget http://ftp.mozilla.org/pub/firefox/releases/57.0/linux-x86_64/en-US/firefox-57.0.tar.bz2 && \
    tar xvjf firefox-57.0.tar.bz2 && \
    ln -s /firefox/firefox /usr/bin/firefox

USER 1001

CMD ["/usr/libexec/s2i/run"]
