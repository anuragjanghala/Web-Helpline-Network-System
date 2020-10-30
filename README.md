# Web-Helpline-Network-System
You have downloaded the directory of the project.

*************************************************************************
*** To download the records of a lab in the ambulance service records ***

1.
- Open the "Labs" directory, go into "lab1" and make the server "Lab1_Server_AS" run
--- To do that, I open a terminal, I go in the "lab1" directory in the terminal and type "Lab1_Server_AS.py".
- The server is now "Ready to receive"

2.
- Now we should make the Ambulance Service Server run
- Go in the "Ambulance_S" directory and make the server "AS_Client_lab1" run
--- To do that, I open a terminal, I go in the "Ambulance_S" directory in the terminal and type "AS_Client_lab1.py".

3.
Now if you go in the "Ambulance_S" directory and in the "Record" directory, you should see that:
	- person1_1.txt, person1_2.txt and person1_3.txt have been downloaded
	- list1.txt has been updated

-> If you now repeat step 2 without closing the lab server, you will receive a message in the Ambulance Service Server 
that says that it is "Uptodate". The files in the Ambulance Service "Record" won't be changed.

-> You can repeat step 1. 2. and 3. for the lab2 and lab3 by:
	- using "lab2" (or "lab3") directory
	- making "Lab2_Server_AS" (or "Lab3_Server_AS") run
	- making "AS_Client_lab2" (or "AS_Client_lab3") run

**************************************************************
*** To make a user send a request to the ambulance service ***

1.
- Open the "Ambulance_S" directory and make the server "AS_Server_User" run
--- To do that, I open a terminal, I go in the "Ambulance_S" directory in the terminal and type "AS_Server_User.py".
- The server is now "Ready to receive"

2.
- Open the "Users" directory, open the "Client" directory and make the server "User_Server" run
--- To do that, I open a terminal, I go in the "Users" then "Client" directory in the terminal and type "User_Server.py".

Now the terminal with the User server is saying "Request state : b'Received'". The user knows his request has been received.
The terminal with the A.S. server is saying "Waiting for you to treat the request".

3.
- Open the "Ambulance_S" directory, there you should see a file named "<addr_of_the_user>_Request_state.txt".
- You may also see a file named "<addr_of_the_user>_X.txt". This will count the time for you to handle the request 
since it has appeared in your directory.
- Open the file "<addr_of_the_user>_Request_state.txt" and replace the "No" by a "yes" or anything with a "y" in it.
- Save this file and close it.

4.
Now on the Client terminal you should read a "Request state : b'Considered'" message. Once it has received this message,
the client will send its me.txt file to introduce himself. The server will receive it and answer with the message "In treatment,
please wait for us to call you". You should be able to read this message on the client terminal (user's server terminal) now.
- Go the "Ambulance_S" directory and open the "Data_current_client.txt" file. You should read :

"
Name = Etienne000
Phonenumber = 01.02.03.04.05
Lab = 1
Numberidentifier = 1
"

It corresponds to the "me.txt" file of the user.
- Close this file.

5. 
- Go to the Ambulance service server terminal. It is aking you: "All associated files closed? :"
- Answer this question by typing anything and press "Enter"
You should now read "Lab data found and now used" on the Ambulance service server terminal. It means that the user requesting for help
has been found in the downloaded lab records.
- Go the "Ambulance_S" directory and open the "Data_current_client.txt" file. You should now read :

"
Name = Etienne000
Tested : Positive
Age : 24ans
Diseases : No known problem 
Lab = 1
Numberidentifier = 1
PhoneNumber = 01.02.03.04.05
"

It corresponds to the "person1_1.txt" file of the records downloaded from the lab.
- Close this file.


-> You can repeat the "request sending" with another client. In order to do that, let the AS_Server_User open and :
	- repeat step 2. to .5
	- use instead of directory "Client", "Client2" (or "Client3")
	- at the end of step 5. with "Client2", you will read : "This user lab file hasnt been found", because the name of the user is corrupted
	- at the end of step 5. with "Client3", you will read : "This user hasnt been in a lab" because the client has no reference about any lab



**************************************************************
*** To download records in the global Server from the labs ***

data in initX.txt (X=1,2,3) (its content changes according to lab records) -> infected : 0 death : 0 recovered : 0
data in reset.txt (its content will untouched) -> infected : 0 death : 0 recovered : 0

other folders (after downloads): labX_client (X=1,2,3) -> contains main client file with their record details file (record.txt)
data in record.txt for example in "lab1" folder -> infected : 2 death : 0 recovered : 0


----------------------------NOW AFTER RUNNING server AND client FILE------------------------------

- terminal 1: $ python3 global_server.py
- terminal 2: $ python3 client_lab.py


firstly,
- enter file name “lab1_record.txt” (always use this name) in server side and press ‘enter’

then,
- enter file name “record.txt” in client side and press ‘enter’

now after this it will create a file “lab1_record.txt” in "global_server" directory and will hold the data extracted from the "lab1" “record.txt” file.

After transferring the data successfully client will disconnect.
Now on terminal with server side it will ask for “record updation” (y/n)

here are two cases->
case 1:  when we want to update the record of lab data and, enter ‘y’ and press ‘enter’ after this it will ask to enter “lab ID” , enter ‘1’ as we are updating the record of lab-1 data
then it update the update data by updating “init1.txt” file.
Data in “init1.txt” -> infected : 2 death : 0 recovered : 0
and along side it will create a “lab1_record.txt” and it will change when lab client record changes and want to update.

case 2 : as now our “init1.txt” is now updated and we want to reset it, then
follows same steps again above case 1 and now you will be asked for updation again and now enter ‘n’ and press ‘enter‘
now it will ask again to confirm to reset lab record if you press ‘n’ then press ‘enter’, here it will cancel reset, and shut down the server, nothing will be changed. But if you enter ‘y’ and then press ‘enter’, then you will come up with this
it will ask for client/lab ID (here say ‘1’ as we want to reset ‘init1.txt’ which is the file for lab 1 client) and ill will reset the “init1.txt” file. Now check “init1.txt” file,
data should be -> infected : 0 death : 0 recovered : 0
which is reseted to inital value

And, now its your choice to delete “lab1_record.txt” coz it wont affect the other files as it will be created again if when you again update record data of lab 1 client (try to use same name so that it wont create to many duplicate files with different names). 
If you dont want “lab1_record.txt” you have to delete it manually.

NOTE : Same steps and instructions for other client files as well but only differ in naming at some places
