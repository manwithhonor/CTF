touch ./files/rw/db.sqlite3
chmod 666 ./files/rw/db.sqlite3
echo "CREATE TABLE users (login varchar(32), password varchar(32))" | sqlite3 ./files/rw/db.sqlite3
echo "CREATE TABLE posts (author INTEGER, title varchar(40), preview TEXT, full TEXT)" | sqlite3 ./files/rw/db.sqlite3
echo "INSERT INTO users (login, password) VALUES ('admin', '$(echo -n vWYG4ui23f1TuwerAadmin | md5sum | awk '{print $1}')')" | sqlite3 ./files/rw/db.sqlite3
echo "INSERT INTO posts (author, title, preview, full) VALUES (1, 'First post', 'My first post', 'My first post. So.... flag is: AAAAAAAAAAAAAAAAAAAAAAA=')" | sqlite3 ./files/rw/db.sqlite3
