-- Create index idx_name_first_score on the 
-- first letter of name and score
-- Description: This script creates an index named 
-- idx_name_first_score on the table names for the first 
-- letter of both the name and score columns.
-- Database: Any

CREATE INDEX idx_name_first_score ON names(name(1), score);
