create database bd_medidor;
drop database bd_medidor;
use bd_medidor;

create table tb_registro(
	id INT AUTO_INCREMENT,
    temperatura DECIMAL(10,2),
    pressao DECIMAL(10,2),
    altitude DECIMAL(10,2),
    umidade DECIMAL(10,2),
    co2 DECIMAL(10,2),
    poeira DECIMAL(10,2),
    tempo_registro TIMESTAMP,
    
    PRIMARY KEY tb_registro(id)
);

create table tb_usuario(
	id INT NOT NULL AUTO_INCREMENT,
    nome CHAR(255) NOT NULL,
    email CHAR(255) NOT NULL,
    
    PRIMARY KEY tb_usuario(id)
);

create table tb_canal(
	id INT NOT NULL AUTO_INCREMENT,
    nome CHAR(255) NOT NULL,
    tipo CHAR(255) NOT NULL,
    data_criacao TIMESTAMP NOT NULL,
    
    PRIMARY KEY tb_canal(id)
);

create table tb_call(
	id INT NOT NULL AUTO_INCREMENT,
    canal_id INT NOT NULL,
    registro_id INT NOT NULL,
    descricao CHAR(255) NOT NULL,
    data_envio TIMESTAMP NOT NULL,
    
    PRIMARY KEY tb_call(id),
    FOREIGN KEY (canal_id) REFERENCES tb_canal(id),
    FOREIGN KEY (registro_id) REFERENCES tb_registro(id)
);

create table subs_canal(
	id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    canal_id INT NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES tb_usuario(id),
    FOREIGN KEY (canal_id) REFERENCES tb_canal(id)
);


select * from tb_registro;
select * from tb_usuario;
select * from tb_canal;