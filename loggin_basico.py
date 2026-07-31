import logging
import os

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s  [%(levelname)s]  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
# )
#
# logger = logging.getLogger("suite_qa")
#
# logger.debug("Iniciando coleta de dados")
# logger.info("Suite iniciada")
# logger.warning("Ambiente instável")
# logger.error("Endpoint retornou 500")
# logger.critical("Banco inacessível - abortando")
#
# logger_api = logging.getLogger("suite_qa.api")
# logger_auth = logging.getLogger("suite_qa.auth")
# logger_dados = logging.getLogger("suite_qa.dados")
#
#
# logger_auth.info("Autenticando qa@empresa.com")
# logger_api.warning("Tempo de resposta: 3.8s")
# logger_dados.debug("50 usuários carregados")

nivel_map = {
    "dev": logging.DEBUG,  # Tudo
    "hml": logging.INFO,  # Progresso
    "prod": logging.WARNING,  # Só problemas
    "ci": logging.INFO,  # Progresso
}

ambiente = os.environ.get("AMBIENTE", "dev")

nivel = nivel_map.get(ambiente, logging.DEBUG)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s  [%(levelname)s]  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

logger = logging.getLogger("suite_qa")

logger.debug(f"Ambiente detectado: {ambiente} | Nível configurado: {logging.getLevelName(nivel)}")

logger.info(f"Ambiente detectado: {ambiente} | Nível configurado: {logging.getLevelName(nivel)}")


