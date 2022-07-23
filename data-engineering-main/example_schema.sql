-- noinspection SqlDialectInspectionForFile
-- noinspection SqlNoDataSourceInspectionForFile

drop table if exists examples;

create table examples
(
    id   serial
        constraint examples_pk
            primary key,
    name varchar
);


drop table  if exists places;

create table places
(
    id   serial
        constraint countries_pk
            primary key,
    city varchar,
    county varchar,
    country varchar
);

drop table  if exists people;

create table people
(
    id   serial
        constraint people_pk
            primary key,
    given_name varchar,
    family_name varchar,
    date_of_birth varchar,
    place_of_birth int references places(id)
);