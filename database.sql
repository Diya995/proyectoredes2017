drop table if exists estados_maquina;

create table estados_maquina (
	id_so serial,
	kernel varchar(100),
	release varchar(100),
	nodename varchar(100),
	kernelv varchar(100),
	machine varchar(100),
	processor varchar(100),
	os varchar(100),
	hardware varchar(100),
	cpu_us varchar(100),
	cpu_sy varchar(100),
	cpu_id varchar(100),
	cpu_wa varchar(100),
	cpu_st varchar(100),
	mem_swpd varchar(100),
	mem_free varchar(100),
	mem_buff varchar(100),
	cache varchar(100),
	swap_si varchar(100),
	swap_so varchar(100),
	primary key (id_so)
);

drop table if exists estados_descargas;

create table estados_descargas (
	id_dt serial,
	magnet_link varchar(100),
	iniciada varchar(2),
	estado_descarga varchar(100) ,
	primary key (id_dt) 
);

INSERT INTO So VALUES 
(1,'linux','release','node','ibm','200mb','x64','ms-dos','old');

