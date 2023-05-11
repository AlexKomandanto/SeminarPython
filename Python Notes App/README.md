# Intermediate test
---
### Job information
---
Includes an assignment:
"Notes application" - which is
runs in the Python programming language 

---

### Project Information :
* You need to write a project that contains functionality for working with notes.
* The program should be able to create a note, save it, read a list of notes, edit a note, delete a note.
* To submit your project, you need to create a separate public
repository (Github, gitlub, or Bitbucket). Develop in this repository, and use the change request pool.
* The program should run and work, there should be no errors during the execution of the program.
### Assignment
* To implement a console application for notes, with saving, reading, adding, editing and deleting notes. 
* The note must contain an identifier, title, note body and the date/time the note was created or last modified. The notes must be saved in
json or csv format (it is recommended to separate the fields with a semicolon).
* The implementation of the user interface can be done by the student
do as he pleases, you can do as parameters to run the program (command, data), you can do as a request for a command from the console followed by data entry, somehow else, at the discretion of the student.
* For example:
    *python notes.py add --title* "new note "*-msg* "body of new note
* Or so:
    *python main.py*
    ---
    Enter the command: *add*
    ---
    Enter the title of the note: *new note*
    ---
    Enter the body of the note: *body of the new note*
    ---
    *The note has been successfully saved.*

* When reading the list of notes, implement filtering by date.

---
## **Project implementation**
## Alexei Komendantov ##
---
### General information :
1. A README.md file was created to describe the project;
2. **IMPORTANT!!!** As a project, the database was chosen - **which is more
relevant and can be used in reality and shown in job searches**
3. Database fields (search by them is implemented)
    - ID - is generated randomly
    - name - to be set
    - last name - to be set
    - phone number - set 
    - email - operators
4. Implemented :
    - show all records in the database
    - add a new entry
    - changing an existing record
    - record deletion
5. Implemented the custom menu :

<image src="11.png">

6. Examples of work with the database:
<image src="12.png">
<image src="13.png">


7. The phonebook.log file is created to record the processed commands
8. For training purposes, a database of 20 people is created,
which can be edited
9. During operation, a csv database is created and deleted 
after work is complete. 


