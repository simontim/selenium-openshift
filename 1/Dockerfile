FROM custom
USER root

RUN cd / && \
    tar xvjf firefox-57.0.tar.bz2

USER 1001
CMD ["/usr/libexec/s2i/run"]
