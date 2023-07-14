-- Create stored procedure ComputeAverageScoreForUser
-- Description: This script creates a stored procedure named 
-- ComputeAverageScoreForUser that computes and stores the 
-- average score for a student.
-- Database: Any

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (
  IN user_id INT
)
BEGIN
  DECLARE average_score DECIMAL(10,2);
  
  -- Compute average score
  SELECT AVG(score) INTO average_score
  FROM corrections
  WHERE user_id = user_id;
  
  -- Update user's average score
  UPDATE users
  SET average_score = average_score
  WHERE id = user_id;
  
END //

DELIMITER ;
