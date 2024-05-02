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
    mun_size_area DECIMAL(10, 2),
    num_reports INT,
    most_common_category VARCHAR(50),
    resolved_reports INT
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
    Geo_Data_Lat DECIMAL(10, 6),
    Geo_Data_Long DECIMAL(10, 6),
    image_src TEXT,
    report_date DATE NOT NULL,
    report_status VARCHAR(20) NOT NULL
);

-- inserts for static tables --
INSERT INTO category (category_name) VALUES
('Carretera Dañada'),
('Poste Caido'),
('Deslizamiento'),
('Peligro de Deslizamiento'),
('Servicio de Agua'),
('Servicio de energía eléctrica');


INSERT INTO municipality (mun_name, mun_population, mun_size_area, num_reports, most_common_category, resolved_reports) VALUES
('Adjuntas', 18010, 173     , 0, 'Ninguna', 0),
('Aguada', 38108, 80        , 0, 'Ninguna', 0),
('Aguadilla', 55046, 95     , 0, 'Ninguna', 0),
('Aguas Buenas', 24189, 78  , 0, 'Ninguna', 0),
('Aibonito', 24633, 81      , 0, 'Ninguna', 0),
('Añasco', 25570, 102       , 0, 'Ninguna', 0),
('Arecibo', 87637, 326      , 0, 'Ninguna', 0),
('Arroyo', 15817, 39        , 0, 'Ninguna', 0),
('Barceloneta', 22669, 48   , 0, 'Ninguna', 0),
('Barranquitas', 28981, 89  , 0, 'Ninguna', 0),
('Bayamón', 184954, 115     , 0, 'Ninguna', 0),
('Cabo Rojo', 47121, 182    , 0, 'Ninguna', 0),
('Caguas', 127072, 152      , 0, 'Ninguna', 0),
('Camuy', 32818, 120        , 0, 'Ninguna', 0),
('Canóvanas', 42326, 85     , 0, 'Ninguna', 0),
('Carolina', 154557, 117    , 0, 'Ninguna', 0),
('Cataño', 23113, 13        , 0, 'Ninguna', 0),
('Cayey', 41587, 135        , 0, 'Ninguna', 0),
('Ceiba', 11284, 75         , 0, 'Ninguna', 0),
('Ciales', 16972, 172       , 0, 'Ninguna', 0),
('Cidra', 39957, 93         , 0, 'Ninguna', 0),
('Coamo', 34603, 202        , 0, 'Ninguna', 0),
('Comerío', 18867, 74       , 0, 'Ninguna', 0),
('Corozal', 34551, 110      , 0, 'Ninguna', 0),
('Culebra', 1790, 30        , 0, 'Ninguna', 0),
('Dorado', 35902, 60        , 0, 'Ninguna', 0),
('Fajardo', 32087, 77       , 0, 'Ninguna', 0),
('Florida', 11682, 39       , 0, 'Ninguna', 0),
('Guánica', 13686, 96       , 0, 'Ninguna', 0),
('Guayama', 36474, 168      , 0, 'Ninguna', 0),
('Guayanilla', 17739, 109   , 0, 'Ninguna', 0),
('Guaynabo', 89758, 71      , 0, 'Ninguna', 0),
('Gurabo', 40589, 72        , 0, 'Ninguna', 0),
('Hatillo', 38447, 108      , 0, 'Ninguna', 0),
('Hormigueros', 15618, 29   , 0, 'Ninguna', 0),
('Humacao', 50824, 116      , 0, 'Ninguna', 0),
('Isabela', 42939, 143      , 0, 'Ninguna', 0),
('Jayuya', 14771, 115       , 0, 'Ninguna', 0),
('Juana Díaz', 46499, 156   , 0, 'Ninguna', 0),
('Juncos', 37030, 69        , 0, 'Ninguna', 0),
('Lajas', 23279, 155        , 0, 'Ninguna', 0),
('Lares', 28090, 159        , 0, 'Ninguna', 0),
('Las Marías', 8856, 120    , 0, 'Ninguna', 0),
('Las Piedras', 35179, 88   , 0, 'Ninguna', 0),
('Loíza', 23608, 50         , 0, 'Ninguna', 0),
('Luquillo', 17766, 67      , 0, 'Ninguna', 0),
('Manatí', 39451, 117       , 0, 'Ninguna', 0),
('Maricao', 4752, 95        , 0, 'Ninguna', 0),
('Maunabo', 10581, 55       , 0, 'Ninguna', 0),
('Mayagüez', 72843, 201     , 0, 'Ninguna', 0),
('Moca', 37455, 130         , 0, 'Ninguna', 0),
('Morovis', 28704, 101      , 0, 'Ninguna', 0),
('Naguabo', 23384, 134      , 0, 'Ninguna', 0),
('Naranjito', 29246, 71     , 0, 'Ninguna', 0),
('Orocovis', 21431, 165     , 0, 'Ninguna', 0),
('Patillas', 15937, 121     , 0, 'Ninguna', 0),
('Peñuelas', 20349, 116     , 0, 'Ninguna', 0),
('Ponce', 137149, 297       , 0, 'Ninguna', 0),
('Quebradillas', 23619, 59  , 0, 'Ninguna', 0),
('Rincón', 15206, 37        , 0, 'Ninguna', 0),
('Río Grande', 47005, 157   , 0, 'Ninguna', 0),
('Sabana Grande', 22701, 93 , 0, 'Ninguna', 0),
('Salinas', 25722, 180      , 0, 'Ninguna', 0),
('San Germán', 31824, 141   , 0, 'Ninguna', 0),
('San Juan', 341667, 124    , 0, 'Ninguna', 0),
('San Lorenzo', 37671, 138  , 0, 'Ninguna', 0),
('San Sebastián', 39312, 182, 0, 'Ninguna', 0),
('Santa Isabel', 20269, 88  , 0, 'Ninguna', 0),
('Toa Alta', 66842, 70      , 0, 'Ninguna', 0),
('Toa Baja', 75092, 60      , 0, 'Ninguna', 0),
('Trujillo Alto', 67687, 54 , 0, 'Ninguna', 0),
('Utuado', 28225, 294       , 0, 'Ninguna', 0),
('Vega Alta', 35367, 72     , 0, 'Ninguna', 0),
('Vega Baja', 54357, 119    , 0, 'Ninguna', 0),
('Vieques', 8236, 131       , 0, 'Ninguna', 0),
('Villalba', 22041, 92      , 0, 'Ninguna', 0),
('Yabucoa', 30329, 143      , 0, 'Ninguna', 0),
('Yauco', 34048, 177        , 0, 'Ninguna', 0);





