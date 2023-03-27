from textual.app import App
from textual.widgets import Placeholder
from textual.binding import Binding

import websockets.client as ws


class GameApp(App[int]):
    BINDINGS = [
        Binding("q", "quit", "Quit the app"),
    ]

    TITLE = "txmmo"

    verbose = False  # enable verbose logging

    def compose(self):
        yield Placeholder()

    async def action_quit(self) -> None:
        self.exit(0)
