from pathlib import Path

# caminho = Path("ralatorios") / "2024" / "resultado.txt"
# print(caminho)

# Caminho ansoluto: ponto de partida fixo no sistema
# caminh_absuloto = Path("/home/qa/projeto/tests/fixtures")
#
# # Caminho relativo: relativo ao diretótio atual
# caminh_relativo = Path("tests") / "fixtures" / "usuarios.json"
#
#
# # Diretório atual de execução
# diretorio_atual = Path.cwd()
# # print(diretorio_atual)
#
# # Diretório home do usuário
# home = Path.home()
# print(home)

# arquivo = Path("evidencias/sprint42/login_bug_001.png")
#
# print(arquivo.parent)  # Pasta qu contém o arquivo
# print(arquivo.name)    # Nome completo da extenção
# print(arquivo.suffix)  # Apenas a extenção
# print(arquivo.stem)    # Nome da extenção
# print(arquivo.parts)   # Tupla com cada parte do caminho


# Verificar existência de Arquivos e Pastas

# base = Path.cwd()
#
# pasta_fixtures = base / "fixtures"
# arquivo_config = base / "config.json"
#
# # print(pasta_fixtures.exists())  # True ou False
# # print(pasta_fixtures.is_dir())  # True se for Pasta
# # print(arquivo_config.is_file()) # True se for aquivo
#
# # Padrão defensivo antes de rodar testes
# arquivo_massa = Path("data") / "usuarios_teste.csv"
# if arquivo_massa.exists():
#     print(f"Massa encontrada: {arquivo_massa}")
#
# else:
#     print(f"ATENCAO: massa nao encontrada em {arquivo_massa}")


# Criando pastas automaticamente

# pasta_logs = Path("saida") / "logs" / "regressao"
# pasta_logs.mkdir(parents=True, exist_ok=True)
#
# pasta_evidencias = Path("saida") / "evidencias" / "sprint43"
# pasta_evidencias.mkdir(parents=True, exist_ok=True)

# Listando Arquivos em uma pasta

# pasta = Path("data") / "fixtures"
#
# # Lista Tudo
# for arquivo in pasta.iterdir():  # Lista tudo na pasta (Arquivos e Subpastas)
#     print(arquivo.name)
#
# # Filtrar por extensão
# for aquivo in pasta.glob(".*json"): # Filtra por padrão dentro da pasta
#     print(aquivo.name)
#
# # Busca Recursiva sobre Pastas
# for arquivo in pasta.rglob("*.json"): # Busca recursiva por padrão em subpastas
#     print(arquivo)

# Renomear e Mover Arquivos

# arquivo_origem = Path("saida") / "relatorio.temp.txt"
# arquivo_destino = Path("saida") / "relatorio_final.txt"
#
# arquivo_origem.rename(arquivo_destino)
# # arquivo_origem deixa de existir
# # arquivo_destino passa a exixtir

# Informações extras Sobre o arquivo

arquivo = Path('saida') / "relatorio_final.txt"
stat = arquivo.stat()

print(stat.st_size)      # Tamanho em bytes
print(arquivo.resolve()) # Caminho absoluto completo
print(arquivo.with_suffix('.log')) # Mesmo nome, extensão diferente