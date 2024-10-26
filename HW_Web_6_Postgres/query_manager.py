from time import sleep

from postgress_connector import postgres_connection, execute_query


def create_query(i):
    # читаємо файл зі скриптом для створення БД
    with open(f'query_{i}.sql', 'r') as f:
        sql = f.read()
    return sql


if __name__ == "__main__":
    for i in range(1, 13):
        print(f"Start query number {i}")
        sql = create_query(i)
        with postgres_connection() as conn:
            if conn is not None:
                res = execute_query(conn, sql)
                for n, item in enumerate(res, start=1):
                    print(n, item)
        print(f"Done query number  {i}", "\n", "\n")
        sleep(3)
    print("All tasks done!!!")