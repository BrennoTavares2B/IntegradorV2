import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger("integrador")
handler = logging.StreamHandler()

formatter = jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

