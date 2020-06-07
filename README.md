Creating a CRUD system using the python, flask and for connection to database Flask-SQLAlchemy.

In the models package i defined autosallon, car and user file. In autosallon model i have created a autosalon table
with its atributes and some "helper" methods. The same goes with car file, created a car table and some methods.
I have conected car and autosalon object with relationship many to 1.
User file contains a user table with its methods.

In resource package I defined autosallon file in witch the class inherits Resource class.
Class Autosalon we can use in route as /autosalon/somename (GET) to get the autosalon with its unique name,
POST to create a new one, and we can DELETE it by passing its name to the route.
There is also AutosalonList which can return all the Autosalon objects with passing in url /autosalons.

Almost everything in autosallon file and car file are the same. Except the atributes and methods.
In car file we have a passability to update a car after it is created its realized with method PUT.

In resources user.py is a method post witch creates a new  user and checking if the user with those
credentials is alredy created.

File authentication contains 2 methods witch are providing us to read the users from db either by the name or email.
It is also checking if the user passed in the correct password.

So this is how it all works. First in our text editor console we should run the 'python application.py' after running it the database
will be created automaticly. In route run http://127.0.0.1/register and in body pass the name, password and email to create a user.
After that run http://127.0.0.1/auth that will provide an JWT token, those are used to authenticate users or by other words to give the
user access to create, read, update or delete a car or autosaloon.
We a car http://127.0.0.1/car/carname in route we define a cars name in body we have to define price, store_id, engintype and cartype..
To create autosalon http://127.0.0.1/autosalon/giveitaname and then in body describe its properties(address, numberofemployees).
When we use GET method in the same rout http://127.0.0.1/autosalon/giveitaname it will retriev the autosalon and all the cars inside of it, cars are passed inside the store by the autosalon_id.





