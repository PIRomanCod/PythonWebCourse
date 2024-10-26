# HW_Web_8

# Part 1
1. Implemented a script to search for quotes by tag, by author name, or by a set of tags. 
The script executes in an infinite loop and accepts commands in the following format command: 
value using the usual input operator. 
Example:
- name: Steve Martin — find and return a list of all quotes by the author Steve Martin;
- tag:life — find and return a list of quotes for the tag life;
- tags:life,live — find and return a list of quotes with life or live tags (note: no spaces between life, live tags);
- exit — end the execution of the script;
2. Implemented for the name:Steve Martin and tag:life commands the ability 
to write abbreviated search values as name:st and tag:li respectively;
3. Cache the result of the name: and tag: commands using Redis, 
so that when re-requested, the search result is not taken from the MongoDB database, but from the cache;

# Part 2

Writed two scripts: consumer.py and producer.py. 
Using RabbitMQ, organized with the help of queues the simulation of email distribution to contacts.

Using Mongoengine ODM, created a model for the contact. 
The model must include fields: 
- full name, 
- email 
- phone number
- logical field that has a value of False by default
- prefered way of communication (email, phone, sms, etc.)

When the producer.py script is run, 
it generates a certain number of fake contacts and writes them to the database. 
Then queues a RabbitMQ message containing the ObjectID of the generated contact, 
and so on for all generated contacts.

producer.py sends SMS and email contacts to different queues. 
Created two scripts consumer_sms.py and consumer_email.py, 
each of which receives and processes its contacts

The consumer.py script receives a message from the RabbitMQ queue, 
processes it and simulates sending a message by email with a stub function. 
After sending the message, the logical field for the contact must be set to True. 
The script runs constantly waiting for messages from RabbitMQ.
 
