## API Documentation

## USER AUTHENTICATION/AUTHORIZATION

### All endpoints that require authentication

All endpoints that require a current user to be logged in.

* Request: endpoints that require authentication
* Error Response: Require authentication
  * Status Code: 401
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Authentication required",
      "statusCode": 401
    }
    ```

### All endpoints that require proper authorization

All endpoints that require authentication and the current user does not have the
correct role(s) or permission(s).

* Request: endpoints that require proper authorization
* Error Response: Require proper authorization
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Forbidden",
      "statusCode": 403
    }
    ```

## PROFILE
### Get the Current User

Returns the information about the current user that is logged in.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /api/users/profile
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "email" : "demolition@yahoo.com",
	  "first_name" : "Demolition",
	  "last_name" : "demo",
	  "username" : "demolition",
	  "pronouns" : "he/him", // default empty
	  "about" : "demo user",
	  "website" : "https://demolition.io",
	  "age" : 24,
	  "profile_visits" : 40,
	  "gender" : "male",
	  "language" : "english",
	  "country" : "United States",
	  "deactivated" : false,
	  "profile_pic" : "http://demolition.png//"
    }
    ```

### Log In a User

Logs in a current user with valid credentials and returns the current user's
information. If user is deactivated, sets the deactivated to false.

* Require Authentication: false
* Request
  * Method: POST
  * URL: /api/users/login
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "email": "demolition@yahoo.com",
      "password": "demo"
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "email" : "demolition@yahoo.com",
	  "first_name" : "Demolition",
	  "last_name" : "demo",
	  "username" : "demolition",
	  "pronouns" : "he/him", // default empty
	  "about" : "demo user",
	  "website" : "https://demolition.io",
	  "age" : 24,
	  "profile_visits" : 40,
	  "gender" : "male",
	  "language" : "english",
	  "country" : "United States",
	  "deactivated" : false,
	  "profile_pic" : "http://demolition.png//",
      "token": ""
    }
    ```

* Error Response: Invalid credentials
  * Status Code: 401
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Invalid credentials",
      "statusCode": 401
    }
    ```

* Error response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation error",
      "statusCode": 400,
      "errors": {
        "email": "Email is required",
        "password": "Password is required"
      }
    }
    ```

### Sign Up a User

Creates a new user, logs them in as the current user, and returns the current
user's information and moves them to the next setup phase.

* Require Authentication: false
* Request
  * Method: POST
  * URL: /api/users/signup
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "email": "demolition@yahoo.com",
      "password": "demo",
	  "age":24 // max 120 age
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "first_name": "Demolition",
	  "username" : "demolition",
      "email": "john.smith@gmail.com",
	  "age":24,
      "token": ""
    }
    ```

* Error response: User already exists with the specified email
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "User already exists",
      "statusCode": 403,
      "errors": {
        "email": "User with that email already exists"
      }
    }
    ```

* Error response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation error",
      "statusCode": 400,
      "errors": {
        "email": "Invalid email",
		"age": "Invalid age number"
      }
    }
    ```

### Sign Up User Details

Finishes up the current users signup process, once finshed redirects the user to the home page and returns
all of the users information.

* Require Authentication: true
* Request
  * Method: POST
  * URL: /api/users/signup-details
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
	  "gender" : "male",
	  "language" : "english",
	  "country" : "United States",
	  "topics" : ["Art", "NBA", "Vehciles", "Anime", "Men's Fashion"] // at least 5
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "email" : "demolition@yahoo.com",
	  "first_name" : "Demolition",
	  "last_name" : "", // default empty
	  "username" : "demolition",
	  "pronouns" : "", // default empty
	  "about" : "demo user",
	  "website" : "https://demolition.io",
	  "age" : 24,
	  "profile_visits" : 0,
	  "gender" : "male",
	  "language" : "english",
	  "country" : "United States",
	  "deactivated" : false,
	  "profile_pic" : "",
      "token": ""
    }
    ```

