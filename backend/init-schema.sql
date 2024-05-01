-- CREATE USER appuser WITH PASSWORD 'appass';
-- CREATE DATABASE averiaspr_db;
-- GRANT ALL PRIVILEGES ON DATABASE averiaspr_db TO appuser;

-- \c averiaspr_db;

-- CREATE TABLE IF NOT EXISTS my_table (
--     client_id character varying(36) NOT NULL,
--     value character varying(255)
-- );
--

-- Create the user table
CREATE TABLE if not exists "user" (
    user_id SERIAL PRIMARY KEY,
    user_email VARCHAR(255) UNIQUE NOT NULL,
    user_pass VARCHAR(255) NOT NULL,
    user_fname VARCHAR(100),
    user_lname VARCHAR(100),
    admin_id bool
);

-- Create the municipalities table
CREATE TABLE if not exists municipality (
    mun_id SERIAL PRIMARY KEY,
    mun_name VARCHAR(255) NOT NULL,
    mun_population INT,
    mun_size_area DECIMAL(10, 2)
);

create TABLE if not exists category(
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL
);

-- Create the report_data table
CREATE TABLE if not exists report_data (
    data_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES "user"(user_id),
    mun_id INT REFERENCES municipality(mun_id),
    category_id INT REFERENCES category(category_id),
    Address_Line_1 VARCHAR(255),
    Address_Line_2 VARCHAR(255),
    Report_category VARCHAR(100),
    City_name VARCHAR(100),
    Zipcode VARCHAR(20),
    Geo_Data_Lat DECIMAL(10, 6),
    Geo_Data_Long DECIMAL(10, 6),
    img_src VARCHAR(255)
);


-- Create the report table
CREATE TABLE if not exists report (
    report_id SERIAL PRIMARY KEY,
    data_id INT REFERENCES report_data(data_id),
    report_date DATE NOT NULL,
    report_email VARCHAR(255) NOT NULL,
    report_status VARCHAR(20) NOT NULL,
    CONSTRAINT fk_report_data FOREIGN KEY (report_id) REFERENCES report_data(data_id) ON DELETE CASCADE
);


-- inserts for static tables --
INSERT INTO category (category_name) VALUES
('Pothole'),
('Light post damages'),
('Landslide/potential landslide'),
('Water outage'),
('Power outage');


INSERT INTO municipality (mun_name, mun_population, mun_size_area) VALUES
('Adjuntas', 18010, 173),
('Aguada', 38108, 80),
('Aguadilla', 55046, 95),
('Aguas Buenas', 24189, 78),
('Aibonito', 24633, 81),
('Añasco', 25570, 102),
('Arecibo', 87637, 326),
('Arroyo', 15817, 39),
('Barceloneta', 22669, 48),
('Barranquitas', 28981, 89),
('Bayamón', 184954, 115),
('Cabo Rojo', 47121, 182),
('Caguas', 127072, 152),
('Camuy', 32818, 120),
('Canóvanas', 42326, 85),
('Carolina', 154557, 117),
('Cataño', 23113, 13),
('Cayey', 41587, 135),
('Ceiba', 11284, 75),
('Ciales', 16972, 172),
('Cidra', 39957, 93),
('Coamo', 34603, 202),
('Comerío', 18867, 74),
('Corozal', 34551, 110),
('Culebra', 1790, 30),
('Dorado', 35902, 60),
('Fajardo', 32087, 77),
('Florida', 11682, 39),
('Guánica', 13686, 96),
('Guayama', 36474, 168),
('Guayanilla', 17739, 109),
('Guaynabo', 89758, 71),
('Gurabo', 40589, 72),
('Hatillo', 38447, 108),
('Hormigueros', 15618, 29),
('Humacao', 50824, 116),
('Isabela', 42939, 143),
('Jayuya', 14771, 115),
('Juana Díaz', 46499, 156),
('Juncos', 37030, 69),
('Lajas', 23279, 155),
('Lares', 28090, 159),
('Las Marías', 8856, 120),
('Las Piedras', 35179, 88),
('Loíza', 23608, 50),
('Luquillo', 17766, 67),
('Manatí', 39451, 117),
('Maricao', 4752, 95),
('Maunabo', 10581, 55),
('Mayagüez', 72843, 201),
('Moca', 37455, 130),
('Morovis', 28704, 101),
('Naguabo', 23384, 134),
('Naranjito', 29246, 71),
('Orocovis', 21431, 165),
('Patillas', 15937, 121),
('Peñuelas', 20349, 116),
('Ponce', 137149, 297),
('Quebradillas', 23619, 59),
('Rincón', 15206, 37),
('Río Grande', 47005, 157),
('Sabana Grande', 22701, 93),
('Salinas', 25722, 180),
('San Germán', 31824, 141),
('San Juan', 341667, 124),
('San Lorenzo', 37671, 138),
('San Sebastián', 39312, 182),
('Santa Isabel', 20269, 88),
('Toa Alta', 66842, 70),
('Toa Baja', 75092, 60),
('Trujillo Alto', 67687, 54),
('Utuado', 28225, 294),
('Vega Alta', 35367, 72),
('Vega Baja', 54357, 119),
('Vieques', 8236, 131),
('Villalba', 22041, 92),
('Yabucoa', 30329, 143),
('Yauco', 34048, 177);





