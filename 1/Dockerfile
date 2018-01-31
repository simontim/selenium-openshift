FROM custom
USER root

RUN wget http://vault.centos.org/6.2/os/x86_64/Packages/xorg-x11-server-Xvfb-1.10.4-6.el6.x86_64.rpm && \
    yum localinstall -y xorg-x11-server-Xvfb-1.10.4-6.el6.x86_64.rpm

USER 1001
CMD ["/usr/libexec/s2i/run"]
