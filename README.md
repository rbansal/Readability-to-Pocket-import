# Readability-to-Pocket-import

Python script to import an exported JSON file from Readability into Pocket.

#### Usage:

1. Sign up for a developer api key here: http://getpocket.com/api/signup/

2. Export JSON file containing Readability articles here: http://www.readability.com/account/export

3. Run the following code using your Pocket username and password:
 
```
importReadability.py username password apikey jsonfile
```
#### Example:
```
python importReadability.py Username Password 12345api6789key012345 ~/Downloads/Readability.json
```

#### Output:
* 200 - Request was successful
* 400 - Invalid request, please make sure you follow the documentation for proper syntax
* 401 - Username and/or password is incorrect
* 403 - Rate limit exceeded, please wait a little bit before resubmitting
* 503 - Read It Later's sync server is down for scheduled maintenance.

#### Contributors:
1. [rbansal](https://github.com/rbansal)