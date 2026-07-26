# Formatação de string com f-string
# status_code = 404
# endpoint = "/usuario/99"
# tempo_resposta = 230
#
# mensagem = f"status: {status_code} | Endpoint: {endpoint} | Tempo: {tempo_resposta}ms"
# print(mensagem)

# usuario = "maria"
# perfil = "admin"
#
# print(f"Usuário: {usuario.upper()}")   # MARIA
# print(f"perfil: {perfil.title()}")     # Admin
# print(f"Tamanho do Nome: {len(usuario)}")
# print(f"Total do pedido: {99.99 * 3}")

# Formatação de números
# taxa_erro = 0.03478
# cobertura = 87.5612
#
# print(f"Taxa de erro:    {taxa_erro:.2f}")
# print(f"Cobertura:       {cobertura:.1f}")

# Separação Porcentagem
# taxa_sucesso = 0.9823
#
# print(f"Taxa de sucesso: {taxa_sucesso:.2%}")
# print(f"Taxa de falha:   {1 - taxa_sucesso:.1%}")

# Separação de Milhar
# total_requisicoes = 1482930
#
# print(f"Total de requisições: {total_requisicoes:,}")

# Aplicação Prática - Relatórios e Logs de QA
# Cenário 1: Resultado de teste com contexto

# def relatar_teste(nome, passou, tempo_ms, detalhe=""):
#     status_label = "PASSOU" if passou else "DETALHE"
#     base = f"[{status_label}] {nome} ({tempo_ms}ms)"
#     if detalhe:
#         base += f" - {detalhe}"
#     return base
#
# print(relatar_teste("Login com credencias válidas", True, 145))
# print(relatar_teste("Login com senha errada", False, 89,
#                     "esperado 401, recebido 200"))
# print(relatar_teste("Exportar relatório CSV", False, 5001,
#                     "Timeout após 5000ms"))


# Cenário 2: Gerar dados de teste nomeados por ambiente
# ambientes = ["dev", "hml", "prod"]
# for i, ambiente in enumerate(ambientes, start=1):
#     usuario = f"qa_user_{ambiente}_{i:02d}@teste.com"
#     senha = f"Senha@{ambiente.upper()}#2024"
#     print(f"Ambiente {ambiente.upper():>4}: {usuario:<35} | Senha: {senha}")

# Cenário 3: Relatório de cobertura de endpoints
# endpoints_testados = [
#     ("GET",    "/usuarios",       True,    95),
#     ("POST",   "/usuarios",       True,    87),
#     ("DELETE", "/usuarios/{id}",  False,    0),
#     ("GET",    "/produtos",        True,   100),
#     ("GET",    "/usuarios/{id}",  False,     0),
#
# ]
#
# print(f"{'Método':<8}  {'Endpoint':<25}  {'Coberto':>8}  {'Cobertura':>12}")
# print("-" * 59)
# for metodo, ep, coberto, cobertura in endpoints_testados:
#     status_icon = "Sim" if coberto else "Não"
#     print(f"{metodo:<8} {ep:<25} {status_icon:>8} {cobertura:>11}%")
#
# cobertos = sum(1 for _, _, c, _ in endpoints_testados if c)
# total = len(endpoints_testados)
# print(f"{'TOTAL':<34} {cobertos}/{total} endpoints  {cobertos/total:.0%}")