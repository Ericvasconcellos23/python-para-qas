class Teste:
    """Classe base para qualquer tipo de teste."""

    def __init__(self, nome, prioridade="media"):
        self.nome = nome
        self.prioridade = prioridade
        self._status = "pendente"
        self._duracao_ms = 0

    def executar(self, duracao_ms):
        self._duracao_ms = duracao_ms
        self._status = "excutado"

    def resumo(self):
        return f"[{self._status.upper()}]  {self.nome} ({self._duracao_ms}ms)"


class TesteAPI(Teste):
    """Teste específica para endpoints de API."""

    def __init__(self, nome, endpoint, metodo="GET", prioridade="media"):
        super().__init__(nome, prioridade)  # Chama __init__ do pai
        self.endpoint = endpoint
        self.metodo = metodo
        self.status_code = None

    def executar(self, duracao_ms, status_code=200):
        super().executar(duracao_ms)   # Chama executar() pai
        self.status_code = status_code
        self._status = "passou" if 200 <= status_code < 300 else "falhou"

    def resumo(self):
        base = super().resumo()
        return f"{base} | {self.metodo} | {self.endpoint} -> {self.status_code}"

# Usando DUCK TYPE
class TestePerformance:
    """Não herda de teste"""
    def __init__(self, nome, requisicoes=100):
        self.nome = nome
        self.requisicoes = requisicoes
        self.tempo_medio_ms = 0

    def resumo(self):
        status = "OK" if self.tempo_medio_ms < 500 else "LENTO"
        return f"[{status}] {self.nome} {self.requisicoes}"

teste = Teste("carrinho")
teste_api = TesteAPI(nome="login", endpoint=r"\login", metodo="POST", prioridade="media")
teste_pf = TestePerformance("Barbie", 98)

suite = [teste, teste_api, teste_pf]

for teste in suite:
    print(teste.resumo())