# Operações e Métodos
# email = "QA@EMPRESA.COM"
# email_normalizada = email.lower() # nova String
# print(email)
# print(email_normalizada)

# corpo = '{"status": "error", "message": "Token expirado"}'
#
# print("erro" in corpo)           # True
# print("Token expirado" in corpo) # True
# print("sucess" in corpo)         # False
#
# senha = "abcdefgh"
# print(len(senha) >= 8)  # False - Senha inválida

# Métodos de Busca e Verificação( Sartswith() e endswith())
# linha_log = "ERRO: falha na autenticação do usuário"
# print(linha_log.startswith("ERRO"))
# print(linha_log.startswith("WARMING"))
# print(linha_log.endswith("usuário"))

# find() e count(): find retorna a posição da primeira ocorrência
# count retorna quantas vezes o texto aparece
# query = "user_id=42&status=active&role=admin&status=pending"
# print(query.find("status"))  # 11 - posição da primeira ocorrência
# print(query.count("status")) # 2 - aparece duas vezes
# print(query.count("role"))   # 1
#
# # Verifica presença sem precisar checar o índice:
# campo = "email"
# print(query.find(campo) != -1) # False o campo não existe

# Métodos de Transformação: strip(), lstrip() e rstrip()
# strip remove todos os espaços na string
# lstrip remove espaços a esquerda da sting
# rstrip remove espaços a direita da string
# email = "  usuario@teste.com  "
# print(email.strip())  # 'usuario@teste.com
# print(email.lstrip()) # 'usuario@teste.com  '
# print(email.rstrip()) # '  usuraio@teste.com'

# # lower(), upper() e title()
# ambiente = "PRODUÇÃO"
# # lower: Tudo em minúsculo
# print(ambiente.lower())   # produção
#
# nome = "maria clara"
# # title: Só a primeira letra da string em maiúsculo
# print(nome.title())  # Maria Clara
#
# # upper: Tudo em maiúsculo
# print(nome.upper())  # MARIA CLARA

# replace() substitui todas as ocorrências de um texto por outro
# url_template = "https://api.exemplo.com/v1/{recurso}/{did}"
# url = url_template.replace("{recurso}", "usuarios").replace("{did}", "99")
# print(url) # https://api.exemplo.com/v1/usuarios/99

# split() divide uma string em lista
# csv_linha = "id,nome,email,perfil,status"
# campos = csv_linha.split(",")
# print(campos)

# join () une uma lista em string
# ambientes = ["dev", "hml", "prod"]
# print(", ".join(ambientes))  # dev, hml, prod
# print("| ".join(ambientes))  # dev | hml | prod

# segmentos = ["https://api.exemplo.com", "v2", "pedidos", "status"]
# print("/".join(segmentos))

# Aplicação Prática - Validações de QA
# cenário 1 - Validar Content-Type da resposta HTTP
# def validar_content_type(header_value, esperado="application/json"):
#     return esperado in header_value.lower()
#
# header = "application/json; charset=utf-8"
# print(validar_content_type(header))
#
#
# # Cenário 2 - Extrair status code de uma linha de log
# linha_log = "2024-01-15 14:32:01 | POST /login | 401 | 120ms"
# partes = linha_log.split(" | ")
# status_code = partes[2].strip()
# print(status_code)  # 401
# print(status_code == "401")  # True

# Cenário 3 - Normalizar e validar email
def normalizar_email(email_bruto):
    return email_bruto.strip().lower()

emails = ["  Admin@Empresa.COM  ", "usuario@teste.com", "  QA@CORP.BR"]
for e in emails:
    normalizado = normalizar_email(e)
    tem_arroba = "@" in normalizado
    tem_dominio = "." in normalizado.split("@") [-1] if tem_arroba else False
    print(f"'{e.strip()}' -> '{normalizado}' | válido: {tem_arroba and tem_dominio}")




