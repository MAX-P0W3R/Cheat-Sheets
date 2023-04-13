# Manual SQL injection cheat sheet from PortSwigger
This [SQL injection](https://portswigger.net/web-security/sql-injection) cheat sheet contains examples of useful syntax that you can use to perform a variety of tasks that often arise when performing SQL injection attacks.

## String concatenation
Oracle:  `'foo'||'bar'`    

Microsoft: `'foo'+'bar'` 

PostgreSQL: `'foo'||'bar'`

MySQL: `'foo' (space) 'bar'`

---

## Substring
Oracle:	`SUBSTR('foobar', 4, 2)`

Microsoft:	`SUBSTRING('foobar', 4, 2)`

PostgreSQL:	`SUBSTRING('foobar', 4, 2)`

MySQL:	`SUBSTRING('foobar', 4, 2)`

---

## Comments
Oracle:	`--comment`

Microsoft:	`--comment`
            `/*comment*/`
            
PostgreSQL:	`--comment`
            `/*comment*/`

MySQL:	`#comment`
`-- comment [Note the space after the double dash]`
`/*comment*/`

---

## Database contents

## Conditional errors

## Batched (or stacked) queries

## Time delays

## Conditional time delays

## DNS lookup

## DNS lookup with data exfiltration
