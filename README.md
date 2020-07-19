# Member activity reporter:

This app is desinged to response to below RESTful web service requests: 

• the total win amount for a given *member*,
• the total wager amount for a given *member*, and
• the number of wagers placed by a given *member*

** All responses are in *JSON* format.

It can accept two optional parameters 
1. *specific month* with default value = 'all'
2. *specific game ID* with default value = 'all'

The app initiation creates the log file app.log which logs failures on creating a new object of the class Member.

For each request there will be a specific endpoint that tries to create an object of the
class Player with the exception of logging the failure into file app.log. Then creates the dict member_report
and returns jsonified dictionary with the following keys:
1. member ID
2. activity_year_month
3. game_id
4. requested variables e.g. total win amount


The class Player which gets three variables of 1. member ID 2. month 3 game id. 
It has the following methods that are querying the database and find:
1. total win amount 
2. total wager amount 
3. number of wagers
The class initioation creates the log file Player.log based on the passed variables in class
initiation the condition of the sql query is being created. Then it tries to create an instance of
the class Oracle and connects the object to database using the class Oracle.
Each method has it's own main sql script which will be concatenated to the
conditional sql that was created on class initiation. And methods trying to
run the specific query and fetch it to the variable that they will return
with exception of logging failure.

The Class Oracle is designed to connect to database, return result of executing the query and get diconnected.
 