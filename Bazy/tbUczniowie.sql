CREATE TABLE tbOddzialy (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    oznaczenia TEXT,
    rok_naboru TEXT,
    rok_matury TEXT
);

CREATE TABLE tbUczniowie (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    imie TEXT,
    nazwisko TEXT,
    plec INTEGER,
    data_ur DATE,
    awatar BLOB,
    egzamin INTEGER,
    srednia_ocen DECIMAL,
    uwagi TEXT,
    
    klasa_id INTEGER,
    FOREIGN KEY (klasa_id) REFERENCES tbOddzialy (id)
);
