-- Create view need_meeting
-- Description: This script creates a view named need_meeting 
-- that lists all students with a score under 80 (strict) and either no l
-- ast_meeting date or a date that is more than one month ago.
-- Database: Any

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
  AND (last_meeting IS NULL OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH));
