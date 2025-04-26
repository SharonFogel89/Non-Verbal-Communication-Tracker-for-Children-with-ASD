def add_child(name, date_of_birth, diagnosis_date=None, notes=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO child (name, date_of_birth, date_of_diagnosis, notes)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
    """, (name, date_of_birth, diagnosis_date, notes))
    child_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def get_child_by_id(child_id):
    get_child_by_id(child_id, notes=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
            INSERT INTO child_id (child_id, notes=None)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """, (child_id, notes=None))
    get_child_by_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def list_all_children(name, date_of_birth, diagnosis_date):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
            INSERT INTO child (name, date_of_birth, diagnosis_date)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """, (name, date_of_birth, diagnosis_date))
    list_all_children = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def add_observer(name, relation, notes=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO observer (name, relation, notes=None)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
    """, (name, relation, notes=None))
    add_observer = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def get_observer_by_id(observer_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
            INSERT INTO get_observer_by_id (observer_id)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """, (observer_id))
    get_observer_by_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def list_all_observers(name, relation, notes=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO observer (name, relation, notes=None)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
    """, (name, relation, notes=None))
    list_all_observers = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def list_all_categories(id, name, description):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
            INSERT INTO categories(id, name, description)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """, (id, name, description))
    list_all_categories = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def categories(id, name, description):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO categories(id, name, description)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
    """, (id, name, description))
    categories_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def behavior_types(id, name, is_milestone, description, category_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO behavior_types(id, name, description)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
    """, (id, name, description))
    behavior_types = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def list_milestone_behavior_types(id, name, is_milestone, description, category_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO list_milestone_behavior_types(id, name, is_milestone, description, category_id)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
    """, (id, name, is_milestone, description, category_id))
    list_milestone_behavior_types = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def add_behavior_entry(child_id, observer_id, behavior_type_id, category_id, behavior_date, duration_sec=None, consolidated=False, base=False, notes=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
            INSERT INTO add_behavior_entry(child_id, observer_id, behavior_type_id, category_id, behavior_date, duration_sec=None, consolidated=False, base=False, notes=None)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """, (child_id, observer_id, behavior_type_id, category_id, behavior_date, duration_sec=None, consolidated=False, base=False, notes=None))
    add_behavior_entry = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def list_behaviors_by_child(child_id):
    list_behaviors_by_child(child_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
                INSERT INTO list_behaviors_by_child (child_id)
                VALUES (%s, %s, %s, %s)
                RETURNING id;
            """, (child_id))
    list_behaviors_by_child = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def filter_behaviors(child_id=None, category_id=None, observer_id=None, is_consolidated=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
                    INSERT INTO filter_behaviors (child_id=None, category_id=None, observer_id=None, is_consolidated=None)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id;
                """, (child_id=None, category_id=None, observer_id=None, is_consolidated=None))
    filter_behaviors = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def get_behavior_summary_by_category(child_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
                    INSERT INTO get_behavior_summary_by_category(child_id)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id;
                """, (child_id))
    get_behavior_summary_by_category = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def get_behavior_timeline(child_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
                    INSERT INTO get_behavior_timeline(child_id)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id;
                """, (child_id))
    get_behavior_timeline = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def create_alert(child_id, alert_date, description):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
                    INSERT INTO create_alert(child_id, alert_date, description)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id;
                """, (child_id, alert_date, description))
    create_alert = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def resolve_alert(alert_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
                    INSERT INTO resolve_alert(alert_id)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id;
                """, (alert_id))
    resolve_alert = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def list_open_alerts(child_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
                    INSERT INTO list_open_alerts(child_id)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id;
                """, (child_id))
    list_open_alerts = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def add_translation(entity_type, language_code, original_text, translated_text):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
                    INSERT INTO add_translation(entity_type, language_code, original_text, translated_text)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id;
                """, (add_translation(entity_type, language_code, original_text, translated_text))
    add_translation = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def get_translation(entity_type, entity_id, language_code):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
                    INSERT INTO get_translation(entity_type, entity_id, language_code)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id;
                """, (entity_type, entity_id, language_code))
    get_translation = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def export_child_data_to_csv(child_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
                    INSERT INTO export_child_data_to_csv(child_id)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id;
                """, (child_id))
    export_child_data_to_csv = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

def export_all_behaviors_to_csv(filename):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
                    INSERT INTO export_all_behaviors_to_csv(filename)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id;
                """, (filename))
    export_all_behaviors_to_csv = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()