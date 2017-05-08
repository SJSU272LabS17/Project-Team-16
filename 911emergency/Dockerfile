FROM ubuntu_python3.6
# Update aptitude with new repo
RUN apt-get update
# Install software
RUN apt-get install git -y
RUN /usr/local/bin/pip3.6 install -r requirements.txt
CMD ["/usr/local/bin/python3.6", "app.py"]
EXPOSE 80
