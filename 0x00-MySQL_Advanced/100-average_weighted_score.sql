-- Create stored procedure ComputeAverageWeightedScoreForUser
-- Description: This script creates a stored procedure named 
-- ComputeAverageWeightedScoreForUser that computes and stores 
-- the average weighted score for a student.
-- Database: Any

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
  DECLARE average_weighted_score INT DEFAULT 0;
  DECLARE t_weight INT DEFAULT 0;

  SELECT SUM(corrections.score * projects.weight) INTO t_weighted_score
  FROM corrections 
  INNER JOIN projects ON corrections.project_id = projects.id
  WHERE corrections.user_id = user_id;

  SELECT SUM(projects.weight) INTO tot_weight FROM corrections
  INNER JOIN projects ON corrections.project_id = projects.id
  WHERE corrections.user_id = user_id;

  IF t_weight = 0 THEN
    UPDATE users
    SET users.average_score = 0
    WHERE users.id = user_id;
  ELSE
    UPDATE users
    SET users.average_score = tot_weighted_score / tot_weight
    WHERE users.id = user_id;
    END IF;
  
END //

DELIMITER ;
