# Readability-to-Pocket-import

Python script to import an exported JSON file from Readability into Pocket.

#### Usage:

1.) Sign up for a developer api key here: http://getpocket.com/api/signup/

2.) Export JSON file containing Readability articles here: http://www.readability.com/account/export

3.) Run the following code using your Pocket username and password:
 
```
import.py username password apikey jsonfile
```
#### Example:
```
python import.py Username Password 12345api6789key012345 ~/Downloads/Readability.json
```
#### Contributors:
1) [rbansal](https://github.com/rbansal)