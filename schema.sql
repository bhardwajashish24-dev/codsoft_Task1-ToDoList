CREATE TABLE Task(
    Id bigint primary key,
    TaskNo int,
    TaskDetail varchar(100),
    Date date,
    IsComplete bool
);