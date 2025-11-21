from sqlalchemy import insert, select, update, delete
from database import engine
from tables import tasks_table

# Create a new task
def create_task(title: str, description: str | None = None):
    query = insert(tasks_table).values(title=title, description=description)
    with engine.connect() as conn:
        result = conn.execute(query)
        conn.commit()
        return result.inserted_primary_key[0]  # return new task id

# Get all tasks
def get_tasks():
    query = select(tasks_table)
    with engine.connect() as conn:
        result = conn.execute(query)
        return result.fetchall()  # returns list of Row objects

# Update a task by id
def update_task(pk: int, title: str | None = None, description: str | None = None):
    values = {}
    if title is not None:
        values['title'] = title
    if description is not None:
        values['description'] = description

    if not values:
        return 0  # nothing to update

    query = update(tasks_table).where(tasks_table.c.id == pk).values(**values)
    with engine.connect() as conn:
        result = conn.execute(query)
        conn.commit()
        return result.rowcount  # number of updated rows

# Delete a task by id
def delete_task(pk: int):
    query = delete(tasks_table).where(tasks_table.c.id == pk)
    with engine.connect() as conn:
        result = conn.execute(query)
        conn.commit()
        return result.rowcount  # number of deleted rows

# Toggle task status (completed/not completed)
def change_task_status(pk: int):
    # First, get current status
    query = select(tasks_table.c.completed).where(tasks_table.c.id == pk)
    with engine.connect() as conn:
        current = conn.execute(query).scalar()
        if current is None:
            return 0  # task not found
        new_status = not current
        update_query = update(tasks_table).where(tasks_table.c.id == pk).values(completed=new_status)
        conn.execute(update_query)
        conn.commit()
        return 1  # success
