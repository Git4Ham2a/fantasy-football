CREATE TABLE IF NOT EXISTS teams (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(30) 
);
CREATE TABLE IF NOT EXISTS players (
        id INT PRIMARY KEY AUTO_INCREMENT, 
        name VARCHAR(30),
        position VARCHAR(30),
        fk_teamid INT, 
        FOREIGN KEY (fk_teamid) REFERENCES teams(id)
);
