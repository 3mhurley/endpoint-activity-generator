# endpoint-activity-generator

## Description
Generator of endpoint activity.

Given a path to an executible:
* Execute process
* Log the following information
  * Process Execution
    * Timestamp of start time
    * Username that started the process
    * Process name
    * Process command line
    * Process ID
  * File Manipulation
    * Timestamp of activity
    * Full path to the file
    * Activity descriptor - e.g. create, modified, delete
    * Username that started the process that created/modified/deleted the file
    * Process name that created/modified/deleted the file
    * Process command line
    * Process ID
  * Network Activity
    * Timestamp of activity
    * Username that started the process that initiated the network ativity
    * Destination address and port
    * Source address and port
    * Amount of data sent
    * Protocol of data sent
    * Process name
    * Process command line
    * Process ID

Sample executible:
* Create a file
* Modify a file
* Delete a file
* Establish a network connection and transmit data
