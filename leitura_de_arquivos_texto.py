from pathlib import Path

# Lendo arquivos utizando o READ (r)

# OBS utilizar o .READ somente para arquivos pequenos, para arquivos grandes utilizar o .READLINES

# with open("saida/log_execucao.txt", "r", encoding="utf-8") as arquivo:
#     texto_completo = arquivo.read()
#
# print(type(texto_completo))  # <class 'str'>
# print(len(texto_completo))   # Total de caracteres
# print(texto_completo)

# Utilizando o READLINES

# with open("saida/log_execucao.txt", "r", encoding="utf-8") as arquivo:
#     linhas = arquivo.readlines()
#
# print(type(linhas))
# print(linhas[0])
# print(linhas[-1])
# print(linhas)


# Iterando linha por linha

# with open("saida/log_execucao.txt", encoding="utf-8") as arquivo:
#     for linha in arquivo:
#         print(linha.strip())

# Filtrando Linhas Durante a Leitura

# Extraindo apenas linhas de falha de um log de execução

# with open("saida/log_execucao.txt", encoding="utf-8") as arquivo:
#     for linha in arquivo:
#         linha_limpa = linha.strip()
#         if "FAIL" in linha_limpa or "ERROR" in linha_limpa:
#             print(linha_limpa)
#
# # Contar Resultados por Status
#
# contagem = {"PASS": 0, "FAIL": 0, "ERROR": 0, "INFO": 0}
#
# with open("saida/log_execucao.txt", encoding="utf-8") as arquivo:
#     for linha in arquivo:
#         for status in contagem:
#             if status in linha:
#                 contagem[status] += 1
#                 break
# print(contagem)

# Tratando arquivos inexistentes

# arquivo = Path("saida/massa_usuarios.txt")
#
# try:
#     conteudo = arquivo.read_text(encoding="utf-8")
# except FileNotFoundError:
#     print(f"Arquivo não encontrado: {arquivo}")
#     print("Verifique se o arquivo de massa foi gerado corretamente")