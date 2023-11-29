CREATE DATABASE IF NOT EXISTS tp2_ibd;

USE tp2_ibd;


-- Referente ao arquivo relatorio_cadop.csv
CREATE TABLE IF NOT exists relatorio (
	`registro_ans` varchar(6) PRIMARY KEY,
	`cnpj` varchar(14),
	`razao_social` varchar(140),
	`nome_fantasia` varchar(140),
	`modalidade` varchar(140),
	`logradouro` varchar(40),
	`numero` varchar(20),
	`complemento` varchar(40),
	`bairro` varchar(30),
	`cidade` varchar(30),
	`uf` varchar(2),
	`cep` varchar(8),
	`ddd` varchar(4),
	`telefone` varchar(20),
	`fax` varchar(20),
	`endereco_eletronico` varchar(255),
	`representante` varchar(50),
	`cargo_representante` varchar(40),
	`regiao_comercializacao` int,
	`data_registro_ans` date
) CHARACTER SET = "UTF8"
;

# Criando index pra facilitar a busca do ANS
CREATE INDEX ans ON relatorio(registro_ans);


CREATE TABLE IF NOT exists operadora_beneficiario (
	`cd_operadora` varchar(6),
	`gr_modalidade` varchar(50),
	`cobertura` varchar(30),
	`vigencia_plano` varchar(2),
	`gr_contratacao` varchar(50),
	`tipo_financiamento` varchar(50),
	`mes` varchar(6),
	`id_cmpt` varchar(6),
	`nr_benef` int
);

# Criando index pra facilitar a busca do CD_OPERADORA
CREATE INDEX cd_oper ON operadora_beneficiario(cd_operadora);
-- Sem PK



CREATE TABLE IF NOT EXISTS demo_contabil (
	`data` date,
	`reg_ans` varchar(6) NOT NULL,
	`cd_conta_contabil` varchar(50),
	`descricao` varchar(255),
	`vl_saldo_inicial` double,
	`vl_saldo_final` double
);
-- Sem PK

# Criando index pra facilitar a busca do reg_ans
CREATE INDEX reg_ans ON demo_contabil(reg_ans);


CREATE TABLE IF NOT EXISTS teste (
	id int primary key auto_increment,
	random_number int
);