FROM custom

RUN DISPLAY=:99   

#passi all'utente 
USER seluser
#lanci il server con il display davanti
CMD ["/bin/xvfb-run", "java", "-jar", "/opt/selenium/standalone.jar"]
