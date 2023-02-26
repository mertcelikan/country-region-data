# COUNTRY REGIONS DATA
Get current country and region datas and save it to MySQL

## Table Of Content

  * [Package Installs](#package-installs)
  * [Usage](#Usage)
  * [Files](#files)
  * [License](#license)

## Package Installs

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```


## Usage
After making the necessary downloads, run the code below

In the main.py file you can add more country in main if you want.

```python
python3 main.py
```



Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
## Files
1) Routers
2) MySqldatabase
3) Worker
4) Tables

1 - Routers

That basicly request to api [geodb-cities](https://rapidapi.com/wirefreethought/api/geodb-cities)

2 - MySqldatabase

Create connection and contains the necessary functions. Insert, update, connect etc.

3 - Worker

It performs the database writing process for the requests returned from the API. If the incoming country and region information is in the database, it checks whether it is up to date.

4 - Tables

To set up the necessary tables. Note: you have to install the tables yourself.


## License
[MIT](https://choosealicense.com/licenses/mit/)
