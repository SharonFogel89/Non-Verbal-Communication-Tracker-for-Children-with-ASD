

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
INSERT INTO category (name, description) VALUES ('Verbal Behavior', 'Behaviors related to speech, requests, and vocalizations');
INSERT INTO category (name, description) VALUES ('Motor Imitation', 'Physically imitated actions, with or without objects');
INSERT INTO category (name, description) VALUES ('Social Skills', 'Behaviors involving interaction with other people');
INSERT INTO category (name, description) VALUES ('Functional and Symbolic Play', 'Use of toys and imaginative play');
INSERT INTO category (name, description) VALUES ('Language Comprehension', 'Responding to commands, recognizing words');
INSERT INTO category (name, description) VALUES ('Cognitive Skills', 'Reasoning, sequencing, classification');
INSERT INTO category (name, description) VALUES ('Self-Care', 'Practical daily life activities');
INSERT INTO category (name, description) VALUES ('Sensory', 'Reactions to and seeking of sensory stimuli');
INSERT INTO category (name, description) VALUES ('Inappropriate Behaviors', 'Self-aggression, shouting, etc.');


CREATE TABLE behavior_type (
  id SERIAL PRIMARY KEY,
  name VARCHAR,
  description VARCHAR,
  category_id INT REFERENCES category(id),
  is_milestone BOOLEAN
);


INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Vocalization', 'Making intentional sounds or syllables', 1, TRUE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Requesting with gesture', 'Pointing or signaling desired object', 1, TRUE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Imitating toy action', 'Copying functional movement with a toy', 2, TRUE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Waving', 'Social gesture like saying goodbye or hello', 3, TRUE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Eye contact', 'Looking into someone’s eyes during interaction', 3, TRUE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Responding to name', 'Reacting when name is called', 5, TRUE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Following simple instruction', 'Complying with one-step direction like ''give me''', 5, TRUE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Nodding yes/no', 'Using head gestures to communicate choice', 1, TRUE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Clapping', 'Spontaneous or imitated hand clapping', 2, TRUE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Pointing to object', 'Indicating desired object without words', 1, TRUE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Mimicking facial expression', 'Copying a smile, frown or other face cue', 3, TRUE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Showing an object', 'Presenting something to share attention', 3, TRUE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Reaching out to interact', 'Extending arm to initiate social or object contact', 3, TRUE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Solving puzzle', 'Logical reasoning activity', 6, FALSE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Sorting objects', 'Grouping by shape, color, or size', 6, FALSE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Eating with spoon', 'Feeding independently', 7, FALSE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Covering ears', 'Response to loud sounds or stimuli', 8, FALSE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Body rocking', 'Self-regulating or repetitive movement', 8, FALSE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Self-injury', 'Hitting oneself or similar behaviors', 9, FALSE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Lining up toys', 'Arranging objects in straight lines', 8, FALSE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Spinning objects', 'Fixating or rotating items repetitively', 8, FALSE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Tapping surfaces', 'Repetitive sound-based self-stimulation', 8, FALSE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Sniffing objects', 'Bringing items close to nose frequently', 8, FALSE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Watching hands', 'Staring at hands or moving them in front of eyes', 8, FALSE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Unusual posture', 'Holding body in atypical stances', 8, FALSE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Jumping repeatedly', 'Non-functional repetitive jumping', 8, FALSE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Chewing non-food items', 'Mouthing or biting non-edibles', 8, FALSE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Screaming', 'Sudden loud vocal outbursts', 9, FALSE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Laughing inappropriately', 'Laughing without clear social context', 9, FALSE);
INSERT INTO behavior_type (name, description, category_id, is_milestone) VALUES ('Avoiding eye contact', 'Consistently looks away during interaction', 3, FALSE);

CREATE TABLE behavior_entry (
  id SERIAL PRIMARY KEY,
  child_id INT REFERENCES child(id),
  observer_id INT REFERENCES observer(id),
  behavior_type_id INT REFERENCES behavior_type(id),
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
