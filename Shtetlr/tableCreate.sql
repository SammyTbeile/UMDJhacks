
CREATE TABLE users (
    username    VARCHAR(20),
    name        VARCHAR(20),
    gender      CHAR(1),
    pricerange  INT(5),
    location    VARCHAR(20),
    PRIMARY KEY (username)
);
CREATE TABLE apts (
    aptID       INT(10),
    location    VARCHAR(20),
    bedrooms    INT(1),
    bathrooms   INT(1),
    rent        INT(5),
    laundry     CHAR(1),
    ac          CHAR(1),
    gym         CHAR(1),
    features    VARCHAR(500),
    ss          CHAR(1),
    sk          CHAR(1),
    pitch       VARCHAR(10000),
    availableRoom VARCHAR(500),
    PRIMARY KEY (aptID)
);
CREATE TABLE photos(
    username    VARCHAR(20),
    aptID       INT(10),
    photos      CHAR(80)
);