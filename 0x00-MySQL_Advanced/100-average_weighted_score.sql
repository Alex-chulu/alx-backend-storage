-- Task: Create a stored procedure ComputeAverageWeightedScoreForUser
-- All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
-- All your files should end with a new line
-- All your SQL queries should have a comment just before (i.e. syntax above)
-- All your files should start by a comment describing the task
-- A README.md file, at the root of the folder of the project, is mandatory
-- The length of your files will be tested using wc

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
    -- Calculate the total weighted score and total weight of projects for the specified user
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    
    -- Initialize variables
    SET total_score = 0;
    SET total_weight = 0;
    
    -- Calculate the weighted average score for the specified user
    SELECT SUM(c.score * p.weight) INTO total_score, SUM(p.weight) INTO total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;
    
    -- Update the user's average_score
    IF total_weight > 0 THEN
        SET total_score = total_score / total_weight;
        UPDATE users
        SET average_score = total_score
        WHERE id = user_id;
    ELSE
        -- If total_weight is 0, set average_score to 0
        UPDATE users
        SET average_score = 0
        WHERE id = user_id;
    END IF;
END$$

DELIMITER ;

