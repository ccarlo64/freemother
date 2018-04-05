-- Schema per gli esempi dell'applicazione to-do.

create table cookies (
    id            integer primary key autoincrement not null,
    node          text,
    name          text
);
create table cookies_events (
    id            integer primary key autoincrement not null,
    node          text,
    date_events   text,
	feed_type     text,
	signal        text,
	val           text 
);