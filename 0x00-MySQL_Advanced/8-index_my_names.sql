-- Create index idx_name_first on the first letter of name
-- Description: This script creates an index named idx_name_first 
-- on the table names for the first letter of the name column.
-- Database: Any

CREATE INDEX idx_name_first ON names (name(1));
