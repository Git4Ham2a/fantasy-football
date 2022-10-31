# Fanatasy Football App

## Project Brief:
The project required a web application that uses Flask web framework to be designed and produced that met the following criteria. 

•	Integrates with a MySQL database which demonstrates CRUD (create, read, update and delete) functionality.

•	Utilises containers to host and deploy the application.

•	Uses a continuous integration (CI)/continuous deployment (CD) pipeline that automatically tests, builds and deploys the application.

•	Stores data entries in a MySQL database with comprises of a minimum of two tables sharing a one-to-many relationship. 

The required structure for the application is shown in the diagram below.  

![image](https://user-images.githubusercontent.com/111743185/199122645-329987bd-8962-42dc-ad2a-f9755df1fec5.png)

## App Design:
I have built a fantasy football app that allows users to add team and player entities (create functionality), view teams and players entries (read functionality), update teams and players entries (update functionality) and delete team and player entries (delete functionality). 

The database for the app comprises of a Teams table and a Players table, with each team associated with multiple players (one-to-many relationship). The ERD for this is shown below:

![image](https://user-images.githubusercontent.com/111743185/199122797-35f197c8-8e9e-457d-aa69-e4fd81531405.png)

## CI Pipeline:

The project required the implementation of several stages of a CI pipeline. These were version control, development environment and build server.

Git was used for version control, with the project repository hosted on GitHub. Version control via Git allowed for changes to be made and committed whilst storing the commit history to allow for access to earlier versions. The app was mainly built on the main and develop branches, with additional branches created later for the purpose of deployment via Docker Swarm and testing through the use of Pytest. 

The development environment used was a Python3 virtual environment (venv) hosted on a Azure virtual machine running Linux Ubuntu 20.04. Use of venv allowed pip installs to be performed and the app to be run without affecting any conflicting pip installs on the same machine.

DockerHub was used to create three different containers. One for the Flask application, another for the MySQL database and the third for Nginx. Deploying these containers hosted the application on the public IP address, connected it to the database and allowed for access via a reverse proxy, Nginx. These were uploaded to DockerHub for use with Docker Compose and Docker Swarm. A Docker compose file was created to run all three of containers using a single command. This was further expanded upon through the use of Docker Swarm which used two VM, a master and worker node to deploy the containers across the two machines. This meant the application could be accessed through either of the two public IP addresses available. 

Jenkins was used as a build server, providing automation of building and testing. The automation was achieved by setting up a pipeline project which connected to the project repository on GitHub that deployed the application using the Docker compose file through a webhook which triggered a new build whenever a commit was pushed in GitHub. 

This pipeline is shown in the diagram below.

![Pipeline](https://user-images.githubusercontent.com/111743185/199123061-77823995-2208-4dc0-98eb-3a616b284bca.png)

## Testing
Testing the app was an essential part of the development process. Unit testing using pycharm was implemented to test the functionality of the app. Unit tests were written for create, read, update, and delete functionality.

The tests I have written currently have poor coverage, as they encounter import error. As a result, I have decided not to integrate the tests into the Jenkins pipeline.

![image](https://user-images.githubusercontent.com/111743185/199123159-49c10961-9343-45c6-8b6c-f89a87330aa4.png)

## Future improvements
•	To improve test coverage 
•	Allow for the player number to be added as well as name, position and team ID.
