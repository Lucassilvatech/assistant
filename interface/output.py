from utils.style import Style

style = Style()

class Output:
    @staticmethod
    def start():
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
        style.print("\nAssistente encerrado.", "bold red")