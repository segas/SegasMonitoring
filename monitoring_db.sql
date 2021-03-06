DROP DATABASE IF EXISTS monitoring;
CREATE DATABASE monitoring;

CREATE TABLE sites(
	id_site		INT UNSIGNED NOT NULL AUTO_INCREMENT,
	name		VARCHAR(20) NOT NULL,
	description	VARCHAR(100) NOT NULL,
	site		VARCHAR(50) NOT NULL,
	created		TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	last_edited	TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	enabled		TINYINT(1) UNSIGNED NOT NULL,
	PRIMARY KEY (id_site)
);

CREATE TABLE monlog(
	id_monlog	INT UNSIGNED NOT NULL AUTO_INCREMENT,
	fk_site		INT UNSIGNED NOT NULL,
	state		VARCHAR(4) NOT NULL,
	date		TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id_monlog),
	FOREIGN KEY (fk_site) REFERENCES sites(id_site)
);
