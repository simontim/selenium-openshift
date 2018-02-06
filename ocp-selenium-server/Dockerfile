FROM custom

#ENV DISPLAY=:99   
RUN Xvfb :99 &
#passi all'utente 
USER seluser
#lanci il server con il display davanti
CMD ["java", "-jar", "/opt/selenium/standalone.jar"]
