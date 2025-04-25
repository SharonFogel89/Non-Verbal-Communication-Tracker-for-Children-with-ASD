class child:
    def __init__(self, id, name, date_of_birth, date_of_diagnosis, notes):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.date_of_diagnosis = date_of_diagnosis
        self.notes = notes


class observer:
    def __init__(self, id, name, relation, notes):
        self.id = id
        self.name = name
        self.relation = relation
        self.notes = notes


class category:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


class behavior_type:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


class behavior_entry:
    def __init__(self, id, child_id, observer_id, behavior_type_id, category_id, behavior_date, notes, duration_sec, consolidated, base):
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


class alert:
    def __init__(self, id, child_id, alert_date, solved, description):
        self.id = id
        self.child_id = child_id
        self.alert_date = alert_date
        self.solved = solved
        self.description = description


class milestone:
    def __init__(self, id, child_id, milestone_date, milestone_type, description):
        self.id = id
        self.child_id = child_id
        self.milestone_date = milestone_date
        self.milestone_type = milestone_type
        self.description = description


class translation:
    def __init__(self, id, language_code, original_text, translated_text):
        self.id = id
        self.language_cod = language_cod
        self.original_text = original_text
        self.translated_text = translated_text