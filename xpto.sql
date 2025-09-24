CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> d76c2c15a56e

CREATE TABLE pessoa (
    id INTEGER NOT NULL, 
    nome VARCHAR(50) NOT NULL, 
    email VARCHAR(50) NOT NULL, 
    PRIMARY KEY (id)
);

INSERT INTO alembic_version (version_num) VALUES ('d76c2c15a56e') RETURNING version_num;

