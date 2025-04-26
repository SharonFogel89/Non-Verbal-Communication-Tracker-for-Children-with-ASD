from core.db_connection import get_connection
from core.models import Child, Observer, BehaviorEntry, BehaviorType, Category

def add_child(child: Child):
    """
    Inserts a new child into the database using a Child object.
    Returns the new child ID.
    """
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO child (name, date_of_birth, date_of_diagnosis, notes)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
    """, (
        child.name,
        child.date_of_birth,
        child.date_of_diagnosis,
        child.notes
    ))

    child.id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return child.id

def list_all_children():
    """
    Lists all the children in the database.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, date_of_birth, date_of_diagnosis, notes FROM child;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [Child(*row) for row in rows]

def list_all_observer():
    """
    Lists all the observer in the database.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM observer;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [Observer(*row) for row in rows]

def add_observer(observer: Observer):
    """
    Inserts a new observer into the database using a Observer object.
    Returns the new observer ID.
    """
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO observer (name, relation, notes)
        VALUES (%s, %s, %s)
        RETURNING id;
    """, (
        observer.name,
        observer.relation,
        observer.notes
    ))

    observer.id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return observer.id


def list_all_behavior_type():
    """
    Lists all the behavior_type in the database.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM behavior_type;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [BehaviorType(*row) for row in rows]

def add_behavior_entry(entry: BehaviorEntry):
    """
    Inserts a new Behavior Entry into the database using a BehaviorEntry object.
    Returns the new BehaviorEntry ID.
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO behavior_entry (
            child_id,
            observer_id,
            behavior_type_id,
            behavior_date,
            notes,
            duration_sec,
            consolidated,
            base
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
    """, (
        entry.child_id,
        entry.observer_id,
        entry.behavior_type_id,
        entry.behavior_date,
        entry.notes,
        entry.duration_sec,
        entry.consolidated,
        entry.base
    ))

    entry.id = cur.fetchone()[0]  # Save the new ID into the object
    conn.commit()
    cur.close()
    conn.close()

    return entry.id


def list_behaviors_by_child(child_id):
    """
    Lists all behavior entries for a specific child, including behavior type name.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            behavior_entry.id,
            behavior_entry.child_id,
            behavior_entry.observer_id,
            behavior_entry.behavior_type_id,
            behavior_entry.behavior_date,
            behavior_entry.notes,
            behavior_entry.duration_sec,
            behavior_entry.consolidated,
            behavior_entry.base,
            behavior_type.name AS behavior_name
        FROM behavior_entry
        JOIN behavior_type ON behavior_entry.behavior_type_id = behavior_type.id
        WHERE behavior_entry.child_id = %s
        ORDER BY behavior_entry.behavior_date ASC;
    """, (child_id,))
    
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows 


def filter_behaviors(child_id=None, category_id=None, observer_id=None, is_consolidated=None):
    """
    Filters behavior entries based on optional parameters.
    """
    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT behavior_entry.*, behavior_type.name, category.name
        FROM behavior_entry
        JOIN behavior_type ON behavior_entry.behavior_type_id = behavior_type.id
        JOIN category ON behavior_type.category_id = category.id
        WHERE 1=1
    """
    params = []

    if child_id:
        query += " AND behavior_entry.child_id = %s"
        params.append(child_id)

    if category_id:
        query += " AND behavior_type.category_id = %s"
        params.append(category_id)

    if observer_id:
        query += " AND behavior_entry.observer_id = %s"
        params.append(observer_id)

    if is_consolidated is not None:
        query += " AND behavior_entry.consolidated = %s"
        params.append(is_consolidated)

    query += " ORDER BY behavior_entry.behavior_date ASC"

    cur.execute(query, tuple(params))
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows


def list_all_categories():
    """
    Lists all the categories  in the database.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM category;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [Category(*row) for row in rows]


def get_behavior_summary_by_category(child_id):
    """
    Returns the count of behaviors per category for a specific child.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            category.name AS category_name,
            COUNT(*) AS behavior_count
        FROM behavior_entry
        JOIN behavior_type ON behavior_entry.behavior_type_id = behavior_type.id
        JOIN category ON behavior_type.category_id = category.id
        WHERE behavior_entry.child_id = %s
        GROUP BY category.name
        ORDER BY behavior_count DESC;
    """, (child_id,))
    
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows


def get_child_by_id(child_id):
    """
    Retrieves a specific child by their ID.
    Returns a Child object or None if not found.
    """
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT id, name, date_of_birth, date_of_diagnosis, notes
        FROM child
        WHERE id = %s;
    """, (child_id,))
    
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        return Child(*row)
    else:
        return None


def get_observer_by_id(observer_id):
    """
    Retrieves a specific observer by their ID.
    Returns an Observer object or None if not found.
    """
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT id, name, relation, notes
        FROM observer
        WHERE id = %s;
    """, (observer_id,))
    
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        return Observer(*row)
    else:
        return None
    


def list_milestone_behavior_types():
    """
    Lists all behavior types marked as milestone (is_milestone = TRUE).
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, name, description, category_id, is_milestone
        FROM behavior_type
        WHERE is_milestone = TRUE;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [BehaviorType(*row) for row in rows]


def get_behavior_timeline_monthly(child_id):
    """
    Returns the number of behaviors registered per month for a specific child.
    """
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT 
            DATE_TRUNC('month', behavior_date) AS month,
            COUNT(*) AS behavior_count
        FROM behavior_entry
        WHERE child_id = %s
        GROUP BY month
        ORDER BY month ASC;
    """, (child_id,))
    
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows  

def get_behavior_timeline_weekly(child_id):
    """
    Returns the number of behaviors registered per week for a specific child.
    """
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT 
            DATE_TRUNC('week', behavior_date) AS week,
            COUNT(*) AS behavior_count
        FROM behavior_entry
        WHERE child_id = %s
        GROUP BY week
        ORDER BY week ASC;
    """, (child_id,))
    
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows  