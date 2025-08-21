CREATE SEQUENCE note_id_seq;
ALTER TABLE notes
ALTER COLUMN note_id SET DEFAULT nextval('note_id_seq')