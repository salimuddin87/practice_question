## Transaction Control Language

Command     | 	Description                                        |	Syntax
------------|-----------------------------------------------------|-----------
BEGIN TRANSACTION	| Starts a new transaction	                           |BEGIN TRANSACTION [transaction_name];
COMMIT	| Saves all changes made during the transaction	      |COMMIT;
ROLLBACK	| Undoes all changes made during the transaction	     | ROLLBACK;                                           
SAVEPOINT	| Creates a savepoint within the current transaction	 |SAVEPOINT savepoint_name;
