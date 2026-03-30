from core.router import Router
from core.history import History

class Assistant:
    def __init__(self):
        self.router = Router()
        self.history = History()

    def handle(self, text: str) -> str:
        self.history.save_history()
        return self.router.route(text)
        