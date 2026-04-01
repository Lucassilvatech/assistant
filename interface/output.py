from utils.style import Style
from utils.logger import Logger

style = Style()
logger = Logger.get_logger(__name__)

class Output:
    @staticmethod
    def start():
        logger.info("Assistant started.")
        style.print("Assistente iniciado.\n", "bold green")
        style.print("Digite 'sair' para encerrar o assistente.\n", "italic yellow")

    @staticmethod
    def get_input():
        return input("> ")

    @staticmethod
    def show_response(response):
        style.print(f"{response}", "cyan")

    @staticmethod
    def exit():
        logger.info("Assistant exited.")
        style.print("\nAssistente encerrado.", "bold red")