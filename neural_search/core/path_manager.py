from pathlib import Path


class PathManger:
    BASE_DIR = Path(__file__).resolve().parents[1]
    COMMAND_DIR = BASE_DIR / "commands"
    CORE_DIR = BASE_DIR / "core"
    DATA_DIR = Path(__file__).resolve().parents[2] / "data"
