import logging
import os


DEBUG = os.getenv("ENVIRONMENT") == "DEV"
HOST = os.getenv("FLASK_RUN_HOST")
PORT = int(os.getenv("FLASK_RUN_PORT", "3000"))

# Loggin Service
logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S"
)