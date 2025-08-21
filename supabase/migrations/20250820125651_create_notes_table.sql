CREATE table notes (
  note_id int NOT null,
  user_id int not NULL,
  content varchar(255) NOT null,
  date_created timestamp,
  date_updated timestamp
);