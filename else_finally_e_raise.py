import requests

# def consultar_endpoint(url, payload):
#     try:
#         if not url.startswith("http"):
#             raise ValueError(f"URL inválida: {url}")
#         if not payload:
#             raise ValueError("Payload vazia não permitido")
#
#         # Simulando resposta de API(sem chmada real)
#         resposta = {"status": 200, "body": {"usuario": "qa_tester", "ativo": True}}
#
#     except ValueError as e:
#         print(f"[ERRO] Validação falhou: {e}")
#         return None
#
#     else:
#         # Só executa se o try passou sem erros
#         print(f"[OK] Requisisção enviada para : {url}")
#         print(f"[OK] Status: {resposta['status']}")
#         print(f"[OK] Usuário: {resposta['body']['usuario']}")
#         return resposta
#
#
# # Teste 1: Tudo correto
# print("=== Teste 1: requisição válida ===")
# resultado = consultar_endpoint("http://localhost:8000/", {"user": "qa", "senha": "1234"})
# print(resultado)
# print()
#
# # Teste 2: URL inválida (sem http)
# print("=== Teste 2: URL sem http ===")
# consultar_endpoint("localhost:8000/", {"usuario": "qa"})
#
# print()
#
# # Teste 3: payload vazio
# print("=== Teste 3: payload vazio ===")
# consultar_endpoint("http://localhost:8000/", {})

# Utilizando o Finally

# def executar_suite_testes(nome_suite, nome_teste, resultado):
#     """
#     nome_teste: Lista de strings com o nome de cada teste
#     resultados: Lista de booleanos - True = passou, False = falhou
#
#     """
#     print(f"\n{'='*45}")
#     print(f"[INÍCIO] suite: {nome_suite}")
#     print(f"{'='*45}")
#
#     aprovados = 0
#     total = len(nome_teste)
#
#     try:
#         for i in range(total):
#             nome = nome_teste[i]
#             passou = resultado[i]
#             if passou:
#                 aprovados += 1
#                 print(f"PASSOU {nome}")
#             else:
#                 print(f"FALHOU {nome}")
#
#         if aprovados == 0:
#             raise RuntimeError("Nenhum teste passou - possivel problema de configuração")
#
#     except RuntimeError as e:
#         print(f"\n[CRÍTICO] {e}")
#
#
#     finally:
#         # Sempre executa - teardown garantido
#         taxa = (aprovados/total * 100) if total > 0 else 0
#         print(f"\n[ENCERRADO] suite '{nome_suite}': {aprovados}/{total} passaram ({taxa:.0f}%)")
#         print(f"[TEARDOWN] conexões encerradas, dados temporários limpos.")
#
# # Suite 1: maoria passou
# nome_login = ["GET /usuarios retorna 200", "POST /login válido", "GET sem token retorna 401",
#               "DELETE retorna 204"]
#
# resultados_login = [True, True, False, True]
#
# # Suite 2: falha total
# nomes_criticos = ["Conectar ao banco de testes", "Carregar massa de dados"]
# resultados_criticos = [False, False]
#
# executar_suite_testes("Autenticação e Usuários", nome_login, resultados_login)
# executar_suite_testes("Suite com falha total", nomes_criticos, resultados_criticos)

def validar_status_code(codigo):
    """ Valida se o código HTTP está no range válido e é do tipo correto."""
    if not isinstance(codigo, int):
        raise TypeError(
            f"Status code deve ser int, receboeu {type(codigo).__name__}: {codigo!r}"
        )
    if not (100 <= codigo <= 599):
        raise ValueError(
            f"Status code fora do range HTTP válido (100-599): {codigo}"
        )
    return True


def classificar_resposta(codigo):
    """ Classifica o status code e levanta exceção se iválido."""
    validar_status_code(codigo) # Lança TypeError ou ValueError se inválido

    categorias = {2: "Sucsso", 3: "Redirecionamneto", 4: "Erro cliente", 5: "Erro servidor"}
    categorias = categorias.get(codigo //100, "Desconhecido")
    print(f"[OK] {codigo} -> {categorias}")


# Testenado com diferentes entradas
entradas = [200, 201, 30, 404, 500, "200", 999, None]

for entrada in entradas:
    try:
        classificar_resposta(entrada)
    except TypeError as e:
        print(f"[TypeError] {e}")
    except ValueError as e:
        print(f"[ValueError] {e}")