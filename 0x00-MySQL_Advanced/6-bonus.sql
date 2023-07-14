-- Create stored procedure AddBonus
-- Description: This script creates a stored procedure 
-- named AddBonus that adds a new correction for a student.
-- Database: Any

DELIMITER //

CREATE PROCEDURE AddBonus (
  IN user_id INT,
  IN project_name VARCHAR(255),
  IN score INT
)
BEGIN
  DECLARE project_id INT;

  -- Check if project exists, else create it
  SELECT id INTO project_id FROM projects WHERE name = project_name;
  
  IF project_id IS NULL THEN
    -- Create new project if it doesn't exist
    INSERT INTO projects (name) VALUES (project_name);
    SET project_id = LAST_INSERT_ID();
  END IF;

  -- Add new correction
  INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
  
END //

DELIMITER ;
