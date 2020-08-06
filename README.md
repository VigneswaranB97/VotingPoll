# VotingPoll

Installation steps:
  1) Download soln.zip file that is submitted and unzip it.
  2) Install Python
  3) pip install -r requirements.txt
  4) python manage.py createsuperuser
      3.1) This will ask for username, password for admin
  5) python manage.py runserver
      4.1) <ip>:<port> will be shown in the console

Important notes:
  1) ip:port/admin => mainpoll, users,  
  2) DON'T USE POLLS, candidates should only be added in mainpolls -> candidates 
  3) Login needed for voting
  4) Edit, Update can be done by candidates
  5) users can vote
  6) admin can add, edit, delete candidate
  
  
