-- Running downgrade 4e5ac4536b32 -> 574014e8f55c

ALTER TABLE pessoa2 DROP COLUMN idade;

CREATE TABLE pessoa2_temp (
    id INTEGER NOT NULL, 
    nome VARCHAR(50) NOT NULL, 
    senha INTEGER NOT NULL, 
    idade INTEGER, 
    PRIMARY KEY (id)
);

UPDATE alembic_version SET version_num='574014e8f55c' WHERE alembic_version.version_num = '4e5ac4536b32';

-- Running downgrade 574014e8f55c -> a7fb5896f14a

DROP TABLE pessoa2;

UPDATE alembic_version SET version_num='a7fb5896f14a' WHERE alembic_version.version_num = '574014e8f55c';

