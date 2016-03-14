CREATE TABLE user
(
   id          int(10),
   fullname    varchar(80),
   email       varchar(80),
   username    varchar(80),
   password    varchar(80),
   is_author   tinyint(1) DEFAULT 0
)