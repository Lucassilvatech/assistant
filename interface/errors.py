from rich.console import Console

console = Console()


class ErrorHandler:
    @staticmethod
    def handle(error: Exception):
        console.print(f"[bold red]Erro:[/bold red] {str(error)}")