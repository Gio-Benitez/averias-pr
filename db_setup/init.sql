CREATE SCHEMA AVERIASPR_DATABASE;
GRANT USAGE ON SCHEMA AVERIASPR_DATABASE TO root;
SET search_path = AVERIASPR_DATABASE;

CREATE TABLE user (
    id SERIAL PRIMARY KEY,
    fname VARCHAR(100) NOT NULL,
    lname VARCHAR(100) NOT NULL,
    -- email VARCHAR(100) NOT NULL,
    -- password VARCHAR(100) NOT NULL,
);

INSERT INTO user (fname, lname) VALUES
  ('Mkyong', 'Asshole'),
  ('Ali', 'Asshole'),
  ('Teoh', 'Asshole');

-- CREATE TABLE report (
--     id SERIAL PRIMARY KEY,
--     report_date DATE NOT NULL,
--     email VARCHAR(100) NOT NULL,
--     status VARCHAR(100) NOT NULL
-- );

-- CREATE TABLE report_data (
--     id SERIAL PRIMARY KEY,
--     address1 VARCHAR(100) NOT NULL,
--     address2 VARCHAR(100) NOT NULL,
--     category VARCHAR(100) NOT NULL,
--     city VARCHAR(100) NOT NULL,
--     zipcode VARCHAR(100) NOT NULL,
--     lattitude DECIMAL NOT NULL,
--     longitude DECIMAL NOT NULL,
--     image VARCHAR(100) NOT NULL
-- );

-- CREATE TABLE municipality (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     population INT NOT NULL,
--     area INT NOT NULL
-- );
