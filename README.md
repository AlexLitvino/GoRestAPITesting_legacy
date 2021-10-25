# Objective

This is portfolio project for backend testing of web service **Go Rest**

# Description

Link to web service: https://gorest.co.in/

Go Rest service provides possibility to perform CRUD operations for users, posts, comments and TODOs

Requirements to Go Rest service is specified in [SRS](SRS.md)

# How to run tests
Get API access [token](https://gorest.co.in/access-token)     
Set obtained API access token in [config.ini](config.ini) file instead of  PUT_YOUR_GOREST_TOKEN_HERE line  
Install Allure (for example from [Git Hub repository](https://github.com/allure-framework/allure2/releases))   
Run `pip install -r requirements.txt`  
Run `python -m pytest --alluredir ./reports` or `python -m pytest -v --alluredir ./reports` for verbose output  
Run `allure generate -c ./reports` to generate report    
Run `allure serve ./reports` to display reports  