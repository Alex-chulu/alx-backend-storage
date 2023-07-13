-- Create users table
-- Description: This script creates a table called "users" 
-- with the specified attributes including an enumeration for the "country" column.
-- Database: Any

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255),
  country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
