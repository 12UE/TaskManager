create table virus_md5(
    name varchar(50),
    md5 varchar(50) not null);
    
    
CREATE TABLE `virus_md5` (
  `name` varchar(50) DEFAULT NULL,
  `md5` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8

insert into virus_md5 values
    ("test_virus",
    "d41d8cd98f00b204e9800998ecf8427e");