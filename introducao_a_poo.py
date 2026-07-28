# class Usuario :
#     # Representa um usário so sistema sob teste.
#     pass # Classe vazia por enquanto
#
# # Criando objetos (intâncias)
# usuario1 = Usuario()
# usuario2 = Usuario()
#
# print(usuario1)
# print(usuario2)
# print(usuario1 is usuario2 )

# class AmbienteTeste :
# #     # Representa um usário so sistema sob teste.
#     def __init__(self, nome, url, ativo=True):
#         self.nome = nome     # atributo instância
#         self.url = url       # atributo instância
#         self.ativo = ativo   # atributo com valor padrão
#
# # Criando objetos com dados
# dev = AmbienteTeste("dev", "https://dev.api.empresa.com")
# hml = AmbienteTeste("hml", "https://hml.api.empresa.com")
# prod = AmbienteTeste("prod", "https://api.empresa.com", ativo=False)
#
# print(dev.nome)
# print(prod.nome)

# Métodos de Instância

# class CasoTeste:
#     """ Representa um caso de Teste"""
#     def __init__(self, nome, endpoint, metodo="GET"):
#         self.nome = nome
#         self.endpoint = endpoint
#         self.metodo = metodo
#         self.status = "pendente"
#         self.duracao_ms = 0
#
#
#     def executar(self, duracao_ms, sucesso=True):
#         """Simula a execução do caso de teste."""
#         self.duracao_ms = duracao_ms
#         self.status = "passou" if sucesso else "falhou"
#
#
#     def resumo(self):
#         """Retorna string formatada com resumo"""
#         return(
#             f"[{self.status.upper()}] {self.metodo} {self.endpoint}"
#             f"-{self.nome} ({self.duracao_ms} ms)"
#         )
#
#
# teste_login = CasoTeste(nome="login", endpoint=r"\login", metodo="POST")
#
# teste_login.executar(duracao_ms=1000, sucesso=True)
#
# teste_perfil = CasoTeste(nome="perfil", endpoint=r"\perfil", metodo="GET")
#
# teste_perfil.executar(duracao_ms=5000, sucesso=False)
#
# teste_logout = CasoTeste(nome="logout", endpoint=r"\logout", metodo="POST")
#
# teste_logout.executar(duracao_ms=300, sucesso=True)
#
#
#
# # Objetos em Coleções
#
# suite = [teste_login, teste_perfil, teste_logout]
#
# total = len(suite)
# passou = 0
# for teste in suite:
#     if teste.status == "Passou":
#         passou += 1
#
# for teste in suite:
#     print(teste.resumo())
#
# print(f"Total: {total} | Passou: {passou} | Falhou: {total - passou}")

