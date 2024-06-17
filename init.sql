CREATE TABLE IF NOT EXISTS user(
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        id INTEGER NOT NULL,
        created_at DATETIME,
        updated_at DATETIME,
        PRIMARY KEY (id)
);
INSERT INTO user VALUES('myc','123456',1,'2024-06-17 14:20:57','2024-06-17 14:20:57');
INSERT INTO user VALUES('tom','654321',2,'2024-06-17 14:20:57','2024-06-17 14:20:57');
INSERT INTO user VALUES('joy','1qaz2wsx',3,'2024-06-17 14:20:57','2024-06-17 14:20:57');