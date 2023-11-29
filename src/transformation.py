import pandas as pd


class Transform:
    def rename_columns(self):
        # Relatório cadop
        relatorio_columns_bd = [
            "registro_ans", "cnpj", "razao_social", "nome_fantasia", "modalidade", "logradouro", "numero", "complemento", "bairro", "cidade", "uf", "cep", "ddd", "telefone", "fax", "endereco_eletronico", "representante", "cargo_representante", "regiao_comercializacao", "data_registro_ans"
        ]

        dict_columns_rename = {
            old_col: relatorio_columns_bd[i] for i, old_col in enumerate(self.df_relatorio.columns)
        }
        self.df_relatorio.rename(columns=dict_columns_rename, inplace = True)
        
        # Renomeando dataframe demonstrativo contábeis
        demo_contab_columns_bd = [
            "data", "reg_ans", "cd_conta_contabil", "descricao", "vl_saldo_inicial", "vl_saldo_final"
        ]

        dict_columns_rename = {
            old_col: demo_contab_columns_bd[i] for i, old_col in enumerate(self.df_demo_contabil.columns)
        }
        self.df_demo_contabil.rename(columns=dict_columns_rename, inplace = True)

        # Renomeando dataframe Operadora beneficiario
        oper_benef_columns_bd = [
            "cd_operadora", "gr_modalidade", "cobertura", "vigencia_plano", "gr_contratacao", "tipo_financiamento", "mes", "id_cmpt", "nr_benef"
        ]

        dict_columns_rename = {
            old_col: oper_benef_columns_bd[i] for i, old_col in enumerate(self.df_oper_benef.columns)
        }
        self.df_oper_benef.rename(columns=dict_columns_rename, inplace = True)

    def standardize_double(self):
        columns_double = [
            "vl_saldo_inicial", "vl_saldo_final"
        ]

        for col_double in columns_double:
            self.df_demo_contabil[col_double] = self.df_demo_contabil[col_double].apply(
                self.adjust_str_to_float
            )
        a = 2

    @staticmethod
    def adjust_str_to_float(value: str) -> float:
        value = str(value)

        try:
            value = value.replace(",", ".")
            return float(value)
        except Exception as e:
            print(f"Erro ao converter {value} para float: {e}")
    
    def resolve_null_values(self):
        print(
            f"""
            Quantidade NaN em demo_contabil: {self.df_demo_contabil.isna().sum().sum()}
            Quantidade NaN em operadora_beneficiario: {self.df_oper_benef.isna().sum().sum()}
            Quantidade NaN em relatorio_cadop: {self.df_relatorio.isna().sum().sum()}
            """.replace("            ", "")
        )

        print("Há alguns valores nulos no arquivo `relatorio_cadop`, mas não são campos essenciais, poderiam ser vazios realmente!")
        self.df_demo_contabil.fillna("", inplace=True)
        self.df_oper_benef.fillna("", inplace=True)
        self.df_relatorio.fillna("", inplace=True)
    
    def standardize_int(self):
        self.df_relatorio["regiao_comercializacao"] = self.df_relatorio["regiao_comercializacao"].apply(
            lambda v: int(v) if v else 0
        )
    
    def standardize_str(self):
        # Tirando espaços vazios desnecessários de strings
        self.df_relatorio["razao_social"] = self.df_relatorio["razao_social"].str.strip()
        self.df_relatorio["logradouro"] = self.df_relatorio["logradouro"].str.strip()