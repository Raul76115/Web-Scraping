USE uefa_cl19;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS fixtures;
DROP TABLE IF EXISTS lineups;
DROP TABLE IF EXISTS stats;

CREATE TABLE teams(
    id INT NOT NULL ,
    group_id VARCHAR(25) NOT NULL,
    team VARCHAR(75) NOT NULL,
    abbrv VARCHAR(5) NOT NULL,
    position VARCHAR(75) NOT NULL,
    player_name VARCHAR(150) NOT NULL
);

LOAD DATA INFILE 'E:/VirtualBox VMs/Docker/home/projects/data.csv'
INTO TABLE teams
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

CREATE TABLE fixtures(
    round_id INT,
    match_id INT NOT NULL,
    location VARCHAR(150),
    home_team VARCHAR(75),
    away_team VARCHAR(75),
    home_goals CHAR(4),
    away_goal CHAR(4)
);

LOAD DATA INFILE 'E:/VirtualBox VMs/Docker/home/projects/fixtures.csv'
INTO TABLE fixtures
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

CREATE TABLE lineups(
    round_id INT,
    match_id INT NOT NULL,
    player_name VARCHAR(150),
    event VARCHAR(200),
    clock CHAR(10)
);

LOAD DATA INFILE 'E:/VirtualBox VMs/Docker/home/projects/lineups_f.csv'
INTO TABLE lineups
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

CREATE TABLE stats(
    round_id INT,
    match_id INT,
    team VARCHAR(75),
    event VARCHAR(50),
    mark0 CHAR(5),
    mark1 CHAR(5) 
);

LOAD DATA INFILE 'E:/VirtualBox VMs/Docker/home/projects/stats_f.csv'
INTO TABLE stats
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;