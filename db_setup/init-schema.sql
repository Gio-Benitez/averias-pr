-- CREATE USER appuser WITH PASSWORD 'appass';
-- CREATE DATABASE averiaspr_db;
-- GRANT ALL PRIVILEGES ON DATABASE averiaspr_db TO appuser;
--
-- \c averiaspr_db;

-- CREATE TABLE IF NOT EXISTS my_table (
--     client_id character varying(36) NOT NULL,
--     value character varying(255)
-- );
--

CREATE TABLE "user" (
    user_id SERIAL PRIMARY KEY,
    user_email VARCHAR(255) UNIQUE NOT NULL,
    user_pass_hash VARCHAR(255) NOT NULL,
    user_salt VARCHAR(255) NOT NULL,
    user_fname VARCHAR(100),
    user_lname VARCHAR(100)
);

CREATE TABLE report_data (
    data_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES "user"(user_id),
    Address_Line_1 VARCHAR(255),
    Address_Line_2 VARCHAR(255),
    Report_category VARCHAR(100),
    City_name VARCHAR(100),
    Zipcode VARCHAR(20),
    Geo_Data_Lat DECIMAL(10, 6),
    Geo_Data_Long DECIMAL(10, 6),
    image_src TEXT
);
