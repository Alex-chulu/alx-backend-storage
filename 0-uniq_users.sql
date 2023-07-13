-- Create users table
-- Description: This script creates a table 
-- called "users" with the specified attributes.
-- Database: MySQL 5.7

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255)
);
