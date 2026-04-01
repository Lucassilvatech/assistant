from core.engine import Assistant
from core.history import History
from interface.output import Output
from interface.errors import ErrorHandler
from config.logging_config import LoggingConfig
from utils.logger import Logger


LoggingConfig.setup_logging()
logger = Logger.get_logger(__name__)

class Runner:
    @staticmethod
    def run():
        assistant = Assistant()
        history = History()

        history.load_history()
        Output.start()
        logger.info("Runner initialized.")
        while True:
            try:
                user_input = Output.get_input()

                if user_input.lower() == "sair":
                    history.save_history()
                    Output.exit()
                    break

                response = assistant.handle(user_input)
                Output.show_response(response)

            except KeyboardInterrupt:
                history.save_history()
                Output.exit()
                break

            except Exception as e:
                ErrorHandler.handle(e)