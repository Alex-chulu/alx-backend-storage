-- Create function SafeDiv
-- Description: This script creates a function named SafeDiv 
-- that divides two numbers and returns the result, or 
-- 0 if the second number is equal to 0.
-- Database: Any

DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10,2)
BEGIN
  DECLARE result DECIMAL(10,2);
  
  IF b = 0 THEN
    SET result = 0;
  ELSE
    SET result = a / b;
  END IF;
  
  RETURN result;
END //

DELIMITER ;
