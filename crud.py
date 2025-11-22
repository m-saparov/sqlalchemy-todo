from sqlalchemy import insert, select, update, delete
from database import engine
from tables import tasks_table


def create_task(title: str, description: str | None = None):
    query = insert(tasks_table).values(title=title, description=description)
    with engine.connect() as conn:
        result = conn.execute(query)
        conn.commit()
        return result.inserted_primary_key[0]

def get_tasks():
    query = select(tasks_table)
    with engine.connect() as conn:
        result = conn.execute(query)
        return list(result)

def update_task(pk: int, title: str | None = None, description: str | None = None):
    values = {}
    if title is not None:
        values['title'] = title
    if description is not None:
        values['description'] = description

    if not values:
        return 0

    query = update(tasks_table).where(tasks_table.c.id == pk).values(**values)
    with engine.connect() as conn:
        result = conn.execute(query)
        conn.commit()
        return result.rowcount

 
def delete_task(pk: int):
    query = delete(tasks_table).where(tasks_table.c.id == pk)
    with engine.connect() as conn:
        result = conn.execute(query)
        conn.commit()
        return result.rowcount 

def change_task_status(pk: int):
    query = select(tasks_table.c.completed).where(tasks_table.c.id == pk)
    with engine.connect() as conn:
        current = conn.execute(query).scalar()
        if current is None:
            return 0
        new_status = not current
        update_query = update(tasks_table).where(tasks_table.c.id == pk).values(completed=new_status)
        conn.execute(update_query)
        conn.commit()
        return 1
