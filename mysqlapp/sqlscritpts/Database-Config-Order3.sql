CREATE TABLE ZillowListingsAssociations (Id BIGINT NOT NULL, Price INT, SaleStatus VARCHAR(50),
timestamp DATETIME NOT NULL, PRIMARY KEY(Id, timestamp), FOREIGN KEY (Id) REFERENCES ZillowListings(Id));

CREATE TABLE AirbnbDataAssociations (Id BIGINT NOT NULL, Price INT,
timestamp DATETIME NOT NULL, PRIMARY KEY(Id, timestamp), FOREIGN KEY (Id) REFERENCES AirbnbData(Id));

CREATE TABLE RemaxListingsAssociations (Id VARCHAR(50) NOT NULL, Price INT, SaleStatus VARCHAR(50),
timestamp DATETIME NOT NULL, PRIMARY KEY(Id, timestamp), FOREIGN KEY (Id) REFERENCES RemaxListings(Id));

CREATE TABLE YelpBusinessData (Id VARCHAR(50) NOT NULL, Categories JSON, PriceRange VARCHAR(5), 
BusinessUrl VARCHAR(2083), PRIMARY KEY(Id), FOREIGN KEY (Id) REFERENCES YelpData(Id));

CREATE TABLE ZillowListingsWalkscore (Id BIGINT NOT NULL, 
WalkScore DECIMAL(4,2), TransitScore DECIMAL(4,2), PRIMARY KEY(Id), 
FOREIGN KEY (Id) REFERENCES ZillowListings(Id));

CREATE TABLE ZillowListingsAmeneties (Id BIGINT NOT NULL, YelpDataId VARCHAR(50) NOT NULL,
Distance DECIMAL(4,2) NOT NULL, PRIMARY KEY(Id, YelpDataId), 
FOREIGN KEY (Id) REFERENCES ZillowListings(Id), FOREIGN KEY (YelpDataId) REFERENCES YelpData(Id));

CREATE TABLE ZillowListingsSchools (Id BIGINT NOT NULL, SchoolId BIGINT NOT NULL,
Distance DECIMAL(4,2) NOT NULL, PRIMARY KEY(Id, SchoolId), 
FOREIGN KEY (Id) REFERENCES ZillowListings(Id), 
FOREIGN KEY (SchoolId) REFERENCES SchoolData(Id));

CREATE TABLE ZillowListingsColleges (Id BIGINT NOT NULL, CollegeName VARCHAR(100) NOT NULL,
Distance DECIMAL(4,2) NOT NULL, PRIMARY KEY(Id, CollegeName), 
FOREIGN KEY (Id) REFERENCES ZillowListings(Id), 
FOREIGN KEY (CollegeName) REFERENCES CollegesData(CollegeName));

CREATE TABLE ZillowListingsUniversities (Id BIGINT NOT NULL, UniversityName VARCHAR(100) NOT NULL,
Distance DECIMAL(4,2) NOT NULL, PRIMARY KEY(Id, UniversityName), 
FOREIGN KEY (Id) REFERENCES ZillowListings(Id), 
FOREIGN KEY (UniversityName) REFERENCES UniversitiesData(UniversityName));

CREATE TABLE ZillowListingsAirbnb (Id BIGINT NOT NULL, AirbnbId BIGINT NOT NULL,
Distance DECIMAL(4,2) NOT NULL, PRIMARY KEY(Id,  AirbnbId), 
FOREIGN KEY (Id) REFERENCES ZillowListings(Id), 
FOREIGN KEY (AirbnbId) REFERENCES AirbnbData(Id));

CREATE TABLE RemaxListingsWalkscore (Id VARCHAR(50) NOT NULL, 
WalkScore DECIMAL(4,2), TransitScore DECIMAL(4,2), PRIMARY KEY(Id), 
FOREIGN KEY (Id) REFERENCES RemaxListings(Id));

CREATE TABLE RemaxListingsAmeneties (Id VARCHAR(50) NOT NULL, YelpDataId VARCHAR(50) NOT NULL,
Distance DECIMAL(4,2) NOT NULL, PRIMARY KEY(Id, YelpDataId), 
FOREIGN KEY (Id) REFERENCES RemaxListings(Id), 
FOREIGN KEY (YelpDataId) REFERENCES YelpData(Id));

CREATE TABLE RemaxListingsSchools (Id VARCHAR(50) NOT NULL, SchoolId BIGINT NOT NULL,
Distance DECIMAL(4,2) NOT NULL, PRIMARY KEY(Id, SchoolId), 
FOREIGN KEY (Id) REFERENCES RemaxListings(Id), 
FOREIGN KEY (SchoolId) REFERENCES SchoolData(Id));

CREATE TABLE RemaxListingsColleges (Id VARCHAR(50) NOT NULL, CollegeName VARCHAR(100) NOT NULL,
Distance DECIMAL(4,2) NOT NULL, PRIMARY KEY(Id, CollegeName), 
FOREIGN KEY (Id) REFERENCES RemaxListings(Id), 
FOREIGN KEY (CollegeName) REFERENCES CollegesData(CollegeName));

CREATE TABLE RemaxListingsUniversities (Id VARCHAR(50) NOT NULL, UniversityName VARCHAR(100) NOT NULL,
Distance DECIMAL(4,2) NOT NULL, PRIMARY KEY(Id, UniversityName), 
FOREIGN KEY (Id) REFERENCES RemaxListings(Id), 
FOREIGN KEY (UniversityName) REFERENCES UniversitiesData(UniversityName));

CREATE TABLE RemaxListingsAirbnb (Id BIGINT NOT NULL, AirbnbId BIGINT NOT NULL,
Distance DECIMAL(4,2) NOT NULL, PRIMARY KEY(Id,  AirbnbId), 
FOREIGN KEY (Id) REFERENCES RemaxListings(Id), 
FOREIGN KEY (AirbnbId) REFERENCES AirbnbData(Id));