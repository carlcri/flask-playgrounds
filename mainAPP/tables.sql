CREATE TABLE public.employees
(
    id serial NOT NULL,
    name character varying NOT NULL,
    lastname character varying,
    birthdate date,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.employees
    OWNER to postgres;

DROP TABLE IF EXISTS employees

CREATE TABLE employees
(
    id serial NOT NULL,
    name character varying NOT NULL,
    lastname character varying,
    birthdate date,
    PRIMARY KEY (id)
);


INSERT INTO employees(
	name, lastname, birthdate)
	VALUES ('alejo', 'vergel', '2002-10-31');


insert into employees (name, lastname, birthdate) values ('Delmer', 'Drance', '2023-05-17');
insert into employees (name, lastname, birthdate) values ('Hedwiga', 'Sparrow', '2023-10-05');
insert into employees (name, lastname, birthdate) values ('Iolande', 'Swalwel', '2022-11-23');
insert into employees (name, lastname, birthdate) values ('Bastien', 'Tireman', '2023-07-22');
insert into employees (name, lastname, birthdate) values ('Ronni', 'Ledgerton', '2022-12-10');
insert into employees (name, lastname, birthdate) values ('Garfield', 'Huonic', '2023-02-19');
insert into employees (name, lastname, birthdate) values ('Delmer', 'Darington', '2022-11-13');
insert into employees (name, lastname, birthdate) values ('Mirelle', 'McIan', '2023-05-18');
insert into employees (name, lastname, birthdate) values ('Elka', 'Meech', '2023-10-21');
insert into employees (name, lastname, birthdate) values ('Zara', 'Shambrooke', '2023-01-12');
insert into employees (name, lastname, birthdate) values ('Romain', 'Rew', '2022-10-30');
insert into employees (name, lastname, birthdate) values ('Leonelle', 'Cominello', '2023-05-29');
insert into employees (name, lastname, birthdate) values ('Lusa', 'Malicki', '2023-05-13');
insert into employees (name, lastname, birthdate) values ('Alasteir', 'Tredgold', '2023-07-06');
insert into employees (name, lastname, birthdate) values ('Elsie', 'Lathbury', '2022-12-25');
insert into employees (name, lastname, birthdate) values ('Farra', 'Swanwick', '2023-01-04');
insert into employees (name, lastname, birthdate) values ('Leicester', 'Manton', '2023-01-27');
insert into employees (name, lastname, birthdate) values ('Fraze', 'Edgcumbe', '2023-08-01');
insert into employees (name, lastname, birthdate) values ('Blinnie', 'Faraday', '2023-10-18');
insert into employees (name, lastname, birthdate) values ('Karmen', 'Binnall', '2023-09-19');
insert into employees (name, lastname, birthdate) values ('Selie', 'Paxforde', '2023-01-25');
insert into employees (name, lastname, birthdate) values ('Belia', 'Waddingham', null);
insert into employees (name, lastname, birthdate) values ('Abraham', 'Robertis', '2023-07-24');
insert into employees (name, lastname, birthdate) values ('Philbert', 'Ashe', '2023-01-22');
insert into employees (name, lastname, birthdate) values ('Ariel', 'Garlick', '2023-09-24');
insert into employees (name, lastname, birthdate) values ('Cahra', 'Yakuntzov', '2023-09-21');
insert into employees (name, lastname, birthdate) values ('Piper', 'Grieg', '2023-01-10');
insert into employees (name, lastname, birthdate) values ('Thalia', 'Gurden', '2023-06-02');
insert into employees (name, lastname, birthdate) values ('Hanna', 'Rangeley', '2023-01-22');
insert into employees (name, lastname, birthdate) values ('Lotty', 'O''Loughlin', '2022-11-15');
insert into employees (name, lastname, birthdate) values ('Georgy', 'Nelissen', '2023-04-01');
insert into employees (name, lastname, birthdate) values ('Ryon', 'Anslow', '2022-12-31');
insert into employees (name, lastname, birthdate) values ('Bartholomeus', 'Syplus', '2022-11-02');
insert into employees (name, lastname, birthdate) values ('Diarmid', 'Castletine', '2023-10-06');
insert into employees (name, lastname, birthdate) values ('Lynn', 'Gauntlett', '2023-08-09');
insert into employees (name, lastname, birthdate) values ('Flossy', null, '2023-09-24');
insert into employees (name, lastname, birthdate) values ('Sukey', 'Pester', '2023-09-29');
insert into employees (name, lastname, birthdate) values ('Ermina', 'Keeler', '2023-04-24');
insert into employees (name, lastname, birthdate) values ('Naoma', null, '2023-10-18');
insert into employees (name, lastname, birthdate) values ('Heywood', 'Cromett', null);
insert into employees (name, lastname, birthdate) values ('Imogen', 'Parcall', '2023-08-10');
insert into employees (name, lastname, birthdate) values ('Truman', 'Dalinder', null);
insert into employees (name, lastname, birthdate) values ('Celestine', 'Martensen', '2023-10-20');
insert into employees (name, lastname, birthdate) values ('Conrade', 'Minchella', '2022-11-12');
insert into employees (name, lastname, birthdate) values ('Jackson', 'Di Napoli', '2023-01-08');
insert into employees (name, lastname, birthdate) values ('Tripp', 'Wind', '2023-07-28');
insert into employees (name, lastname, birthdate) values ('Merell', 'Huck', null);
insert into employees (name, lastname, birthdate) values ('Bianca', 'Showen', '2023-05-31');