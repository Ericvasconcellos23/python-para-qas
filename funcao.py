# def exibir_status_teste(nome_teste, status):
#     print(f"Teste: {nome_teste} | status: {status}")
#
# # Chamando o parâmetro da função
# exibir_status_teste(nome_teste="login credenciais válidas", status='PASSOU' )
#
# exibir_status_teste("login com senha incorreta",'PASSOU' )
#
# exibir_status_teste("login sem preencher",'PASSOU' )


# def classificar_status_code(codigo):
#     if 200 <= codigo < 300:
#         print(f"status {codigo}: Sucesso")
#     elif 400 <= codigo < 500:
#         print(f"status {codigo}: Erro do cliente")
#     elif 500 <= codigo < 600:
#         print(f"status {codigo}: Erro do servidor")
#
# classificar_status_code(200)
# classificar_status_code(401)
# classificar_status_code(501)


# # Calculando e devolvendo resultado com return
#
# def calcular_taxa_sucesso(total, aprovados):
#     if total == 0:
#         return 0
#     return(aprovados / total) * 100
#
# taxa = calcular_taxa_sucesso(15, 8)
# print(f"Taxa de sucesso: {taxa}%")


# Toda função do python retorna None quando não há um return

# def logar_acao(acao):
#     print(f"[LOG] Ação executada: {acao}")
#
# resultado = logar_acao("clicou no botão salvar")
# print(resultado)  # None

# Usando o return para encerrar uma funçãp antes do fim
#
# def validar_campo_obrigatorio(campo, valor):
#     if not valor:
#         print(f"[ERRO] Campo  '{campo}' está vazio! ")
#         return # Encerra aqui, não executa o resto
#     print(f"[OK] campo '{campo}' preencido: {valor}")
#
# validar_campo_obrigatorio(campo = "Busca", valor = "Busca")


# Escopo de variáveis local (Dentro da função) e Global (Fora da função)

# ambiente_global = "Produção"
#
# def configurar_teste():
#     ambiente_local = "Homologação"
#     print(ambiente_global) # Funciona
#     print(ambiente_local)  # Funciona (leitura)
#
# configurar_teste()
# # print(ambiente_local) # ERRO: variável não existe aqui

# Variáveis com o mesmo nome más com escopos diferentes

# url_base = "http://apiproducao.com"
#
# def obter_url_teste():
#     url_base = "http://apihomologacao.com" # Local, não altera a Global
#     print(url_base) # Homologação
#
# obter_url_teste()
# print(url_base) # Produção (inalterada)

# Mudando a variável Global dentro da Função ( Não recomendado )

# url_base = "http://apiproducao.com"
#
# def obter_url_teste():
#     global url_base
#     url_base = "http://apihomologacao.com.br"
#     print(url_base) # Homologação
#
# obter_url_teste()
# print(url_base)

# Chamando uma função dentro da outra

def formatar_resultado(nome, status):
    icone = "✅" if status == "PASSOU" else "❌"
    return f"{icone} {nome}: {status}"

def calcular_taxa_sucesso(total, aprovados):
    if total == 0:
        return 0
    return(aprovados / total) * 100

def gerar_relatorio_suit(nome_suite, resultados):
    print(f" Suite: {nome_suite}")
    for teste, status in resultados:
        linha = formatar_resultado(teste, status) # Chama outra função
        print(f" {linha}")

    total = len(resultados)
    aprovados = sum(1 for _, s in resultados if s == "PASSOU")
    taxa = calcular_taxa_sucesso(total, aprovados) # Reutilizar
    print(f" Taxa de sucesso: {taxa}%")

testes_login = {
    ("login válido", "PASSOU"),
    ("login inválido", "PASSOU"),
    ("login sem senha", "FALHOU"),
    ("login bloqueado", "PASSOU"),
}

testes_cadastro = {
    ("cadastro completo", "PASSOU"),
    ("cadastro sem email", "PASSOU"),
    ("cadastro duplicado", "FALHOU"),
}

gerar_relatorio_suit("login", testes_login)
gerar_relatorio_suit("cadastro", testes_cadastro)