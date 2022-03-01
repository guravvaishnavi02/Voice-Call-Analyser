# Voice Call Analyzer

Not Complete -- Files Omitted to prevent plagrism

## Idea:
To design a platform where a user can see insights from uploaded call records by utilizing ML/DL facilitated functionalities such as speech recognition, classification, speech diarization etc.

Find our project here: http://34.122.214.22:8000/ \
Presentation for Hacksprint v3.0: https://docs.google.com/presentation/d/1EjfcQZh3_JjIkSPGFT-1_bOg5zB9Ruh2JOlkO8ahkBY/edit?usp=sharing

## Functionalities:
- Upload a call recording
- Play uploaded call record
- Calculates number of speakers in the call
- Display 5 most used words throughout the conversation
- Visualized representations for:
  - Voice activity detection 
  - Multiple speaker voice separation
  - Speaker's speaking duration
  - Overall emotions recorded throughout the call
  - Speaker-wise emotion throughout the call
  - Comparative visual represenation of duration of emotions of individual speaker 

## Highlight Features:
- Easy-to-use & attractive User Interface
- Data privacy & security : all user data including uploaded files and analysis is deleted once user closes the website
- Multiple ethnicity supporting ML model

## Procedure- Using the platform
1) After going to http://34.122.214.22:8000/, welcome page will be displayed.
2) By scrolling down, user will get option to upload the call record(audio) file.
3) NOTE that the file must be of .wav format. User will be requested to upload file multiple times till correct format file is not uploaded.
4) Once user uploads the file, they will be directed to a loading page displaying message of successful file uploadation and will get a prompt to begin with the Analysis of the record.
5) User will have to wait on the loading page itself till the analysis is complete. Time required for analysis might vary depending on file size, internet connectivity and hardware details.
6) Once the analysis is complete, user will be automatically directed to an interactive dashboard where all the insights & above mentioned functionalities will be displayed.

## Instructions for Running Application on Local Host
**If the above mentioned URL is not working, follow following steps to run the application on local host.**
1) Clone this repository on local machine *with python installed*.
2) Go to command prompt and traverse to the directory created for this repository.
3) Execute following commands sequentially
  ```
  python -m venv env
  ```
  ```
  env\Scripts\activate.bat
  ```
  ```
  pip install -r requirements.txt
  ```
  ```
  cd project
  ```
  ```
  python manage.py runserver
  ```
4) Now open your browser and visit http://127.0.0.1:8000/
5) In no time, you will be welcomed by our Call Analyzer homepage.
Now you can start uploading and analyzing!

## Technical details:
### Technologies used:
- Frontend: HTML,CSS, JavaScript
- Backend: Django
- Programming Language: Python
### Algorithm details:
- Malaya-speech module: ML model used for emotions analysis and speech diarization
- speech-recognition library of Python for speech-to-text conversation
- Training dataset for emotions analysis & speech diarization: vggvox_v2
- Google's recognition api for words detection.
