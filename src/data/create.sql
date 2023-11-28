-------------------------------------------------------------------------------------------------------------------

-- STANDARD SETTINGS

-------------------------------------------------------------------------------------------------------------------

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET xmloption = content;
SET client_min_messages = warning;

-------------------------------------------------------------------------------------------------------------------

DROP SCHEMA IF EXISTS postgres CASCADE;
CREATE SCHEMA postgres;
SET search_path TO postgres;

-------------------------------------------------------------------------------------------------------------------

DROP TABLE IF EXISTS factory CASCADE;
DROP TABLE IF EXISTS system CASCADE;
DROP TABLE IF EXISTS expansion CASCADE;
DROP TABLE IF EXISTS sensor CASCADE;
DROP TABLE IF EXISTS factory_systems CASCADE;
DROP TABLE IF EXISTS system_expansions CASCADE;
DROP TABLE IF EXISTS expansion_sensors CASCADE;

DROP TYPE IF EXISTS system_type CASCADE;
DROP TYPE IF EXISTS expansion_type CASCADE;
DROP TYPE IF EXISTS sensor_type CASCADE;

-------------------------------------------------------------------------------------------------------------------

-- TABLES & TYPES

-------------------------------------------------------------------------------------------------------------------

CREATE TYPE system_type AS ENUM ('Basic', 'Advanced', 'Expert');
CREATE TYPE expansion_type AS ENUM ('Station', 'Module', 'Component');
CREATE TYPE sensor_type AS ENUM ('Temperature', 'Flow', 'Pressure'); -- This should be used later on as a table
CREATE TYPE status AS ENUM ('Offline', 'Online', 'Working', 'Maintenance Required');

-------------------------------------------------------------------------------------------------------------------

CREATE TABLE system_model (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE, -- ex.: System 1
    manufacturer TEXT NOT NULL, -- ex.: Festo
    type system_type NOT NULL DEFAULT 'Basic'
);

CREATE TABLE expansion_model (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE, -- ex.: 3D printer
    manufacturer TEXT NOT NULL, -- ex.: Festo
    type expansion_type NOT NULL DEFAULT 'Station'
);

CREATE TABLE sensor_model (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE, -- ex.: Temperature sensor
    manufacturer TEXT NOT NULL, -- ex.: Festo
    type sensor_type NOT NULL,
    min_value REAL NOT NULL,
    max_value REAL NOT NULL
);

CREATE TABLE factory (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE, -- ex.: Facility 1
    tag TEXT NOT NULL UNIQUE, -- ex.: FAC1
    location TEXT NOT NULL DEFAULT 'N/A', -- ex.: PT01 Porto
    longitude FLOAT NOT NULL DEFAULT 0,
    latitude FLOAT NOT NULL DEFAULT 0
);

CREATE TABLE system (
    id SERIAL PRIMARY KEY,
    factory_id INTEGER NOT NULL REFERENCES factory(id),
    system_model_id INTEGER NOT NULL REFERENCES system_model(id),
    status status NOT NULL DEFAULT 'Offline'
);

CREATE TABLE expansion (
    id SERIAL PRIMARY KEY,
    system_id INTEGER NOT NULL REFERENCES system(id),
    expansion_model_id INTEGER NOT NULL REFERENCES expansion_model(id),
    status status NOT NULL DEFAULT 'Offline'
);

CREATE TABLE sensor (
    id SERIAL PRIMARY KEY,
    expansion_id INTEGER NOT NULL REFERENCES expansion(id),
    sensor_model_id INTEGER NOT NULL REFERENCES sensor_model(id),
    status status NOT NULL DEFAULT 'Offline'
);

CREATE TABLE task(
    id SERIAL PRIMARY KEY,
    system_id INTEGER NOT NULL REFERENCES system(id),
    name TEXT NOT NULL,
    duration INTEGER NOT NULL,
    energetic_costs INTEGER NOT NULL
);

-------------------------------------------------------------------------------------------------------------------


-------------------------------------------------------------------------------------------------------------------

-- TRIGGERS & FUNCTIONS

-------------------------------------------------------------------------------------------------------------------
