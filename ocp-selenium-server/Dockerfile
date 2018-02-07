FROM custom

ENV DISPLAY=:99
RUN yum install -y which.x86_64

#passi all'utente 

#RUN alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'
#USER seluser
#lanci il server con il display davanti "/bin/xvfb-run"
CMD ["xvfb-run", "java", "-jar", "/opt/selenium/standalone.jar"]
