CREATE TABLE speedtest (
    Download int,
    Upload int,
    Ping double(6,3),
    dt datetime
);
CREATE TABLE speedtest_errors (
    dt datetime,
    Errortype text
);