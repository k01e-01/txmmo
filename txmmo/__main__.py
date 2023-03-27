import sys as _sys
from .client import main as _client_main
from .server import main as _server_main
import types as _t


def _isset(args: list[int]) -> bool:
    return any(x in _sys.argv for x in args)


def main():
    _main: _t.FunctionType[int] = (
        _server_main if _isset(["--server", "-s"]) else _client_main
    )
    _sys.exit(_main(verbose=_isset(["-v", "--verbose"])))
