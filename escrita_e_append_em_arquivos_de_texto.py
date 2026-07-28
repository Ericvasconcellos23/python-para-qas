from pathlib import Path

# Escrita Simples com MODO W

# with open("relatorio_teste.txt", "w", encoding="utf-8") as arquivo:
#     arquivo.write("Relatório de Execução de teste\n")
#     arquivo.write("Suite: Regressão Sprint 42\n")
#     arquivo.write("Ambiente: homologação\n")


# Adicionando conteúdo com MODO 'a' (APPEND)

# Primeira execução

# with open("execucao.log", "a", encoding="utf-8") as log:
#     log.write("[10:00:01] Iniciando suite de testes\n")
#     log.write("[10:00:02] Conectando ao ambiente dev\n")
#
#
# # Segunda execução
#
# with open("execucao.log", "a", encoding="utf-8") as log:
#     log.write("[10:00:03] GET /api/usuarios -> 200 OK\n")
#     log.write("[10:00:04] POST /api/login -> 401 Unauthorized\n")


# Escrevendo Múltiplas Linhas com a FUNÇÂO WRITELINES

# resultados = [
#     "PASSOU: login com usuario valido\n",
#     "PASSOU: listagem de produtos retorna 200\n",
#     "FALHOU: criacao de pedido retorna 500\n",
#     "IGNORADO: teste de pagamento (ambiente sem gateway)\n",
# ]
#
# with open("resultado_casos.txt", "w", encoding="utf-8") as arquivo:
#     arquivo.writelines(resultados)


# Protegendo contra Sobrescrita Acidental

# def salvar_com_portecao(caminho, conteudo):
#     path = Path(caminho)
#
#     if path.exists():
#         print(f"Arquivo já existe: {path.name}")
#         print(f"Para sobrescrever, exclua o arquivo primeiro.")
#         return False
#
#     with open(path, "w", encoding="utf-8") as f:
#         f.write(conteudo)
#     print(f"Arquivo salvo: {path.name}")
#     return True
#
# # Primeira Chamada - Salvar normalmente
# salvar_com_portecao("evidencia_sprint42.txt", "Evidência de execução sprint 42\n")
#
#
# # Segunda Chamada - Bloqueada
# salvar_com_portecao("evidencia_sprint42.txt", "Tentativa de sobrescrita\n")

