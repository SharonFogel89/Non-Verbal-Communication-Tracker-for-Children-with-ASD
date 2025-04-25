CREATE TABLE child (
  id SERIAL PRIMARY KEY,
  name VARCHAR,
  date_of_birth DATE,
  date_of_diagnosis DATE,
  notes TEXT
);

CREATE TABLE observer (
  id SERIAL PRIMARY KEY,
  name VARCHAR,
  relation VARCHAR,
  notes TEXT
);

CREATE TABLE category (
  id SERIAL PRIMARY KEY,
  name VARCHAR,
  description VARCHAR
);

CREATE TABLE behavior_type (
  id SERIAL PRIMARY KEY,
  name VARCHAR,
  description VARCHAR,
  is_milestone BOOLEAN
);

CREATE TABLE behavior_entry (
  id SERIAL PRIMARY KEY,
  child_id INT REFERENCES child(id),
  observer_id INT REFERENCES observer(id),
  behavior_type_id INT REFERENCES behavior_type(id),
  category_id INT REFERENCES category(id),
  behavior_date TIMESTAMP,
  notes TEXT,
  duration_sec INT,
  consolidated BOOLEAN,
  base BOOLEAN
);

CREATE TABLE alert (
  id SERIAL PRIMARY KEY,
  child_id INT REFERENCES child(id),
  alert_date TIMESTAMP,
  solved BOOLEAN,
  description TEXT
);

CREATE TABLE translation (
  id SERIAL PRIMARY KEY,
  language_code VARCHAR,
  original_text VARCHAR,
  translated_text VARCHAR
);
