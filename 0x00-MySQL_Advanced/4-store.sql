-- Create trigger to decrease item 
-- quantity after adding a new order
-- Description: This script creates a trigger 
-- that automatically decreases the quantity 
-- of an item after adding a new order.
-- Database: MySQL

CREATE TRIGGER decrease_quantity AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE item_id = NEW.item_id;
