-- Create stored procedure ComputeAverageWeightedScoreForUser
-- Description: This script creates a stored procedure named 
-- ComputeAverageWeightedScoreForUser that computes and stores 
-- the average weighted score for a student.
-- Database: Any

DELIMITER //

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (
  IN user_id INT
)
BEGIN
  DECLARE average_weighted_score INT DEFAULT 0;
  
  -- Compute average weighted score
  SELECT SUM(score * weight) / SUM(weight) INTO average_weighted_score
  FROM corrections
  WHERE user_id = user_id;
  
  -- Update user's average weighted score
  UPDATE users
  SET average_weighted_score = average_weighted_score
  WHERE id = user_id;
  
END //

DELIMITER ;
