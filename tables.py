create_table_query_country_details = """
CREATE TABLE Country_Details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    capital VARCHAR(255),
    code VARCHAR(255),
    callingCode VARCHAR(255),
    currencyCodes VARCHAR(255),
    flagImageUri VARCHAR(255),
    country_name VARCHAR(255),
    numRegions INT,
    wikiDataId VARCHAR(255)
);
"""
create_table_query_regions = """
CREATE TABLE Country_Regions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    countryCode VARCHAR(255),
    fipsCode VARCHAR(255),
    isoCode VARCHAR(255),
    region_name VARCHAR(255),
    wikiDataId VARCHAR(255)
);
"""

#db.createtable(create_table_query_country_details,"Country_Details")

#db.createtable(create_table_query_regions,"Country_Regions")