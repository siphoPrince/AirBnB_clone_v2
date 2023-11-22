-- this file is to prepare for the project using mysql --

-- Create or use the specified database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create or modify the user hbnb_dev with the specified password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY "hbnb_dev_pwd";

-- Grant all privileges on the hbnb_dev_db to the user hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema to the user hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

