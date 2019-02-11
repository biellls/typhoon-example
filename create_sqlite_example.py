import sqlite3


def populate_database():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    # c.execute("INSERT INTO person VALUES (12, 'John', 'Doe', 35, '2019-02-05')")
    # c.execute("INSERT INTO person VALUES (17, 'Jane', 'Doe', 32, '2019-02-05')")
    c.execute("INSERT INTO person VALUES (14, 'Clark', 'Kane', 47, '2019-02-05')")

    # c.execute("INSERT INTO job VALUES (3, 'Marketing Manager', 17, 90000, '2019-02-05')")
    # c.execute("INSERT INTO job VALUES (2, 'Consultant', 12, 75000, '2019-02-05')")
    # c.execute("INSERT INTO job VALUES (1, 'Clerk', 14, 22000, '2019-02-05')")

    # c.execute("INSERT INTO property VALUES (1, 'Bond Street 5', 17, 200, 470000, '2019-02-05')")
    # c.execute("INSERT INTO property VALUES (3, 'Old Street 7', 12, 250, 812000, '2019-02-05')")
    # c.execute("INSERT INTO property VALUES (2, 'Angel Dist 17 num 5', 14, 60, 180000, '2019-02-05')")

    conn.commit()
    conn.close()


# noinspection SqlNoDataSourceInspection
def create_database():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    # Create tables
    c.execute('CREATE TABLE person (id integer, name text, surname text, age integer, creation_date text)')
    c.execute('CREATE TABLE job (id integer, title text, personid integer, salary real, creation_date text)')
    c.execute('CREATE TABLE property (id integer, address text, personid integer, size integer, price real, creation_date text)')

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


if __name__ == '__main__':
    # create_database()
    populate_database()
