-- Task: Create a stored procedure ComputeAverageWeightedScoreForUsers
-- All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
-- All your files should end with a new line
-- All your SQL queries should have a comment just before (i.e. syntax above)
-- All your files should start by a comment describing the task
-- A README.md file, at the root of the folder of the project, is mandatory
-- The length of your files will be tested using wc

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Calculate the average weighted score for all students
    
    -- Declare variables
    DECLARE user_count INT;
    
    -- Get the count of users
    SELECT COUNT(*) INTO user_count FROM users;
    
    -- Iterate through each user and calculate their average weighted score
    DECLARE i INT DEFAULT 1;
    WHILE i <= user_count DO
        DECLARE user_id INT;
        DECLARE total_score FLOAT;
        DECLARE total_weight INT;
        
        -- Get user_id
        SELECT id INTO user_id FROM users LIMIT 1 OFFSET (i - 1);
        
        -- Initialize variables
        SET total_score = 0;
        SET total_weight = 0;
        
        -- Calculate the weighted average score for the user
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
        
        SET i = i + 1;
    END WHILE;
END$$

DELIMITER ;

