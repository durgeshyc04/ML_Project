from pathlib import Path
from typing import List
from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str = "requirements.txt") -> List[str]:
    """
    Return a cleaned list of requirements suitable for install_requires.

    - If requirements.txt is missing, returns an empty list.
    - Strips blank lines and comments.
    - Ignores editable installs (-e .), local file paths (file:, ., ..) to avoid pip invoking this package again.
    - Keeps git+ and normal package specifiers.
    """
    path = Path(file_path)
    if not path.exists():
        return []

    # read and normalize lines
    raw_lines = path.read_text(encoding="utf-8").splitlines()
    cleaned: List[str] = []
    for ln in raw_lines:
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        # ignore editable installs and local file/path entries that would cause pip to try to install this project
        if ln.startswith("-e") or ln.startswith("file:") or ln.startswith(".") or ln.startswith(".."):
            continue
        cleaned.append(ln)
    return cleaned

setup(
    name="ML_Project",
    version="0.0.1",
    author="Durgesh",
    author_email="durgeshyc04@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
