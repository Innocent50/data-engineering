drop table if exists examples;


create table examples
(
    id   serial
        constraint examples_pk
            primary key,
    name varchar
);
-- Create places table
CREATE TABLE places (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    county VARCHAR(255),
    country VARCHAR(255) NOT NULL
);

-- Create people table
CREATE TABLE people (
    id SERIAL PRIMARY KEY,
    given_name VARCHAR(255) NOT NULL,
    family_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    place_of_birth INTEGER,
    FOREIGN KEY (place_of_birth) REFERENCES places(id)
);

