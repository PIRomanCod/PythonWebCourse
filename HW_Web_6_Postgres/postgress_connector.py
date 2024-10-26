from psycopg2 import connect, DatabaseError
from contextlib import contextmanager


@contextmanager
def postgres_connection():
    conn = None
    try:
        conn = connect(host='localhost', user='postgres', database='postgres', password='piromankod')
        yield conn
        conn.commit()
    except DatabaseError as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()


def execute_query(conn, sql: str) -> list:
    try:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()

    except DatabaseError as error:
        print(error)


if __name__ == '__main__':
    pass
