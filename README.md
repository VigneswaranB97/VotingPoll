# VotingPoll

Installation steps:
  1) Download soln.zip file that is submitted and unzip it.
  2) Install Python
  3) Open command prompt/anaconda prompt and go to the soln folder.
  4) pip install -r requirements.txt 
  5) Inside hack_poll type following cmds
  6) python manage.py createsuperuser
      6.1) This will ask for username, password for admin
  7) python manage.py runserver
      7.1) ip:port will be shown in the console

Important notes:
  1) ip:port/admin => mainpoll, users,  
  2) DON'T USE POLLS, candidates should only be added in mainpolls -> candidates 
  3) Login needed for voting (Registration can be done)
  4) Edit, Update can be done by candidates
  5) users can vote
  6) admin can add, edit, delete candidate
  
  
