# Aplicação Prática: Validador de Resposta API

class RespostaApi:
    """Representa uma resposta de API para validação"""

    def __init__(self, endpoint, status_code, corpo, tempo_ms):
        self.endpoint = endpoint
        self.status_code = status_code
        self.corpo = corpo
        self.tempo_ms = tempo_ms

    def is_sucesso(self):
        return 200 <= self.status_code < 300

    def is_lento(self, limite_ms):
        return self.tempo_ms > limite_ms

    def tem_campo(self, campo):
        return campo in self.corpo

    def validar(self, campo_obrigatorio=None, limite_ms=500):
        problemas = []
        if not self.is_sucesso():
            problemas.append(f"Status {self.status_code} (esperado 2xx")
        if self.is_lento(limite_ms):
            problemas.append(f"Lento: {self.tempo_ms}ms (limite: {limite_ms}")

        if campo_obrigatorio and not self.tem_campo(campo_obrigatorio):
            problemas.append(f"Campo: '{self.corpo}' ausnte")

        return{
            "endpoint": self.endpoint,
            "status":"OK" if not problemas else "FALHA",
            "problemas": problemas
        }

login = RespostaApi(endpoint="/login", status_code=200, corpo='{"mensagem":"sucesso")', tempo_ms=500)
resultado = login.validar()
print(resultado)