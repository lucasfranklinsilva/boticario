
# README #

This API allows you to save information about Resellers, Purchases and Cashback.

## What is it made of? ##

* Python 3.8
* MySql 8.0
* Main Libraries From Flask:
	* Flask
	* Blueprint
	* Request
	* Current_app
	* Jsonify
	* Migrate
	* SQLAlchemy
	* Marshmallow
  	* Serilog
	
* Tools:
	* PyCharm IDE
	* MySql Workbench
	* Git Bash
	* Postman
	

## How to set up ##

* Get all the dependecies from the file requirements.txt
* Create a database named: boticario
* Set up the database credentials in the App constants file (constants.py) in the section #MYSQL. The conection string must have this format mysql://user_name:password@localhost:3306/boticario (The domain localhost and the port can be different depending on your setup)
* There are two ways to import the tables to the database:
**Running the migrates**: 
In the terminal run * Flask db init *(Start the service) -> * Flask db migrate * (Create the migrate files) -> * Flask db Upgrade * (Upgrade the database)
** Running the queries in the folder utils **

* Installing Seq (Log System): You can run the log system with docker, to download the image, run the command: *docker pull datalust/seq*. Then you can run a instace by the command: *docker run --name seq -d --restart unless-stopped -e ACCEPT_EULA=Y -p 5341:80 datalust/seq:latest*. The config file for the system is in the folder app/serilog.yml. Ref link: https://hub.docker.com/r/datalust/seq


## How to use the API ##

After everything is up and running, you can:

* To add a new Real Estate Agency the API expect the following json:

    {
	
    	"address": "",		//Optional
    	"name": ""			//Mandatory
		
    }

* To add a new Real Estate Property:

    {
	
    	"address": "",				//Mandatory
    	"agency": "",				//Mandatory
    	"characteristics": "",		//Optional
    	"description": "",			//Mandatory
    	"name": "",					//Mandatory
    	"purpose": "",				//Optional
    	"status": ""				//Mandatory
		
    }

## Still pending development ##

* **Better error handling**
* **Return objects for *agency*, *purpose* and *status* instead of forigner key in the  Real Estate Property answer.**

## End Points ##

### Real State Properties ###

 - http://127.0.0.1:5000/realestate			[GET] Get All Real State
   Properties
 - http://127.0.0.1:5000/realestate/1			[GET] Get Real State Property
   with ID iquals to 1
 - http://127.0.0.1:5000/realestate/update/1	[PUT] Update Real State
   Property with ID iquals to 1
 - http://127.0.0.1:5000/realestate/delete/1	[DELETE] Delete Real State
   Property with ID iquals to 1
 - http://127.0.0.1:5000/realestate/new		[POST] Add new Real State
   Property

### Real State Agencies ###

 - http://127.0.0.1:5000/agency		[GET] Get All Real State Agencies
 - http://127.0.0.1:5000/agency/1			[GET] Get Real State Agency with
   ID iquals to 1
 - http://127.0.0.1:5000/agency/update/1	[PUT] Update Real State
   Agency with ID iquals to 1
 - http://127.0.0.1:5000/agency/delete/1	[DELETE] Delete Real State
   Agency with ID iquals to 1
 - http://127.0.0.1:5000/agency/new		[POST] Add new Real State
   Agency

