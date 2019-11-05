Django Test Project By Zhao SongXun
=============

This project was created only for testing purpose by Zhao SongXun.

Installation
------------

First, prepare your python virtual environment and activate.

```bash
virtual venv
source venv/bin/activate
```

Please unzip the project archive and move into the unzipped folder.
```bash
unzip project.zip
cd project
```
Install all required packages and you are ready to go!
```bash
pip install -r requirements/default.txt
```

Usage
-----
Once your virtual environment is ready, you can run django project.
```bash
python manage.py runserver 0.0.0.0:8000
```

You can also run test using the following command.
```bash
python manage.py test
```

API Lists
-----------
API base URL is ~/api/
* Create a company  
```text
POST companies/  
```
Example request:
```json
{"name": "blabla", "locality": "blabla", "city": 1, "state": 1, postal_code: "111111"}
```

* Retrieve a company  
```text
GET companies/{pk}
```

* Update a company
```
PUT companies/{pk}  
```
Example request:
```json
{"name": "blabla", "locality": "blabla", "city": 1, "state": 1, postal_code: "111111"}
```

* Delete a company  
```text
DELETE companies/{pk}  
```

* Get a company with name  
```text
GET companies/?name={name}
```
* Get companies with city  
```text
GET companies/?city_id={city id}
```

* Get postal codes with more than X of companies in it.  
```text
GET postal_codes/?num_companies={X}
```

Prerequisites
-----------
Make sure you installed following prerequisites on your test machine
* Python >3.0
