FROM custom

RUN DISPLAY=:99   

#passi all'utente 
USER seluser
RUN alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'

#lanci il server con il display davanti
CMD ["/bin/xvfb-run", "java", "-jar", "/opt/selenium/standalone.jar"]
