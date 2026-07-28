# class ValidadorEndpoint:
#     def __init__(self, endpoint, metodo, requer_auth=False):
#         self.endpoint = endpoint
#         self.metodo = metodo
#         self.requer_auth = requer_auth
#         self._erros = []
#
#     def _validar_formato(self):
#         if not self.endpoint.startswith('/'):
#             self._erros.append("Endpoint deve começar com /")
#
#     def _validar_metodo(self):
#         metodos_validos = {"GET", "POST", "PUT", "PATCH", "DELETE"}
#         if self.metodo.upper() not in metodos_validos:
#             self._erros.append(f"Método '{self.metodo}' não é válido")
#
#     def _validar_auth(self):
#         rotas_publicas = {"/api/health", "/api/status", "/api/version"}
#         if self.endpoint in rotas_publicas and self.requer_auth:
#             self._erros.append("Rota pública não deveria exigir autenticação")
#
#     def validar(self):
#         self._erros = []
#         self._validar_formato()
#         self._validar_metodo()
#         self._validar_auth()
#         return{"endpoint": self.endpoint, "valido": len(self._erros) == 0, "erro": self._erros.copy()}
#
# endpoint = ValidadorEndpoint("/login", "GET", True)
#
# retorno = endpoint.validar()
# print(endpoint.validar())

# class Ambiente:
#     def __init__(self, nome, url):
#         self.nome = nome
#         self._url = url
#
#     @property
#     def url(self):
#         """Getter: retorna a url do ambiente"""
#         return self._url
#
#     @url.setter
#     def url(self, nova_url):
#         """Setter: retorna a url do ambiente"""
#         if not nova_url.startswith('https://'):
#             raise ValueError(f"URL deve começar com https:// ")
#         self.url = nova_url
#
#     @property
#     def esta_ativo(self):
#         """Somente leitura (sem setter)"""
#         return self._url is not None and len(self._url) > 6
#
# homologacao = Ambiente("hml", "https://hml.api.empresa.com")
#
# print(homologacao.url)
# homologacao.url = "https://dev.api.empresa.com"
# print(homologacao.url)

# Utilizando o __str__

class CasoTeste:
    def __init__(self, id_teste, nome, prioridade="média"):
        self.id_teste = id_teste
        self.nome = nome
        self.prioridade = prioridade
        self._status = "pendente"

    def __str__(self):
        return f"[{self._status.upper}()] {self.id_teste}: {self.nome}"

tc = CasoTeste("TC-001", "login válido")

print(tc)       # [PENDENTE] TC-001: Login válido