* Error response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation error",
      "statusCode": 400,
      "errors": {
        "gender": "Invalid gender",
		"language": "Invalid language",
		"country": "Invalid country",
		"topics": "Invalid topics",
      }
    }
    ```

### Edit current Users public profile

Edit the current users public profile once edited returns the
current users information.

* Require Authentication: true
* Request
  * Method: PUT
  * URL: /api/users/edit-profile
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
	  "first_name" : "Demo",
	  "last_name" : "lition", // default empty
	  "username" : "demo!!",
	  "pronouns" : "he/him", // default empty
	  "about" : "demo user",
	  "profile_pic" : "https://demo.png",
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "email" : "demolition@yahoo.com",
	  "first_name" : "Demo",
	  "last_name" : "lition",
	  "username" : "demo!!",
	  "pronouns" : "he/him",
	  "about" : "demo user",
	  "website" : "https://demolition.io",
	  "age" : 24,
	  "profile_visits" : 0,
	  "gender" : "male",
	  "language" : "english",
	  "country" : "United States",
	  "deactivated" : false,
	  "profile_pic" : "https://demo.png",
      "token": ""
    }
    ```

* Error response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation error",
      "statusCode": 400,
      "errors": {
        "first_name": "Invalid first name",
		"last_name": "Invalid last name",
		"about": "Invalid about me",
		"pronouns": "Invalid pronouns",
		"website": "Invalid website",
		"username": "Invalid username",
      }
    }
    ```

### Edit current Users personal information

Edit the current users personal information once finished
return the current users information.

* Require Authentication: true
* Request
  * Method: PUT
  * URL: /api/users/personal-information
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
	  "gender" : "male",
	  "country" : "United Kingdom",
	  "language" : "korean",
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "email" : "demolition@yahoo.com",
	  "first_name" : "Demolition",
	  "last_name" : "", // default empty
	  "username" : "demolition",
	  "pronouns" : "", // default empty
	  "about" : "demo user",
	  "website" : "https://demolition.io",
	  "age" : 24,
	  "profile_visits" : 0,
	  "gender" : "male",
	  "language" : "korean",
	  "country" : "United Kingdom",
	  "deactivated" : false,
	  "profile_pic" : "",
      "token": ""
    }
    ```

* Error response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation error",
      "statusCode": 400,
      "errors": {
        "gender": "Invalid gender",
		"country": "Invalid country",
		"language": "Invalid language",
      }
    }
    ```

### Edit current Users account settings

Edit the current users account settings once finished
return the current users information.

* Require Authentication: true
* Request
  * Method: PUT
  * URL: /api/users/account-settings
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
	  "email" : "newdemo@yahoo.com"
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "id": 1,
      "email" : "newdemo@yahoo.com",
	  "first_name" : "Demolition",
	  "last_name" : "", // default empty
	  "username" : "demolition",
	  "pronouns" : "", // default empty
	  "about" : "demo user",
	  "website" : "https://demolition.io",
	  "age" : 24,
	  "profile_visits" : 0,
	  "gender" : "male",
	  "language" : "korean",
	  "country" : "United Kingdom",
	  "deactivated" : false,
	  "profile_pic" : "",
      "token": ""
    }
    ```

* Error response: User already exists with the specified email
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "User already exists",
      "statusCode": 403,
      "errors": {
        "email": "User with that email already exists"
      }
    }
    ```

* Error response: Body validation errors
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation error",
      "statusCode": 400,
      "errors": {
        "email": "Invalid email"
      }
    }
    ```

### Deactivate current user

Logs out a current user,
deactivate their account
and returns successful message.

* Require Authentication: true
* Request
  * Method: PUT
  * URL: /api/users/deactivate
  * Headers:
    * Content-Type: application/json
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body

    ```json
    {
      "message": "Successfully deactivated"
    }

* Error Response
  * Users's account has already been deactivated
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Account has already been deactivated"
    }
    ```

### Log Out a User

Logs out a current user and returns successful message.

* Require Authentication: true
* Request
  * Method: POST
  * URL: /api/users/logout
  * Headers:
    * Content-Type: application/json
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body

    ```json
    {
      "message": "Successfully logged out"
    }

* Error Response
  * No current user logged in
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "No user currently logged in"
    }
    ```

### Delete current users Account

Completely remove all of the current users account and
logs them out.

