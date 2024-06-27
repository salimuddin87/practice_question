## Data Definition Language

Command | Description                                                                                   |   Syntax
------- |-----------------------------------------------------------------------------------------------|---------
CREATE  | Create database or its objects (table, index, function, views, store procedure, and triggers) | CREATE TABLE table_name (column1 data_type, column2 data_type, ...);
DROP    | Delete objects(table schema and all records) from the database                                |	DROP TABLE table_name;
ALTER   | Alter the structure of the database                                                           |	ALTER TABLE table_name ADD COLUMN column_name data_type;
TRUNCATE | Remove all records from a table, but it will not delete schema of table                       |	TRUNCATE TABLE table_name;
COMMENT	| Add comments to the data dictionary	                                                          |COMMENT 'comment_text' ON TABLE table_name;
RENAME	| Rename an object existing in the database	                                                    |RENAME TABLE old_table_name TO new_table_name;
