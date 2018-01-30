FROM custom
USER root

RUN yum install -y Xvfb

USER 1001
CMD ["/usr/libexec/s2i/run"]
