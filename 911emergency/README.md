**Steps to Run the app**
 - For Windows refer
   - ```http://python.org```
 - For Mac
   - ```pip install virtualenv```
   - To Activate the env
     - ```virtualenv -p /usr/local/bin/python3.6 <project-name>```
     - ### Note ***```if the above step fails make sure python3.6 is installed or check python path using below command```***
     - Run command ```which python```
     - Run command ```source ./<project-name>/bin/activate```
- Now Clone the repo in current directory
  - ```git clone https://github.com/SJSU272LabS17/Project-Team-16.git```
  - ```cd ./Project-Team-16/911emergency/```
- Install the libaries using Pip
  -  ```pip install -r requirements.txt```
- Run the app
  - ```python3.6 app.py```


**Docker steps**
 - '''docker pull manika15/python3.6ubuntu:latest'''
 - '''/root/Project-Team-16/911emergency'''
 - ''' docker-compose up -d'''
 - ''' docker logs <container-id> --follow'''
