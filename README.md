# endpoint-activity-generator

## Description
This app is a simple CLI project that generates endpoint activity and logs that activity to a file (csv).
The app functions using a simple CLI with three core functions.
1. file - Create, manipulate, and delete a file given a destination, name, and extension.
2. exe - Run an executable given a location, name, and any optional arguments or options.
3. data - Transmit a JSON object over TCP or HTTP (API).

This application includes a logging file (csv) which captures information about the application as it process each function
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
  * Username that started the process that initiated the network activity
  * Destination address and port
  * Source address and port
  * Amount of data sent
  * Protocol of data sent
  * Process name
  * Process command line
  * Process ID

A sample executable has been provided for testing the execution process.

Sample executable:
* Create a file
* Modify a file
* Delete a file
* Establish a network connection and transmit data

## Usage

### Endpoint Activity Generator

This app is command line based and can either be run directly as a python file or through the executable.

This app has three main processes:
1. Create, modify, and delete a file
2. Run an specified executable
3. Transmit data to a specified location

#### File manipulation
```
$ ./app.exe file
```

Invoking this process prompts the user for three additional pieces of information.
1. Directory path to store the file
2. Name of the file - Defaults to `endpoint_activity`
3. Extension type of the file - Defaults to `txt`

Leave prompts blank to use the default option.

Example:
```
$ ./app.exe file
Enter a path for the file destination: D:/Dev/Misc
Enter a name for the file [endpoint_activity]:
Enter an extension type for the file [txt]: csv
```

#### Executable Invocation
```
$ ./app.exe exe
```

Invoking this process prompts the user for three additional pieces of information.
1. File path where the executable is located
2. Name of the executable
3. Options or arguments for the executable - Can be blank

Example:
```
$ ./app.exe file
Enter the path to the executable: D:/Dev/Apps
Enter the name of the executable: file_manipulation.exe
Enter any optional arguments:
```

#### Data Transmission
The application can be used to send json data either via API or TCP
##### API
```
$ ./app.exe data api
```

Invoking this process prompts the user for three additional pieces of information.
1. The api endpoint address
2. An api key
3. A json object to send

Example:
```
$ ./app.exe file
Enter the api endpoint: 1.1.1.1
Enter the api key: 1234
Enter the json data: {"alpha": 1, "beta": 2}
```

##### TCP
```
$ ./app.exe data tcp
```

Invoking this process prompts the user for three additional pieces of information.
1. The host address
2. The port
3. A json object to send

Example:
```
$ ./app.exe file
Enter the host address or ip address: 1.1.1.1
Enter the port: 1234
Enter the json data: {"alpha": 1, "beta": 2}
```

### Sample Execution App

If you want to run this manually these are the options:

```
python app.py [path] --name [file_name] --exe [file_exe]
```

Note: If on Windows be sure to escape your slashes `D:\\Dev\\Data`

## Dev Instructions

python version 3.8.x

### Virtual Environment
This project was built using `virtualenv`

Installation and Configuration
```
$ pip install virtualenv --user
$ cd endpoint-activity-generator
$ virtualenv venv
```

Activate
```
$ . venv/bin/activate
```

or

```
$ . venv/Scripts/activate
```

Deactivate
```
$ deactivate
```

### Install Requirements
There are two sets of installation requirements depending on your intended use.
The standard requirements file includes all packages required for running the application through python.
The dev requirements include all packages used to format, clean, and bundle the python project into an executable.

#### Requirements
```
$ pip install -r requirements.txt
```

#### Dev Requirements
```
$ pip install -r dev-requirements.txt
```

### Build Process
The application can be run as a python project or bundled into an executable.
The build process utilizes a python package called `pyinstaller`.

Ensure you are at the project root before executing the build command.

Build
```
$ pyinstaller --onefile app.py
```

Once this process is complete you should see a `dist` folder which contains your executable. Copy this exe and move it to the root project directory to to run it.
