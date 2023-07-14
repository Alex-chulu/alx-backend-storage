-- Create stored procedure ComputeAverageScoreForUser
-- Description: This script creates a stored procedure named 
-- ComputeAverageScoreForUser that computes and stores the 
-- average score for a student.
-- Database: Any

DELIMITER //

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	UPDATE users
	SET
	average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
	WHERE id = user_id;
  
END //

DELIMITER ;
