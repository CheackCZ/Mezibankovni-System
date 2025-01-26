from src.logger import setup_logger

# Nastavení loggeru
logger = setup_logger()

# Příklad logování
logger.info("Aplikace spuštěna.")
logger.debug("Detailní informace pro ladění.")
logger.error("Došlo k chybě při zpracování příkazu.")
