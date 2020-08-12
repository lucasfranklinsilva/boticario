
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
In the terminal run: Flask db init (Start the service) -> Flask db migrate (Create the migrate files) -> Flask db Upgrade (Upgrade the database) or
Running the queries in the folder utils  

* Installing Seq (Log System): You can run the log system with docker, to download the image, run the command: *docker pull datalust/seq*. Then you can run a instace by the command: *docker run --name seq -d --restart unless-stopped -e ACCEPT_EULA=Y -p 5341:80 datalust/seq:latest*. The config file for the system is in the folder app/serilog.yml. Ref link: https://hub.docker.com/r/datalust/seq


## How to use the API ##

After everything is up and running, you can:

* Get All Resellers: http://127.0.0.1:5000/reseller [GET]
* Get a Reseller: http://127.0.0.1:5000/reseller/{cpf} [GET]
* Update a Reseller: http://127.0.0.1:5000/reseller/update/{cpf} [PUT]
* Update a Reseller: http://127.0.0.1:5000/reseller/delete/{cpf} [DELETE]
* Add a Reseller: http://127.0.0.1:5000/reseller/new [POST]

    {
        "city": "Montes Claros",
        "country": "Brazil",
        "cpf": "09838081639",
        "create_date": "2020-08-08T14:43:35",
        "email": "lucas.silva@gmail.com",
        "first_name": "Lucas",
        "is_active": 1,
        "last_name": "Silva",
        "phone": "31899882299",
        "state": "MG",
        "street": "Rua B",
        "zip_code": "30900123",
        "password": "a1b2c3d4e5@",
	"last_updated": "2020-08-08T14:43:35"
    }


* Get All Purchases: http://127.0.0.1:5000/purchase [GET]
* Get a Reseller Purchases: http://127.0.0.1:5000/reseller/purchases/{cpf} [GET]
* Get Purchase: http://127.0.0.1:5000/purchase/{purchase_d} [GET]
* Update a Purchase: http://127.0.0.1:5000/purchase/update/{id_purchase} [PUT]
* Delete a Purchase: http://127.0.0.1:5000/purchase/delete/{id_purchase} [DELETE]
* Add a Purchase: http://127.0.0.1:5000/purchase/new [POST]
    {
        "cpf": "09838081639",
        "date": "2020-08-08T14:54:35",
        "product_code": "1",
        "product_price": 5000.0
    }
    
* Get Total Cashback: http://127.0.0.1:5000/cashback/total/{cpf} [GET]
* User Login: http://127.0.0.1:5000/authentication [POST]

    {
        "email": "abc@cde.com.br",
        "password": "a1b2c3d4"
    }
//Returns Autentication Token

## Still pending on development ##

* **Implement autentication in all end points and set access control**
* **Implement administration and access rules**
* **Bug Fixes** 

### Other End Points ###

 - http://127.0.0.1:5000/purchase_status		[GET] Get All Purchase Status
   Properties
 - http://127.0.0.1:5000/purchase_status/{id}		[GET] Get a All Purchase Status
   with ID iquals to 1
 - http://127.0.0.1:5000/purchase_status/update/{id}	[PUT] Update a Purchase Status
   Property with ID iquals to 1
 - http://127.0.0.1:5000/purchase_status/delete/{id}	[DELETE] Delete a Purchase Status
   Property with ID iquals to 1
 - http://127.0.0.1:5000/purchase_status/new		[POST] Add a new Purchase Status
   

 - http://127.0.0.1:5000/cashback		[GET] Get All Cashback
   Properties
 - http://127.0.0.1:5000/cashback/{id}		[GET] Get a All Cashback
   with ID iquals to 1
 - http://127.0.0.1:5000/cashback/update/{id}	[PUT] Update a Cashback
   Property with ID iquals to 1
 - http://127.0.0.1:5000/cashback/delete/{id}	[DELETE] Delete a Cashback
   Property with ID iquals to 1
 - http://127.0.0.1:5000/cashback/new		[POST] Add a new Cashback


