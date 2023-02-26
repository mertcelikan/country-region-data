from routers import *
from mysqlsatabase import MySQLDatabase

# MySQL connects and runs the server.
db = MySQLDatabase('127.0.0.1', 'root', 'my-secret-pw', 'test_db')
db.connect()

def getCountryInfo(country):

    # Returns country details
    data = country_details(country)

    # Country name is searched in the table
    countrySearch = db.search("Country_Details", "code", data["code"])

    # If country exist in the table
    if len(countrySearch) > 0:
        # The below code check if any data changes in that country
        i = 1
        for x in data:
            if data[x] != countrySearch[0][i]:
                # There is a change in data!
                if type(data[x]) == type(countrySearch[0][i]):
                    where = {x: data[x]}
                    db.update("Country_Details", data, where)
            i += 1
    # Country not in the table
    else:
        temp_data = {
            'capital': data["capital"],
            'code': data["code"],
            'callingCode': data["callingCode"],
            'currencyCodes': data["currencyCodes"][0],
            'flagImageUri': data["flagImageUri"],
            'country_name': data["name"],
            'numRegions': data["numRegions"],
            'wikiDataId': data["wikiDataId"]
        }
        db.insert("Country_Details", temp_data)

def getRegionsInfo(country):

    # Returns country details
    data = country_regions(country)
    for region in data:

        # Region name is searched in the table
        regionSearch = db.search("Country_Regions", "region_name", region["name"])

        # Region is in the table
        if len(regionSearch) > 0:
            # The below code check if any data changes in that region
            i = 1
            for x in region:
                if region[x] != regionSearch[0][i]:
                    # There is a change in data!
                    if type(region[x]) == type(regionSearch[0][i]):
                        where = {x: data[x]}
                        db.update("Country_Details", data, where)
                i += 1
        # Region is not in the table
        else:
            temp_data = {
                'countryCode': region["countryCode"],
                'fipsCode': region["fipsCode"],
                'isoCode': region["isoCode"],
                'region_name': region["name"],
                'wikiDataId': region["wikiDataId"],
            }
            db.insert("Country_Regions", temp_data)


























def droptable():
    mycursor = db.conn.cursor()

    #mycursor.execute("DROP TABLE Country_Details")
    mycursor.execute("DROP TABLE Country_Regions")

#droptable()

def deleteable():
    mycursor = db.conn.cursor()

    # Tüm verileri silme işlemi
    mycursor.execute("DELETE FROM Country_Details")

    # Değişiklikleri kaydetme
    db.conn.commit()

    # Bağlantıyı kapatma
    mycursor.close()
    db.conn.close()

#deleteable()


def printtable():
    cursor = db.conn.cursor()

    # Tablo sütun bilgilerini al
    table_name = "Country_Regions"
    cursor.execute(f"SHOW COLUMNS FROM {table_name}")
    columns = cursor.fetchall()

    # Sütun bilgilerini yazdır
    for column in columns:
        print(column)

#printtable()

"""mycursor = db.conn.cursor()

# Tabloları listeleme
mycursor.execute("SHOW TABLES")

for table in mycursor:
  print(table)"""