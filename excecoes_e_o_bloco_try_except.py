# def extrair_campo_reposta(resposta, campo):
#     try:
#         valor = resposta[campo]
#         print(f"[OK] campo '{campo}' encontrado {valor}")
#         return valor
#     except KeyError:
#         print(f"[Erro] campo '{campo}' não existe na resposta")
#         return None
#
# extrair_campo_reposta(resposta={'id': 1, 'nome': 'Marilia'}, campo= 'idade')

# def carregar_massa_de_teste(arquivo):
#     try:
#         with open(arquivo, "r") as f:
#             return f.read()
#     except FileNotFoundError as e:
#         print(f"[FALHA] Arquivo não encontrado: {arquivo}")
#         print(f"[DETALHE] {e}")
#         return None
#     except PermissionError as e:
#         print(f"[FALHA] Sem permissão para ler: {arquivo}")
#         print(f"[DETALHE] {e}")
#         return None
#
# carregar_massa_de_teste('PYTHON_QA.txt')

def carregar_massa_de_teste(arquivo):
    try:
        with open(arquivo, "r") as f:
            return f.read()
    except PermissionError as e:
        print(f"[FALHA] Sem permissão para ler: {arquivo}")
        print(f"[DETALHE] {e}")
        return None
    # Usado para tratar qualquer tipo de erro que não esteja especificado no código.
    except Exception as erro:
        print(f"[FALHA] {erro}")

carregar_massa_de_teste('PYTHON_QA.txt')
