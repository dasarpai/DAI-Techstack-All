import db


def test_create_schema(database):
    db.create_schema(database)
    cur = database.cursor()
    cur.execute('SELECT * FROM logs')  # Make sure the table is there
    db.create_schema(database)  # See we can do it 2nd time without error
