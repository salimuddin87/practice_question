## Data Control Language 

Command     |	Description     |	Syntax
------------|-------------------|--------
GRANT	|Assigns new privileges to a user account, allowing access to specific database objects, actions, or functions.	|GRANT privilege_type [(column_list)] ON [object_type] object_name TO user [WITH GRANT OPTION];
REVOKE	|Removes previously granted privileges from a user account, taking away their access to certain database objects or actions.	|REVOKE [GRANT OPTION FOR] privilege_type [(column_list)] ON [object_type] object_name FROM user [CASCADE];
