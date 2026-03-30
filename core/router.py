from skills.time_skill import get_time
from skills.greet_skill import greet

class Router:
    def route(self, text: str) -> str:
        text = text.lower()

        if "hora" in text:
            return get_time()

        if "oi" in text or "olá" in text:
            return greet()

        return "Não entendi. Pode repetir?"