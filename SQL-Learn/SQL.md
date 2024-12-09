# SQL and Databases
A databases is a collection of organised data stored on a computer for easy search and retrieval operations. A database management system is a type of software that allows users to interact with the data. There are numerous types of DBMS but the two most popular types are Relational DBMS and NoSQL DBMS.

Topics discussed:
1. [**What is SQL?**](#a-little-on-sql)
2. [**RDBMS**](#relational-database-management-system)
3. [**Filtering Data**](#filtering-data-with-where)
4. [**Sort the Data**](#more-filtering-and-sorting)


## A Little on SQL
**Structured Query Language** (SQL) is the main programming language used to manipulate, transform, and query data that is stored in a relational database. It was created in 1970 to be similar to natural languages. SQL focuses on telling the system the *what* but not the *how*.

There are several basic data types that can be used in SQL:
- **Interger**: represents numbers from -2147483648 to +2147483648.
- **Decimal**: DECIMAL(precision, scale), where precision is the whole digit and scale is the number of units after the decimal point.
- **Float**: has an approximate part from 1-53
- **Boolean**: TRUE or FALSE
- **VARCHAR(n)**: String or text types that cannot be more than n characters long.

In SQL strings can be written in single or double quotes. Numbers can be explicitly defined with the *- or +* signs precedding them; however, the default (no symbol) would be positive. Values can also be **type-cast** using the **CAST()** operator:
```sql
CAST(value as DECIMAL());
CAST(4.5 as DECIMAL(2, 2));
```

## Filtering Data with WHERE
The **WHERE** clause is applied to each row to determine if the data of the row satisfies the conditions. A basic look at how it is used:
```sql
SELECT column, another_column
FROM mytable
WHERE condition
    AND/OR another condition;
```
Complex conditions can be created by using additional WHERE operators that are joined by the logical AND or OR operators:
|Operator     | Use Description               | Example        |
|:-----------:|:------------------------------|:--------------:|
|`=, !=, <, <=, >, >=`| Common numerical operations| `digit < 5`|
|`BETWEEN...AND`| Number is between specified values. BETWEEN is an inclusive operator as it can check strings, numbers, and dates|`col_name BETWEEN 4 AND 7`|
|`NOT BETWEEN AND`| Number is not in the range of values|`col_name NOT BETWEEN 8 AND 14`|
|`IN/NOT IN`| Number exists or does exists in a specified list| `price IN(9, 12,17)`|
|`LIKE/NOT LIKE` | used for pattern matching strings| `product LIKE %a%`|

When checking for string values always use single quotes. The *<>* can also be used for string inequality. **LIKE** uses special syntax for pattern matching:
- `%`: used anywhere in a string to match a sequence of zero or more characters - *product LIKE %s% can return cash, blissard
- `_`: used anywhere to match a single character - text LIKE s_ (so)


## More Filtering and Sorting
The **DISTINCT** clause can be used with different SQL statements to discard duplicated values.
```sql
SELECT DISTINCT column
From mytable;
```
The **ORDER BY** clause allows the data to be sorted in ascending or descending order by a specific column. That is, the values of all the tables are arranged based on the ordering of the specific column.
```sql
SELECT column1, column2 
FROM Soccer 
ORDER BY ASC/DESC;
```
The **LIMIT** clause is used to restrict the number rows and the **OFFSET** clause specifies where to start the limiting. They are generally placed last in a query.
```sql
SELECT column1, column2 
FROM Soccer 
ORDER BY ASC/DESC
LIMIT 6 OFFSET 13;
```