* Require Authentication: true
* Request
  * Method: DELETE
  * URL: /api/users
  * Headers:
    * Content-Type: application/json
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body

    ```json
    {
      "message": "Successfully deleted"
    }

* Error Response
  * User does not exist
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "User does not exist"
    }
    ```


## Follows

### Get all followers of user

Returns all the followers.

* Require Authentication: false
* Request
  * Method: GET
  * URL: /api/users/<int:user_id>/followers
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "followers":[
        {
          "id": 2,
		  "first_name" : "user2",
	  	  "last_name" : "first",
		  "profile_pic" : "https://user2profile.png",
        },
		{
          "id": 3,
		  "first_name" : "alex",
	  	  "last_name" : "betita",
		  "profile_pic" : "https://alexbetita.png",
        },
		{
          "id": 4,
		  "first_name" : "john",
	  	  "last_name" : "doe",
		  "profile_pic" : "https://johndoe.png",
        }
      ],
	  "num_of_followers": 3
    }
    ```

* Error Response
  * User does not exist
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "User does not exist"
    }
    ```

### Get all following of user

Returns users following information.

* Require Authentication: false
* Request
  * Method: GET
  * URL: /api/users/<int:user_id>/following
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "following":[
        {
          "id": 2,
		  "first_name" : "user2",
	  	  "last_name" : "first",
		  "profile_pic" : "https://user2profile.png",
        },
		{
          "id": 3,
		  "first_name" : "alex",
	  	  "last_name" : "betita",
		  "profile_pic" : "https://alexbetita.png",
        },
		{
          "id": 4,
		  "first_name" : "john",
	  	  "last_name" : "doe",
		  "profile_pic" : "https://johndoe.png",
        }
      ],
	 "num_of_following": 3
    }
    ```

* Error Response
  * User does not exist
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "User does not exist"
    }
    ```

### Follow a user

Follow a user.

* Require Authentication: true
* Request
  * Method: POST
  * URL: /api/users/<int:user_id>/follow
  * Headers:
    * Content-Type: application/json
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body

    ```json
    {
      "message": "Successfully followed user"
    }

* Error Response
  * User already following this user
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Already following this user"
    }
    ```

* Error Response
  * User does not exist
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "User does not exist"
    }
    ```

### Unfollow a user

Unfollow a user.

* Require Authentication: true
* Request
  * Method: POST
  * URL: /api/users/<int:user_id>/unfollow
  * Headers:
    * Content-Type: application/json
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body

    ```json
    {
      "message": "Successfully unfollowed user"
    }

* Error Response
  * Unable to unfollow a user who isn't followed
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Unable to unfollow a user who isn't followed"
    }
    ```

* Error Response
  * User does not exist
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "User does not exist"
    }
    ```

## Pins

### Get all pins

