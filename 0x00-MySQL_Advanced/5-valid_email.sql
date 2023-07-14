-- Create trigger to reset valid_email attribute when email is changed
-- Description: This script creates a trigger that resets the 
-- `valid_email` attribute only when the email has been changed.
-- Database: Any
CREATE TRIGGER reset_valid_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email <> OLD.email THEN
    SET NEW.valid_email = 0;
  END IF;
END;
