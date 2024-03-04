CREATE USER appuser WITH PASSWORD 'appass';
CREATE DATABASE averiaspr_db;
GRANT ALL PRIVILEGES ON DATABASE averiaspr_db TO appuser;

\c averiaspr_db;

CREATE TABLE IF NOT EXISTS my_table (
    client_id character varying(36) NOT NULL,
    value character varying(255)
);