Returns all the pins.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /api/pins
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "pins":[
        {
			"id" : 1,
			"media_url" : "https://i.pinimg.com/originals/c2/1c/15/c21c15271b1a73f15cab2d152563afb4.jpg",
			"title" : "pokeball",
			"createdAt": "2021-11-19 20:39:36",
     	 	"updatedAt": "2021-11-19 20:39:36",
			"user" : {
				"id" : 1,
				"first_name" : "Demolition",
				"last_name" : "Demo",
				"profile_pic" : "demoliton.png"
			},
			"topic" : "games"
        },
		{
			"id" : 2,
			"media_url" : "https://i.pinimg.com/originals/6d/2c/54/6d2c54126dae331528fc2af6b43acfa1.jpg",
			"title" : "rando_pic",
			"createdAt": "2021-11-19 20:39:36",
      		"updatedAt": "2021-11-19 20:39:36",
			"user" : {
				"id" : 1,
				"first_name" : "Demolition",
				"last_name" : "Demo",
				"profile_pic" : "demoliton.png"
			},
			"topic" : "sports"
        },
		{
			"id" : 3,
			"media_url" : "https://3121c1231.jpg",
			"title" : "test",
			"createdAt": "2021-11-19 20:39:36",
      		"updatedAt": "2021-11-19 20:39:36",
			"user" : {
				"id" : 1,
				"first_name" : "Demolition",
				"last_name" : "Demo",
				"profile_pic" : "demoliton.png"
			},
			"topic" : "fashion"
        }
      ],
	  "num_of_pins": 3
    }
    ```

### Get all saved pins

Returns all the pins that were saved from the current user.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /api/pins/saved
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "pins":[
        {
			"id" : 1,
			"media_url" : "https://i.pinimg.com/originals/c2/1c/15/c21c15271b1a73f15cab2d152563afb4.jpg",
			"title" : "pokeball",
			"createdAt": "2021-11-19 20:39:36",
     	 	"updatedAt": "2021-11-19 20:39:36",
			"user" : {
				"id" : 1,
				"first_name" : "Demolition",
				"last_name" : "Demo",
				"profile_pic" : "demoliton.png"
			},
			"topic" : "games"
        },
		{
			"id" : 2,
			"media_url" : "https://i.pinimg.com/originals/6d/2c/54/6d2c54126dae331528fc2af6b43acfa1.jpg",
			"title" : "rando_pic",
			"createdAt": "2021-11-19 20:39:36",
      		"updatedAt": "2021-11-19 20:39:36",
			"user" : {
				"id" : 1,
				"first_name" : "Demolition",
				"last_name" : "Demo",
				"profile_pic" : "demoliton.png"
			},
			"topic" : "sports"
        },
		{
			"id" : 3,
			"media_url" : "https://3121c1231.jpg",
			"title" : "test",
			"createdAt": "2021-11-19 20:39:36",
      		"updatedAt": "2021-11-19 20:39:36",
			"user" : {
				"id" : 1,
				"first_name" : "Demolition",
				"last_name" : "Demo",
				"profile_pic" : "demoliton.png"
			},
			"topic" : "fashion"
        }
      ],
	  "num_of_pins": 3
    }
    ```


### Get all pins of current user

Returns all the current users pins.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /api/users/profile/pins
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "pins":[
        {
			"id" : 1,
			"media_url" : "https://i.pinimg.com/originals/c2/1c/15/c21c15271b1a73f15cab2d152563afb4.jpg",
			"title" : "pokeball",
			"createdAt": "2021-11-19 20:39:36",
      		"updatedAt": "2021-11-19 20:39:36",
			"topic" : "games"
        },
		{
			"id" : 2,
			"media_url" : "https://i.pinimg.com/originals/6d/2c/54/6d2c54126dae331528fc2af6b43acfa1.jpg",
			"title" : "rando_pic",
			"createdAt": "2021-11-19 20:39:36",
      		"updatedAt": "2021-11-19 20:39:36",
			"topic" : "games"
        },
		{
			"id" : 3,
			"media_url" : "https://3121c1231.jpg",
			"title" : "test",
			"createdAt": "2021-11-19 20:39:36",
      		"updatedAt": "2021-11-19 20:39:36",
			"topic" : "games"
        }
      ],
	  "num_of_pins": 3
    }
    ```

### Get all pins of from a user

Returns all pins from a users id.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /api/users/<int:id>/pins
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
	  "user": {
		"id" : 2,
		"first_name" : "v",
		"last_name" : "juniper",
		"username" : "juniperv",
		"website" : "https://junpier.com",
		"about" : "check out my pins",
		"profile_visits" : 10,
		"profile_pic" : "https://juniperv.png"
	  },
	  "num_of_followers": 10,
	  "num_of_following": 20,
      "pins":[
        {
			"id" : 1,
			"media_url" : "https://i.pinimg.com/originals/c2/1c/15/c21c15271b1a73f15cab2d152563afb4.jpg",
			"title" : "pokeball",
			"createdAt": "2021-11-19 20:39:36",
      		"updatedAt": "2021-11-19 20:39:36",
			"topic" : "games"
        },
		{
			"id" : 2,
			"media_url" : "https://i.pinimg.com/originals/6d/2c/54/6d2c54126dae331528fc2af6b43acfa1.jpg",
			"title" : "rando_pic",
			"createdAt": "2021-11-19 20:39:36",
      		"updatedAt": "2021-11-19 20:39:36",
			"topic" : "games"
        },
		{
			"id" : 3,
			"media_url" : "https://3121c1231.jpg",
			"title" : "test",
			"createdAt": "2021-11-19 20:39:36",
      		"updatedAt": "2021-11-19 20:39:36",
			"topic" : "games"
        }
      ],
	  "num_of_pins": 3
    }
    ```

