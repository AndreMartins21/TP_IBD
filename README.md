# Trabalho Prático 2 - Introdução a Banco de Dados
### => Alunos: </br> André Augusto Moreira Martins (2021035144)
### Gilmar Junio de Macedo Guedes
### Pedro Afonso
### Isabelle

<details>
    <summary> <b>OBJETIVO DO TP</b> </summary>
    - O objetivo deste trabalho prático é promover o acesso, coleta, gerenciamento, integração e análise de conjuntos de dados públicos; </br></br>
    - Idealmente, o resultado desse trabalho poderia ser republicado, sendo que o conteúdo ainda seria formado por dados públicos, mas com as vantagens decorrentes da análise e integração que serão
feitos no escopo do TP.
</details>


<details>
<summary> <b>ETAPAS </b> </summary>
1- Escolher dois ou mais conjuntos de dados em alguma fonte de dados públicos e abertos;

</br>2- Carregar esses dados em um gerenciador de bancos de dados relacional, como o PostgreSQL ou outro, e combinar esses dados, de modo a permitir análises integradas;

3- Realizar uma análise exploratória dos dados;

4- Apresentar uma análise crítica das fontes de dados utilizadas

5- Apresentar análises referentes à combinação ou integração de dados.
</details>


### Etapa 1:
Para o trabalho, fiz uso de 3 conjunto de dados do ramo da saúde, disponibilizados pela ANS (dados abertos). São eles:
[1°: Relatorio_cadop.csv](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)

[2°: demonstracoes_contabeis_2T2023.csv](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/)

[3°: beneficiarios_operadoras_e_carteira.csv](https://dadosabertos.ans.gov.br/FTP/PDA/beneficiarios_vinculos_tipo_contratacao_vda/)


### Etapa 2:
Para o carregamento dos dados apresentados, usufrui do SGBD relacional MariaDB, com o principal objetivo de aprender mais sobre esse gerenciador.

----------------------------------
<details>
<summary> <b>Motivações para uso do MariaDB </b> </summary>
-> Desempenho: MariaDB foi projetado para alto desempenho (PS: Para o trabalho, não utilizei da capacidade e desempenho do BD com uma frequência alta, o que não me levou a perceber tais otimizações. Mas aproveitei para aprender sobre, caso um dia necessite utilizá-lo.);

</br>
-> Open Source: Promovendo uma forte comunidade de desenvolvedores e usuários colaborando para a melhoria do gerenciador;

</br>
-> Compatibilidade com MySQL: MariaDB pode substituir o MySQL sem muitos problemas, uma vez que esse SGBD é originado do MySQL, tornando-o mais tranquilo para quem está familiarizado com esse outro gerenciador;

</br>
-> Comunidade ativa: É possível encontrar várias documentações, fóruns e suportes sobre configurações e dicas para o melhor uso desse SGBD
</br></br>

Outras vantagens de se utilizar o MariaDB, em relação ao MySQL, por exemplo, podem ser encontradas [aqui](https://www.cloudways.com/blog/mariadb-vs-mysql/).
</details> 

----------------------------------

</br>

Para prosseguir com as inserções dos datasets apresentados, bem como as análises em cima dos dados, foi-se necessário a criação de 3 tabelas no banco de dados, uma para cada CSV. Os códigos SQL encontram-se em `src/code.sql`.

Antes de carregar as informações, foi necessário o processo de transformação dos dados, para que haja uma garantia que os dados serão inseridos corretamente no BD de acordo com seus tipos (float, date, varchar,...). Essas transformações ocorreram no arquivo `src/transformation.py`.

Com os dados tratados, foi-se possível realizar o carregamento das informações no BD (arquivo de carregamento: `src/transformation.py`).


### Problemas encontrados (rascunho):
- No relatório cadop há alguns valores vazios (NaN), que foram tratados;

- Campos de valores (demo_contabeis) não estavam padronizados para o data type Double, tornando-se necessária uma padronização;

- Ao seguir o dicionário de dados para o relatorio_cadop, o campo 'modalidade' teoricamente seria um varchar de tamanho 2, mas na realidade há mais caractéres que o informado;

- As tabelas `demo_contabil` e `operadora_beneficiario` não apresentam chave primária. Não há praticidade terem um id único
