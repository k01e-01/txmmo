from .app import GameApp


def main(verbose: bool) -> int:
    app = GameApp()
    app.verbose = verbose
    return app.run()