* Error Response
  * User does not exist
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "User does not exist"
    }
    ```

### Get details of a pin from pin id

Return details of a pin from pin id.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /api/pins/<int:pin_id>
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
	  "user" : {
		"id" : 1,
		"first_name" : "Demolition",
		"last_name" : "demo",
		"profile_pic" : "https://demolition.png"
	  },
      "pin": {
		"id" : 1,
		"link" : "media.com",
		"media_url" : "https://i.pinimg.com/originals/c2/1c/15/c21c15271b1a73f15cab2d152563afb4.jpg",
		"title" : "pokeball",
		"description": "a tool for catching pokemon",
		"alt_text": "alternative text",
		"website" : "media.com",
		"pin_clicks" : 20,
		"impressions": 3,
		"saves" : 4,
		"is_commentable" : true,
		"notes_to_self" : "this a pokeball",
		"board_only" : false,
		"createdAt": "2021-11-19 20:39:36",
		"updatedAt": "2021-11-19 20:39:36",
      },
	  "topic" : "games",
	  "board" : {
		"id" : 1,
		"board_cover" : "https://i.pinimg.com/originals/c2/1c/	15/c21c15271b1a73f15cab2d152563afb4.jpg",
		"is_secret" : false,
		"name" : "HOME"
	  }
    }
    ```

### Create a pin

Create a pin and returns pin information

* Require Authentication: true
* Request
  * Method: POST
  * URL: /api/pins
  * Body:

    ```json
    {
		"link" : "media.com",
		"media_url" : "https://i.pinimg.com/originals/c2/1c/15/c21c15271b1a73f15cab2d152563afb4.jpg",
		"title" : "pokeball",
		"description": "a tool for catching pokemon",
		"alt_text": "alternative text",
		"website": "media.com",
		"is_commentable" : true,
		"notes_to_self" : "this a pokeball",
		"board_only" : false,
		"topic" : "games",
		"board" : "profile" // has to exist
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "pin": {
		"id" : 1,
		"link" : "media.com",
		"media_url" : "https://i.pinimg.com/originals/c2/1c/15/c21c15271b1a73f15cab2d152563afb4.jpg",
		"title" : "pokeball",
		"description": "a tool for catching pokemon",
		"alt_text": "alternative text",
		"website": "media.com",
		"pin_clicks" : 0,
		"impressions": 0,
		"saves" : 0,
		"is_commentable" : true,
		"notes_to_self" : "this a pokeball",
		"board_id" : 1,
		"createdAt": "2021-11-19 20:39:36",
		"updatedAt": "2021-11-19 20:39:36",
      },
	  "topic" : "games",
	  "board" : {
		"id" : 1,
		"board_cover" : "https://i.pinimg.com/originals/c2/1c/	15/c21c15271b1a73f15cab2d152563afb4.jpg",
		"is_secret" : false,
		"name" : "profile"
	  }
    }
    ```

* Error Response: Body validation error
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation Error",
      "statusCode": 400,
      "errors": {
		"boards" : "Not a valid board",
		"media_url" : "An Image is required to make a pin",
		"title" : "Title must be less than 100 characters",
		"description" : "Description less than 500 characters",
		"website" : "Website must be a valid website",
		"alt_text" : "Alt Text must be less than 500 characters",
		"is_commentable" : "Must be a valid value, either true or false"
      }
    }
    ```


### Edit details of a pin from id

Edit details of a pin from id.

* Require Authentication: true
* Require proper authorization: Current User must be the owner of the pin
* Request
  * Method: PUT
  * URL: /api/pins/<int:pin_id>
  * Body:

   ```json
    {
		"boards" : "profile",
		"title" : "new title",
		"description" : "new description",
		"website" : "https://new_title.com",
		"alt_text" : "new text",
		"notes_to_self" : "here is new note",
		"is_commentable" : false
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
		"id" : 1,
		"link" : "media.com",
		"media_url" : "https://i.pinimg.com/originals/c2/1c/15/c21c15271b1a73f15cab2d152563afb4.jpg",
		"title" : "new title",
		"description": "new description",
		"alt_text": "new text",
		"impressions": 3,
		"saves" : 4,
		"is_commentable" : false,
		"notes_to_self" : "here is new note",
		"board_id" : 1,
		"createdAt": "2021-11-19 20:39:36",
		"updatedAt": "2021-11-19 20:39:36",
		"board" : {
			"id" : 1,
			"board_cover" : "https://i.pinimg.com/originals/c2/1c/	15/c21c15271b1a73f15cab2d152563afb4.jpg",
			"is_secret" : false,
			"name" : "profile"
	  	}
    }
    ```

* Error Response: Body validation error
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation Error",
      "statusCode": 400,
      "errors": {
		"boards" : "Not a valid board",
		"title" : "Title must be less than 100 characters",
		"description" : "Description less than 500 characters",
		"website" : "Website must be a valid website",
		"alt_text" : "Alt Text must be less than 500 characters",
		"is_commentable" : "Must be a valid value, either true or false"
      }
    }
    ```

