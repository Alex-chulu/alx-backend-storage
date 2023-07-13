-- Rank country origins of bands by number 
-- of non-unique fans
-- Description: This script ranks the country 
-- origins of bands based on the number 
-- of non-unique fans.
-- Database: Any

SELECT origin, SUM(fans) AS total_fans
FROM metal_bands
GROUP BY origin ORDER BY total_fans DESC;
