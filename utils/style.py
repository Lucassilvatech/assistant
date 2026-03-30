from rich.console import Console

console = Console()
 
class Style:
    @staticmethod
    def print(text: str, style: str = None):
        if style:
            console.print(f"[{style}]{text}[/{style}]")
        else:
            console.print(text)
