from src.mcqgenerator.logger import logging

#logging.info("Starting mcq generator")

from dotenv import load_dotenv,dotenv_values

load_dotenv()
config = dotenv_values(".env")
print(config["OPENAI_API_KEY"])
