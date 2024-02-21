CREATE TABLE hospital (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    planning_area INT NOT NULL,
    control_type VARCHAR(100) NOT NULL,
    type VARCHAR(100) NOT NULL,
    phone VARCHAR(100) NOT NULL,
    address VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    zipcode VARCHAR(100) NOT NULL,
    ceo VARCHAR(100) NOT NULL
);

CREATE TABLE staff (
    id SERIAL PRIMARY KEY,
    hid INT REFERENCES hospital(id),
    productive_hours_per_patient FLOAT NOT NULL,
    productive_hours INT NOT NULL,
    position VARCHAR(100) NOT NULL
);

CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    operational BIGINT NOT NULL,
    professional INT NOT NULL
);

CREATE TABLE outpatient_revenue (
    id SERIAL PRIMARY KEY,
    medicare_traditional INT NOT NULL,
    medicare_care INT NOT NULL,
    medi_traditional INT NOT NULL,
    medi_care INT NOT NULL
);

CREATE TABLE discharges (
    id SERIAL PRIMARY KEY,
    medicare_traditional INT NOT NULL,
    medicare_care INT NOT NULL,
    medi_traditional INT NOT NULL,
    medi_care INT NOT NULL
);

CREATE TABLE utilization (
    id SERIAL PRIMARY KEY,
    available_beds INT NOT NULL,
    staffed_beds INT NOT NULL,
    license_beds INT NOT NULL
);

CREATE TABLE visits (
    id SERIAL PRIMARY KEY,
    medicare_traditional INT NOT NULL,
    medicare_care INT NOT NULL,
    medi_traditional INT NOT NULL,
    medi_care INT NOT NULL
);

CREATE TABLE patient_days (
    id SERIAL PRIMARY KEY,
    medicare_traditional INT NOT NULL,
    medicare_care INT NOT NULL,
    medi_traditional INT NOT NULL,
    medi_care INT NOT NULL
);

CREATE TABLE inpatient_revenue (
    id SERIAL PRIMARY KEY,
    medicare_traditional INT NOT NULL,
    medicare_care INT NOT NULL,
    medi_traditional INT NOT NULL,
    medi_care INT NOT NULL
);

CREATE TABLE report (
    id SERIAL PRIMARY KEY,
    year INT NOT NULL,
    quarter INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE TABLE report_content (
    id SERIAL PRIMARY KEY,
    current_status VARCHAR(100) NOT NULL,
    rid INT REFERENCES report(id),
    hid INT REFERENCES hospital(id),
    outid INT REFERENCES outpatient_revenue(id),
    visid INT REFERENCES visits(id),
    expid INT REFERENCES expenses(id),
    inid INT REFERENCES inpatient_revenue(id),
    utilid INT REFERENCES utilization(id),
    patid INT REFERENCES patient_days(id),
    disid INT REFERENCES discharges(id)
);
