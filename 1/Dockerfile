FROM custom
USER root

RUN yum install -y xorg-X11-server-Xvfb

USER 1001
CMD ["/usr/libexec/s2i/run"]
