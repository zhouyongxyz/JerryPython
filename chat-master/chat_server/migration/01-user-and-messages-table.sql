CREATE DATABASE chat;
use chat;

drop table if exists user;
create table user(
	`id` int(11) not null AUTO_INCREMENT PRIMARY KEY,
    `login` varchar(255) NOT NULL,
    `nickname` varchar(255) NOT NULL,
    `password` varchar(255) NOT NULL,
    `status` int(1) DEFAULT 5,
    `create_at` DATETIME DEFAULT 0,
    `update_at` DATETIME DEFAULT 0
)ENGINE= InnoDB charset = utf8;

drop table if exists messages;
create table messages(
	`id` int(11) not null AUTO_INCREMENT PRIMARY KEY,
    `text` text ,
    `id_user` int(11) not null,
    `date` DATETIME	DEFAULT 0,
    `room_id` int(11) DEFAULT 1,
    `create_at` DATETIME DEFAULT 0,
    `status` int(1) DEFAULT 5
)ENGINE= InnoDB charset = utf8;