# Member activity reporter:

This app is desinged to response to below RESTful web service requests: 

* the total win amount for a given **member**,
* the total wager amount for a given **member**, and
* the number of wagers placed by a given **member**

 *All responses are in JSON format*

### Optional parameters
1. **specific month** with default value = '**all**'
2. **specific game ID** with default value = '**all**'

# Tech/framework used
 * Flask
 * Python
 * Oracle

# Description

This app is designed with 3 different endpoints to respond to the above RESTful web service requests. The app initiation will create the log file to log failures and warnings.

```python
@app.route('/total_wager_amount/<member_id>')
```

First request is the total win amount. The endpoint can be provided with specific month and game ID as optional parameters. After assigning the main parameters(member ID) and optional parameters(all months\games if not provided), the app tries to create an object of Member class for the specific member ID provided. Jsonified member report will be returned based on the provided parameters and using the Member total win amount method of Member class.  

```python
@app.route('/total_wager_amount/<member_id>')
```

Second request is the total wager amount. The endpoint can be provided with specific month and game ID as optional parameters. After assigning the main parameters(member ID) and optional parameters(all months\games if not provided), the app tries to create an object of Member class for the specific member ID provided. Jsonified member report will be returned based on the provided parameters and using the Member total wager amount method of Member class.  

```python
@app.route('/total_number_of_wagers/<member_id>')
```

First request is the total number of wagers. The endpoint can be provided with specific month and game ID as optional parameters. After assigning the main parameters(member ID) and optional parameters(all months\games if not provided), the app tries to create an object of Member class for the specific member ID provided. Jsonified member report will be returned based on the provided parameters and using the Member total number of wagers method of Member class.  


# Member Class

The class Member which gets three variables of 
1. member ID 
2. month 
3. game id

It has the following methods that are querying the database(Oracle):
1. total win amount 
2. total wager amount 
3. number of wagers

The class initioation creates the log file member.log based on the passed variables in class
initiation the condition of the sql query is being created. Then it tries to create an instance of
the class CallOracle to connect to database and return the requested value.
Each method has it's own main sql script which will be concatenated to the
conditional sql that was created on class initiation. 

# CallOracle class
This simple class is designed to connect to database, run a query and return the results and get diconnected from the database.
 