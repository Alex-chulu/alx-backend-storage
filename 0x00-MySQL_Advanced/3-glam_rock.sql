-- List bands with Glam rock as main style ranked by longevity
-- Description: This script lists bands with Glam rock
-- as their main style, ranked by their longevity.
-- Database: Any

SELECT band_name, 
    YEAR(2022) - SUBSTRING_INDEX(lifespan, '-', 1) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