* Error Response
  * Pin couldn't be found
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Pin couldn't be found"
    }

### Delete a pin

Delete a pin.

* Require Authentication: true
* Require proper authorization: Current User must be the owner of the pin
* Request
  * Method: DELETE
  * URL: /api/pins/<int:pin_id>
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
		"message" : "Successfully deleted"
    }
    ```

* Error Response
  * Pin couldn't be found
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Pin couldn't be found"
    }
    ```

### Save a pin based on pin id

Save a pin based on pin id.

* Require Authentication: true
* Request
  * Method: POST
  * URL: /api/pins/<int:pin_id>/save
  * Headers:
    * Content-Type: application/json
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body

    ```json
    {
      "message": "Successfully saved pin"
    }

* Error Response
  * User already following this user
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Already saved this pin"
    }
    ```

* Error Response
  * Pin couldn't be found
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Pin couldn't be found"
    }
    ```

### Unsave a pin based on pin id

Unsave a pin based on pin id.

* Require Authentication: true
* Request
  * Method: PUT
  * URL: /api/pins/<int:pin_id>/unsave
  * Headers:
    * Content-Type: application/json
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body

    ```json
    {
      "message": "Successfully unsaved pin"
    }

* Error Response
  * User already following this user
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Already unsaved this pin"
    }
    ```

* Error Response
  * Pin couldn't be found
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Pin couldn't be found"
    }
    ```


### Add a pin to a board by id

Add a pin to a board by id

* Require Authentication: true
* Request
  * Method: POST
  * URL: /api/pin/<id:pin_id>/board
  * Body:

    ```json
    {
		"board_id" : 1
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
		"id" : 1,
		"media_url" : "pin1.img",
		"user" : {
			"id" : 1,
			"first_name" : "Demolition",
			"last_name" : "demo"
		}
    }
    ```

* Error Response: Body validation error
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation Error",
      "statusCode": 400,
      "errors": {
		"pin_id" : "Invalid pin id"
      }
    }
    ```

* Error Response:
  * Board couldn't be found
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Board couldn't be found"
    }
    ```

* Error Response:
  * Pin couldn't be found
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Pin couldn't be found"
    }
    ```

## Boards

### Get all boards from current user

Get all boards from the current user and return with pin information.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /api/users/profile/boards
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
	  "boards": [
			{
				"id" : 1,
				"name": "demo_board",
				"board_cover" : "pin1.png",
				"is_secret" : false,
				"num_of_pins": 3,
				"images" : [
					"pin1.png", "pin2.png", "pin3.jpeg"
				]
			},
			{
				"id" : 2,
				"name": "demo_board2",
				"board_cover" : "pin4.png",
				"is_secret" : false,
				"num_of_pins": 10,
				"images" : [
					"pin1.png", "pin2.png", "pin3.jpeg"
				]
			},
	  ]
    }
    ```

### Get all boards from a user id

