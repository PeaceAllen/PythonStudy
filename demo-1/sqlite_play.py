import sqlite3


def test_1():
    conn = sqlite3.connect("test.db")

    cursor = conn.cursor()

    # cursor.execute('create table t_user(id int primary key, username text)')
    # conn.commit()

    cursor.execute('''insert into t_user(id, username) values(?,?)''', (8, "zhangsan2"))
    conn.commit()

    cursor.execute("select * from t_user")
    users = cursor.fetchall()
    print(f'users count = {len(users)}')

    for u in users:
        print(f'user = {u}')

    cursor.close()

    pass


def test_2():
    conn = sqlite3.connect("podcast.db")
    cursor = conn.cursor()

    cursor.execute('''select * from Episode where id = "dir469327837"''')
    episodes = cursor.fetchall()

    print(f'episode count = {len(episodes)}')

    for episode in episodes:
        print(f'episode title = {episode}')

    cursor.close()
    pass


def test_3():
    conn = sqlite3.connect("podcast.db")
    cursor = conn.cursor()

    cursor.execute('''select * from Podcast''')
    podcasts = cursor.fetchall()

    print(f'podcasts count = {len(podcasts)}')

    for p in podcasts:
        print(p)

    cursor.close()
    pass


test_3()
