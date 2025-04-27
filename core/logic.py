import csv

from core.db_connection import get_connection
from core.models import Child, Observer, BehaviorEntry, BehaviorType, Category

from datetime import datetime, timedelta

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

def list_open_alerts(child_id):
    """
    Lists all open (unsolved) alerts for a child.
    """
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, child_id, alert_date, description, solved
        FROM alert
        WHERE child_id = %s AND solved = FALSE
        ORDER BY alert_date ASC;
    """, (child_id,))
    
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows

def resolve_alert(alert_id):
    """
    Marks an alert as solved.
    """
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE alert
        SET solved = TRUE
        WHERE id = %s;
    """, (alert_id,))

    conn.commit()
    cur.close()
    conn.close()


def check_and_create_alerts():
    """
    Checks if any child has not registered a behavior in the last 7 days and creates alerts if necessary.
    """
    conn = get_connection()
    cur = conn.cursor()

    # Busca todas as crianças
    cur.execute("SELECT id, name FROM child;")
    children = cur.fetchall()

    today = datetime.now().date()
    seven_days_ago = today - timedelta(days=7)

    for child_id, child_name in children:

        cur.execute("""
            SELECT MAX(behavior_date)
            FROM behavior_entry
            WHERE child_id = %s;
        """, (child_id,))
        last_behavior_date = cur.fetchone()[0]

        #print(f"{child_id} - {child_name}")
        #print("Last behavior:", last_behavior_date)

        if last_behavior_date is None or last_behavior_date.date() < seven_days_ago:
            cur.execute("""
                SELECT id
                FROM alert
                WHERE child_id = %s 
                  AND solved = FALSE 
                  AND alert_date >= %s;
            """, (child_id, seven_days_ago))
            existing_alert = cur.fetchone()

            if not existing_alert:
                description = f"No behaviors registered in the last 7 days for {child_name}."
                cur.execute("""
                    INSERT INTO alert (child_id, alert_date, description, solved)
                    VALUES (%s, %s, %s, FALSE);
                """, (child_id, today, description))
                print(f"Alert created for {child_name}.")
            else:
                #print(f"Existing open alert found for {child_name}. No new alert created.")
                pass
        else:
            #print(f"Recent behavior found for {child_name}. No alert needed.")
            pass
    conn.commit()


    print("\n=== Open Alerts ===")
    cur.execute("""
        SELECT alert.id, child.name, alert.alert_date, alert.description
        FROM alert
        JOIN child ON alert.child_id = child.id
        WHERE alert.solved = FALSE
        ORDER BY alert.alert_date ASC;
    """)
    open_alerts = cur.fetchall()

    if open_alerts:
        for alert_id, child_name, alert_date, description in open_alerts:
            print(f"- ID {alert_id} | {child_name} | {alert_date.strftime('%Y-%m-%d')} | {description}")
    else:
        print("No open alerts found.")


    cur.close()
    conn.close()

def export_child_data_to_csv(child_id, filename):
    """
    Exports all behavior entries for a specific child to a CSV file.
    """
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            behavior_entry.behavior_date,
            behavior_type.name AS behavior_name,
            category.name AS category_name,
            behavior_entry.notes,
            behavior_entry.duration_sec,
            behavior_entry.consolidated,
            behavior_entry.base
        FROM behavior_entry
        JOIN behavior_type ON behavior_entry.behavior_type_id = behavior_type.id
        JOIN category ON behavior_type.category_id = category.id
        WHERE behavior_entry.child_id = %s
        ORDER BY behavior_entry.behavior_date ASC;
    """, (child_id,))

    rows = cur.fetchall()
    cur.close()
    conn.close()

    if not rows:
        print("No behaviors found for this child.")
        return

    with open(filename, mode="w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Date", "Behavior", "Category", "Notes", "Duration (sec)", "Consolidated", "Pre-existing"])

        for row in rows:
            writer.writerow(row)

    print(f"Exported {len(rows)} behaviors to {filename}")


def export_all_behaviors_to_csv(filename):
    """
    Exports all behavior entries from all children to a CSV file.
    """
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            child.name AS child_name,
            behavior_entry.behavior_date,
            behavior_type.name AS behavior_name,
            category.name AS category_name,
            behavior_entry.notes,
            behavior_entry.duration_sec,
            behavior_entry.consolidated,
            behavior_entry.base
        FROM behavior_entry
        JOIN behavior_type ON behavior_entry.behavior_type_id = behavior_type.id
        JOIN category ON behavior_type.category_id = category.id
        JOIN child ON behavior_entry.child_id = child.id
        ORDER BY behavior_entry.behavior_date ASC;
    """)

    rows = cur.fetchall()
    cur.close()
    conn.close()

    if not rows:
        print("No behaviors found in the database.")
        return

    with open(filename, mode="w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Child", "Date", "Behavior", "Category", "Notes", "Duration (sec)", "Consolidated", "Pre-existing"])

        for row in rows:
            writer.writerow(row)

    print(f"Exported {len(rows)} behaviors to {filename}")