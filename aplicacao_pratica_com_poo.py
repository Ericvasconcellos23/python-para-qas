class ConfiguracaoTeste:
    AMBIENTES_VALIDOS = {"dev", "hml", "ci"}
    BROWSERS_VALIDOS = {"chrome", "firefox", "edge"}

    def __init__(self, ambiente="hml", browser="chrome", timeout =30):
        self.ambiente = ambiente  # setter valida
        self.browser = browser    # setter valida
        self._timeout = timeout

    @property
    def ambiente(self):
        return self._ambiente

    @ambiente.setter
    def ambiente(self, valor):
        if valor not in self.AMBIENTES_VALIDOS:
            raise ValueError(f"Ambient: '{valor}' invalido")
        self._ambiente = valor

    @property
    def browser(self):
        return self._ambiente

    @browser.setter
    def browser(self, valor):
        if valor not in self.BROWSERS_VALIDOS:
            raise ValueError(f"Ambient: '{valor}' invalido")
        self._browser = valor

    @property
    def base_url(self):
        """URL calculada a partir do ambiente (somente leitura)"""

        urls = {
            "dev": "https://dev.api.empresa.com",
            "hml": "https://hml.api.empresa.com",
            "prod": "https://api.empresa.com",
        }
        return urls[self._ambiente]

config = ConfiguracaoTeste("hml", "chrome", 15)
print(config.ambiente)     # hml
print(config.base_url)     # https://hml.api.empresa.com

# Mudar ambiente (setter valida)
config.ambiente = "dev"
print(config.ambiente)     # dev
print(config.base_url)     # https://dev.api.empresa.com (recalculou sozinho)

# Tentar ambiente inválido
config.ambiente = "staging"  # ValueError: Ambient: 'staging' invalido