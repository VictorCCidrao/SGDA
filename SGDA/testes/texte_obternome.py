import pandas as pd


def obter_nomes(matricula, arquivo_excel):
    try:
        # Lê o arquivo Excel
        df = pd.read_excel(arquivo_excel)

        # Verifica se a matrícula está presente no DataFrame
        if str(matricula) in df["Matrícula"].astype(str).values:
            # Encontra o nome correspondente à matrícula
            nome = df.loc[df["Matrícula"].astype(str) == str(matricula), "Nome"].iloc[0]
            return nome
        else:
            return None
    except Exception as e:
        # Trata exceções de leitura de arquivo aqui
        print(e)
        return False


# Caminho para o arquivo Excel de teste
arquivo_excel_teste = "../media/matriculas.xlsx"

# Teste para uma matrícula existente no arquivo Excel
matricula_existente = "20241173010295"
nome_existente = obter_nomes(matricula_existente, arquivo_excel_teste)
print("Nome para matrícula existente:", nome_existente)

# Teste para uma matrícula inexistente no arquivo Excel
matricula_inexistente = "99999"
nome_inexistente = obter_nomes(matricula_inexistente, arquivo_excel_teste)
print("Nome para matrícula inexistente:", nome_inexistente)
