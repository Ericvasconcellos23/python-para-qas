from dataclasses import dataclass

# class ResultadoTeste:
#     def __init__(self, nome, status, duracao_ms):
#      self.nome = nome
#      self.status = status
#      self.duracao_ms = duracao_ms
#      def __str__(self):
#         return f"[{self.status.upper()}] {self.nome} ({self.duracao_ms}ms)"
#
# class SuiteTeste:
#  """Suite que CONTÉM resultados de testes."""
# def __init__(self, nome):
#          self.nome = nome
#          self._resultados = []
# def adicionar(self, resultado):
#         self._resultados.append(resultado)
#
# @property
# def total(self):
#     return len(self._resultados)
#
# @property
# def passou(self):
#     count = 0
#     for r in self._resultados:
#         if r.status == "passou":
#             count += 1
#     return count
# @property
# def falhou(self):
#     return self.total - self.passou
#
# @property
# def taxa_sucesso(self):
#      if self.total == 0:
#          return 0.0
#      return round((self.passou / self.total) * 100, 1)
#
# def relatorio(self):
#     linhas = [f"Suite: {self.nome}", "-" * 50]
#     for r in self._resultados:
#          linhas.append(f" {r}")
#     linhas.append("-" * 50)
#     linhas.append(
#          f"Total: {self.total} | Passou: {self.passou} |"
#          f"Falhou: {self.falhou} | Taxa: {self.taxa_sucesso}%"
#      )
#     return "\n".join(linhas)
#
#
# # Usando composição
#
# suite = SuiteTeste("Smoke Test - API Auth")
#
# suite.adicionar(ResultadoTeste("Login válido", "passou", 120))
#
# suite.adicionar(ResultadoTeste("Login inválido", "passou",95))
#
# suite.adicionar(ResultadoTeste("Token expirado", "falhou",200))
#
# suite.adicionar(ResultadoTeste("Logout", "passou", 80))
#
# print(suite.relatorio())

# Utilizando DataClasse

# @dataclass
# class Usuario:
#     nome: str
#     email: str
#     perfil: str = "viwer"
#     ativo: bool = True
#
# # Criando objetos (mesma sintaxe de qualquer classe)
#
# u1 = Usuario("Ana QA", "ana@emprresa.com", "admin")
# u2 = Usuario("Carlos dev", "carlos@emprresa.com")
# u3 = Usuario("Manoela QA", "manoela@emprresa.com", "admin")
#
#
# # __repr__ gerado automaticamente
# print(u1)
# print(u2)
#
# # __eq__ gerado automaticamente (compara todos os campos)
# print(f"\n u1 == u3? {u1 == u3}" )
# print(f"u1 == u2? {u1 == u2}" )

# Utilizando o DataClasse com Massa de Teste

@dataclass
class CredencialTeste:
    usuario: str
    senha: str
    esperado: str
    descricao: str = ""

# Massa de Teste limpa e tipada

massa_login = [
    CredencialTeste("Maria Antonela", "Adm@123", "sucesso", "Admin valido"),
    CredencialTeste("Gedalva Muniz", "Gead@123", "erro", "User Inválido"),
    CredencialTeste("Joana Dark", "Joane@454", "sucesso", "Admin valido"),
    CredencialTeste("", "qualquer um", "erro", "Sem email"),
]

print("Massa de teste para Login:")
print(f"{'Descrição':<20} {'Usuário':<25} {'Esperado':<10}")
print("-" * 50)

for c in massa_login:
    print(f"{c.descricao:<20} {c.usuario:<25} {c.esperado:<10}")

# Filtrar cenário de erro
erros = []
for c in massa_login:
     if c.esperado == "erro":
        erros.append(c)

print(f"\n Cenários de erro: {len(erros)}")
for e in erros:
    print(f"  {e.descricao} | {e.usuario}")
