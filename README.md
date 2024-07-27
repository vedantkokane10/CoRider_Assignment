# CoRider_Assignment

This application is developed using Flask and MongoDB. It provides REST API endpoints for CRUD operations on a User resource.

### User Resource Fields

- `id` (unique identifier for the user) 
- `firstName` (the first name of the user)
- `lastName` (the last name of the user)
- `email` (the email address of the user)
- `password` (the password of the user)

### REST API Endpoints

- `POST /createUser` - Creates a new user. (Pass JSON body for feilds like firstName, lastName, email, password)
- `POST /fetchUsers` - Fetches all users.
- `POST /update/<email>` - Updates user data by email.
- `DELETE /delete/<email>` - Deletes user by email.

### Requirements
- Flask==2.1.1
- Flask-PyMongo==2.3.0
- flask-bcrypt==0.7.1
- python-dotenv==0.20.0

  
### Running the Application with Docker

- To pull - docker pull vedantkokane545/corider-assignment:0.0.1.RELEASE
- To run - docker run -p 5000:5000 vedantkokane545/corider-assignment:0.0.1.RELEASE
