# GeoDjango
A mandatory GeoDjango requirement is GDAL.

$ sudo apt-get install gdal-bin
$ sudo apt-get install libgdal-de

Export path
$ export CPLUS_INCLUDE_PATH=/usr/include/gdal
$ export C_INCLUDE_PATH=/usr/include/gdal
$ pip install GDAL



In order to use PostGIS as a database backend,
we need to install the PostgreSQL C client library
$ sudo apt-get install libpq5

Install PostgreSQL
$ sudo apt-get install postgis*

create database user
$ sudo -u postgres psql
$ postgres=# ALTER USER postgres PASSWORD 'password';

Install dependencies 
$ pip install -r requirements.txt
To run server
$ python manage.py runserver

Navigate to add markers on map.
	http://127.0.0.1:8000/admin/markers/marker/add/  


these markers will go to PostgreSQL database 

Navigate to to see added markers.
	http://127.0.0.1:8000/markers/map/
	
By Running python file get_weather_data.py you can see data fetched 
from API "https://api.weather.gov/gridpoints/ABQ/31,80/forecast"
$ python get_weather_data.py

In terminal you can see Data from server in JSON Parsed
Format.
