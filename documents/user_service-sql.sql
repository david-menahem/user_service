CREATE TABLE IF NOT EXISTS `users` (
	`id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`first_name` varchar(255) NOT NULL,
	`last_name` varchar(255) NOT NULL,
	`email` varchar(255) NOT NULL,
	`age` int(11) NOT NULL,
	`address` varchar(255) NOT NULL,
	`joining_date` varchar(255) NOT NULL,
	`is_registered` boolean NOT NULL DEFAULT False,
	`is_active` boolean NOT NULL DEFAULT True,
	PRIMARY KEY (`id`)
);