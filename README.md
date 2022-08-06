# NotePad_Microservice
This is a project meant to demostrate a microservice

## Communication Contract
This project utilizes Zeromq as a communication pipeline

## Request Data
To request data one must use the gui and select the "Write to" option. From there, you can use another program (client program) that utilizes Zeromq to write a message to
the program and the GUI will display that message.
![Request](https://user-images.githubusercontent.com/76986911/180889387-092a1747-acf2-4c71-8ad8-790b9044bf0b.gif)

## Receive Data
When the program/server recieves the request it will send back a message received message to the client to let the client know that the message was indeed received. 

## UML 
![Notepad UML Part 2](https://user-images.githubusercontent.com/76986911/183225598-93874076-5641-4595-86d6-87b5e5aa919a.png)
