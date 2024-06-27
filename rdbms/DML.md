## Data Manipulation Language

Command     | 	Description                          |	Syntax
------------|---------------------------------------|----------
INSERT	| Insert data into a table	             |INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
UPDATE	| Update existing data within a table	  |UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
DELETE	| Delete records from a database table	 |DELETE FROM table_name WHERE condition;
LOCK	| Table control concurrency	            |LOCK TABLE table_name IN lock_mode;
CALL	| Call a PL/SQL or JAVA subprogram	     |CALL procedure_name(arguments);
EXPLAIN PLAN	|Describe the access path to data	|EXPLAIN PLAN FOR SELECT * FROM table_name;
