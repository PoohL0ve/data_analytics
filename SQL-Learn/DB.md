# Understanding Databases and Systems
A databases is a collection of organised data stored on a computer for easy search and retrieval operations. A database management system is a type of software that allows users to interact with the data. There are numerous types of DBMS but the two most popular types are Relational DBMS and NoSQL DBMS.

In order to ensure that data integrity and security is maintained, database systems use constraints and rules. Data management is field that focuses on the creation, storage, and retrieval of data.

Components of a Database system
- **HArdware**: the physical structures that the system runs on like the RAM and CPU.
- **Software**: programs that organise the database and allows user interaction such as DBMS and operating system software.
- **People**: Systems Administrators (manages the entire system), Database designers, Database Administrators, Systems Analyst and Programmers.
- **Procedures**: Rules on how the database is designed and how it is used.
- **Data**: raw facts used to build information.



## Relational Database Model
Columns are the properties and the rows are the entities.
The schema describes the structure and the datatypes that each column can take.

## Design
### Normalisation
Database normalisation is the process of organizing data into tables to reduce redundancy and improve data integrity. It involves breaking down
a large database into smaller, related tables and defining relationships between them using primary and foreign keys. As the data is spread across different databases, using the **JOIN** clause in SQL can combine tables to retrieve relevant data.

Database transactions represents a unit of work performed within a DBMS against a databse, which is any change such as when retrieving or inserting data. There four properties of a transaction referred to as ACID properties:
- **Atomicity**: if one transaction fails, all should fail.
- **Consistency**: any transaction should take the DB from one state to another.
- **Isolation**: transactions should be isolated, that it, one should not affect the other.
- **Durability**: data modification that occurs within a successful transaction should be permantly kept.

The cycle should be:
- Active -> failed -> aborted -> exist or
- Active -> partially commited -> committed -> exit.