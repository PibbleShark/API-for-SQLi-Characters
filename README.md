# Simple API for SQLi Character Detection
 Simple API for SQLi Character Detection

simple API converts JSON payload to a python string and searches it for a possible SQL injection character.

Because there are many possible SQL injections I have used a list of characters to search for based on commonly used
injections.  This approach allows for easy debugging, viewing, and editing of the possible characters.  It also allows
the potential for adding possible SQL commands at a later point.  A simple modification can also be made to use
characters from a JSON or CSV data format rather than a python list.

one excpetion is a single backslash character.  It is raises and error in JSON becuase it is an escape character.
If we are using a JSON payload, it is my understanding that we are always going to encounter an error if a single
backslash is used.