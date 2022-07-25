# NotePad_Microservice
This is a project meant to demostrate a microservice

## Communication Contract
This project utilizes Zeromq as a communication pipeline

## Request Data
To request data one must use the gui and select the "Write to" option. From there, you can use another program (client program) that utilizes Zeromq to write a message to
the program and the GUI will display that message.

## Receive Data
When the program/server recieves the request it will send back a message received message to the client to let the client know that the message was indeed received. 
