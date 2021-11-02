# Software Requirements Specification

**Description:**
Go Rest service (will be referenced as Service below) provides possibility to perform CRUD operations for users, posts, comments and TODOs  

## Users operation
[SRS_1] Service shall provide possibility to create new user.  
[SRS_2] Service shall forbid create user without authorization.  

### User fields
[SRS_3] Id field shall be autoincremented integer.  
[SRS_4] Name field shall be mandatory string.  
[SRS_5] Email shall be mandatory string.  
[SRS_6] Gender shall be mandatory string 'male' or 'female'.  
[SRS_7] Status field shall be mandatory string 'active' or 'inactive'.  
[SRS_8] Email should be unique.  
******TODO:** need clarification 
- Should server check email syntax?
- What limitations to name and email length?
- What type of integer for id? 
- If previously created user was deleted, could his id be taken for new user?  

### User search
[SRS] Service shall provide possibility to search users by any of user fields.
[SRS] User shall contain the following fields: id, name, email, gender, status  


Resources
https://gorest.co.in/public/v1/users	1666
https://gorest.co.in/public/v1/posts	1287
https://gorest.co.in/public/v1/comments	1268
https://gorest.co.in/public/v1/todos	1833

Trying it Out
POST /public/v1/users	Create a new user
GET /public/v1/users/123	Get user details
PUT|PATCH /public/v1/users/123	Update user details
DELETE /public/v1/users/123	Delete user

Nested Resources
GET /public/v1/users/123/posts	Retrieves user posts
GET /public/v1/posts/123/comments	Retrieves post comments
GET /public/v1/users/123/todos	Retrieves user todos
POST /public/v1/users/123/posts	Creates a user post
POST /public/v1/posts/123/comments	Creates a post comment
POST /public/v1/users/123/todos	Creates a user todo




## User creation


