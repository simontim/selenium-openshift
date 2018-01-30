FROM custom
USER root

#RUN wget bzip.org/1.0.3/bzip2-1.0.3.tar.gz
#RUN yum install -y bzip2
RUN cd / && \
    tar xvjf firefox-57.0.tar.bz2

#RUN yum update -y && \
 #   yum install -y make

USER 1001
CMD ["/usr/libexec/s2i/run"]
