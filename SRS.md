# Software Requirements Specification

**Description:**
Go Rest service (will be referenced as Service below) provides possibility to perform CRUD operations for users, posts, comments and TODOs  

## Users operation
[SRS] Service shall provide possibility to create new user.  
[SRS] User shall contain the following fields: id, name, email, gender, status  
### User fields
[SRS] Id field shall be mandatory, integer, autoincremented.  
[SRS] Name field shall be mandatory string.  
[SRS] Email shall be mandatory string.  
[SRS] Gender shall be mandatory string 'male' or 'female'.  
[SRS] Status field shall be mandatory string 'active' or 'inactive'.  
******TODO:** need clarification 
- Should server check email syntax?
- What limitations to name and email length?
- What type of integer for id? 
- If created previously created user was deleted, could his id be taken for new user?  
[SRS] Service shall provide possibility to search users by any of user fields.



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


