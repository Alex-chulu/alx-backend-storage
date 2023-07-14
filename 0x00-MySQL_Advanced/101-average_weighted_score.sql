-- Create stored procedure ComputeAverageWeightedScoreForUsers
-- Description: This script creates a stored procedure named 
-- ComputeAverageWeightedScoreForUsers that computes and stores 
-- the average weighted score for all students.
-- Database: Any

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
  DECLARE user_id INT;
  DECLARE average_weighted_score DECIMAL(10,2);
  
  -- Declare cursor for selecting distinct user IDs
  DECLARE user_cursor CURSOR FOR SELECT DISTINCT id FROM users;
  
  -- Declare cursor handler
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET user_id = NULL;
  
  -- Open cursor
  OPEN user_cursor;
  
  -- Start fetching rows from cursor
  FETCH NEXT FROM user_cursor INTO user_id;
  
  -- Loop through each user
  WHILE user_id IS NOT NULL DO
    -- Compute average weighted score for current user
    SELECT SUM(score * weight) / SUM(weight) INTO average_weighted_score
    FROM corrections
    WHERE user_id = user_id;
  
    -- Update user's average weighted score
    UPDATE users
    SET average_weighted_score = average_weighted_score
    WHERE id = user_id;
    
    -- Fetch next user
    FETCH NEXT FROM user_cursor INTO user_id;
  END WHILE;
  
  -- Close cursor
  CLOSE user_cursor;
  
END //

DELIMITER ;
