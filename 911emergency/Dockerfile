FROM manika15/python3.6ubuntu
# Update aptitude with new repo
RUN apt-get update
# Install software
RUN apt-get install git -y
RUN git clone https://github.com/SJSU272LabS17/Project-Team-16.git
WORKDIR ./Project-Team-16/911emergency
RUN /usr/local/bin/pip3.6 install -r requirements.txt
CMD ["/usr/local/bin/python3.6", "app.py"]
EXPOSE 80

