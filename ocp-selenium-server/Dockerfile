FROM custom

#ENV DISPLAY=:99   

#passi all'utente 
USER seluser
#lanci il server con il display davanti
CMD ["DISPLAY=", ":99", "xvfb-run", "java", "-jar", "/opt/selenium/standalone.jar"]
