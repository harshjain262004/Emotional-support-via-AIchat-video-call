EMU-AIchat&VideoCall

Description
This repository is the winning project prototype of IEEE CS MUJ Hackerzstreet 2.0. Team TechNormies It aims for user to signup/login and talk his/her emotional problems to a chatbot. The chat reply mechanism is 
backed by Google Gemini 1.0-Pro API, and is preprompted to act like a therapist. Moreover, addtional video calling service with a therapist is made available more Red category issues. Login/signup data is stored in
the MySQL database chatbot, table userdata, analysing chat and patient issue is stored in table keywords. Analysing of the chat is also done by Gemini 1.0-pro. 

Installation
Install the Master branch Zip file directly from the repository page.
Make sure to install all the required classes and modeules of python as showed in requirement.txt 
RUN: python -m pip install requirements.txt
(assuming python and pip are installed)

Configuration
Create a api key for google Gemini 1.0-pro from Google AI studio and place it in Bot.py
A Zego Cloud API secretserver key for video calling service.
create two tables in a MySQL database named userdata(pk user_id int, username varchar, passkey varchar) and keywords(fk user_id from userdata, keywords varchar)
RUN: python app.py

Live Demo:
https://drive.google.com/drive/folders/1e1wdW-JQb0_BmbA7sxiqn6ggbD8sY5jQ?usp=sharing
