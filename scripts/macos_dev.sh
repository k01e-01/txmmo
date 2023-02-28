#!/bin/bash
pipx uninstall txmmo
maturin build
pipx install ./target/wheels/txmmo-0.1.0-cp310-cp310-macosx_10_7_x86_64.whl
txmmo