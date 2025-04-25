from core.db_connection import get_connection
from core.models import Child

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
