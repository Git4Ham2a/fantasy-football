CREATE TABLE IF NOT EXISTS lists (
        lid INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(20) 
);
CREATE TABLE IF NOT EXISTS todos (
        tid INT PRIMARY KEY AUTO_INCREMENT, 
        tasks VARCHAR(30),
        complete BOOLEAN,
        fk_lid INT, 
        FOREIGN KEY (fk_lid) REFERENCES lists(lid)
);