Get all boards from the current user and return with pin information.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /api/boards/<int:user_id>
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
		"user": {
			"id" : 2,
			"first_name" : "v",
			"last_name" : "juniper",
			"username" : "juniperv",
			"website" : "https://junpier.com",
			"about" : "check out my pins",
			"profile_visits" : 10,
			"profile_pic" : "https://juniperv.png",
			"num_of_followers": 100,
			"num_of_following": 100
		},
		"boards": [
			{
				"id" : 1,
				"name": "demo_board",
				"board_cover" : "pin1.png",
				"is_secret" : false,
				"num_of_pins": 3,
				"images" : [
					"pin1.png", "pin2.png", "pin3.jpeg"
				]
			},
			{
				"id" : 2,
				"name": "demo_board2",
				"board_cover" : "pin4.png",
				"is_secret" : false,
				"num_of_pins": 10,
				"images" : [
					"pin1.png", "pin2.png", "pin3.jpeg"
				]
			},
		]
    }
    ```

* Error Response
  * User does not exist
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "User does not exist"
    }
    ```


### Get all pins of from a board id

Returns all pins from a board id.

* Require Authentication: true
* Request
  * Method: GET
  * URL: /api/boards/<int:board_id>
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "pins":[
        {
			"id" : 1,
			"media_url" : "https://i.pinimg.com/originals/c2/1c/15/c21c15271b1a73f15cab2d152563afb4.jpg",
			"title" : "pokeball",
			"createdAt": "2021-11-19 20:39:36",
      		"updatedAt": "2021-11-19 20:39:36",
			"topic" : "games"
        },
		{
			"id" : 2,
			"media_url" : "https://i.pinimg.com/originals/6d/2c/54/6d2c54126dae331528fc2af6b43acfa1.jpg",
			"title" : "rando_pic",
			"createdAt": "2021-11-19 20:39:36",
      		"updatedAt": "2021-11-19 20:39:36",
			"topic" : "games"
        },
		{
			"id" : 3,
			"media_url" : "https://3121c1231.jpg",
			"title" : "test",
			"createdAt": "2021-11-19 20:39:36",
      		"updatedAt": "2021-11-19 20:39:36",
			"topic" : "games"
        }
      ],
	  "num_of_pins": 3
    }
    ```

* Error Response
  * Board couldn't be found
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Board couldn't be found"
    }

### Create a board

Create a board and returns pin information

* Require Authentication: true
* Request
  * Method: POST
  * URL: /api/board
  * Body:

    ```json
    {
		"name" : "new board",
		"is_secret" : false,
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
		"id" : 1,
		"board_cover" : "",
		"is_secret" : false,
		"name" : "new board",
		"createdAt": "2021-11-19 20:39:36",
		"updatedAt": "2021-11-19 20:39:36",
    }
    ```

* Error Response: Body validation error
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation Error",
      "statusCode": 400,
      "errors": {
		"name" : "Name must be between 1 and 50"
      }
    }
    ```

* Error Response:
  * Board already exists
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Board already exists"
    }
    ```

### Edit a board from id

Edit a board from id and returns board information

* Require Authentication: true
* Request
  * Method: POST
  * URL: /api/board/<int:board_id>
  * Body:

    ```json
    {
		"board_cover" : "board_cover.png",
		"name" : "edited_board",
		"is_secret" : true
    }
    ```

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
		"id" : 1,
		"board_cover" : "board_cover.png",
		"is_secret" : true,
		"name" : "edited_board",
		"createdAt": "2021-11-19 20:39:36",
		"updatedAt": "2021-11-19 20:39:36",
    }
    ```

* Error Response: Body validation error
  * Status Code: 400
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Validation Error",
      "statusCode": 400,
      "errors": {
		"name" : "Name must be between 1 and 50"
      }
    }
    ```

* Error Response:
  * Board already exists
  * Status Code: 403
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Board already exists"
    }
    ```

### Delete a board

Delete a board.

* Require Authentication: true
* Require proper authorization: Current User must be the owner of the board
* Request
  * Method: DELETE
  * URL: /api/board/<int:board_id>
  * Body: none

* Successful Response
  * Status Code: 200
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
		"message" : "Successfully deleted"
    }
    ```

* Error Response
  * Board couldn't be found
  * Status Code: 404
  * Headers:
    * Content-Type: application/json
  * Body:

    ```json
    {
      "message": "Board couldn't be found"
    }
    ```
