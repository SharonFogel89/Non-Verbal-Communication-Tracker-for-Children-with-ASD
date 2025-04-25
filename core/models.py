class Child:
    def __init__(self, id, name, date_of_birth, date_of_diagnosis, notes):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.date_of_diagnosis = date_of_diagnosis
        self.notes = notes

class Observer:
    def __init__(self, id, name, relation, notes):
        self.id = id
        self.name = name
        self.relation = relation
        self.notes = notes

class Category:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

class BehaviorType:
    def __init__(self, id, name, description, category_id, is_milestone):
        self.id = id
        self.name = name
        self.description = description
        self.category_id = category_id
        self.is_milestone = is_milestone

class BehaviorEntry:
    def __init__(self, id, child_id, observer_id, behavior_type_id, category_id,
                 behavior_date, notes, duration_sec, consolidated, base):
        self.id = id
        self.child_id = child_id
        self.observer_id = observer_id
        self.behavior_type_id = behavior_type_id
        self.category_id = category_id
        self.behavior_date = behavior_date
        self.notes = notes
        self.duration_sec = duration_sec
        self.consolidated = consolidated
        self.base = base

class Alert:
    def __init__(self, id, child_id, alert_date, solved, description):
        self.id = id
        self.child_id = child_id
        self.alert_date = alert_date
        self.solved = solved
        self.description = description

class Milestone:
    def __init__(self, id, child_id, milestone_date, milestone_type, description):
        self.id = id
        self.child_id = child_id
        self.milestone_date = milestone_date
        self.milestone_type = milestone_type
        self.description = description

class Translation:
    def __init__(self, id, language_code, original_text, translated_text):
        self.id = id
        self.language_code = language_code
        self.original_text = original_text
        self.translated_text = translated_text
