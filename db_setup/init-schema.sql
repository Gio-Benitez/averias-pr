CREATE USER appuser WITH PASSWORD 'appass';
CREATE DATABASE averiaspr_db;
GRANT ALL PRIVILEGES ON DATABASE averiaspr_db TO appuser;

\c averiaspr_db;

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    admin_id INT NOT NULL,
    user_email VARCHAR(100) NOT NULL,
    user_pass_hash VARCHAR(100) NOT NULL,
    user_salt VARCHAR(100) NOT NULL,
    user_fname VARCHAR(100) NOT NULL,
    user_lname VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS report (
    report_id SERIAL PRIMARY KEY,
    report_date VARCHAR(100) NOT NULL,
    report_email VARCHAR(100) NOT NULL,
    report_status VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS municipality (
    mun_id SERIAL PRIMARY KEY,
    mun_name VARCHAR(100) NOT NULL,
    mun_population INT NOT NULL,
    mun_size_area INT NOT NULL
);

CREATE TABLE IF NOT EXISTS report_data(
    data_id SERIAL PRIMARY KEY,
    address_line_1 VARCHAR(100) NOT NULL,
    address_line_2 VARCHAR(100) NOT NULL,
    report_category VARCHAR(100) NOT NULL,
    city_name VARCHAR(100) NOT NULL,
    zipcode VARCHAR(100) NOT NULL,
    geo_data_lat DECIMAL NOT NULL,
    geo_data_long DECIMAL NOT NULL,
    image_src VARCHAR(100) NOT NULL
);