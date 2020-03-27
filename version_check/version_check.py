from typing import Optional, Sequence
import os

def clear_string(version_line: str):
    """
    Get a clean version from the line string containing 'version = xxx'

    Parameters
    ----------
    The line containing the version string

    Returns
    -------
    str
        A clear version without any quotes
    """
    version = version_line.split("=")[-1].strip()
    return version.replace('"', '').replace("'", "")

def main(argv: Optional[Sequence[str]] = None) -> int:
    try:
        with open("pyproject.toml", mode='r') as f:
            lines = f.readlines()
            for line in lines:
                if "version" in line:
                    version1 = line.split("=")[-1].strip()
    except FileNotFoundError:
        return 0

    package_name = "pyphysim"
    try:
        with open(f"{package_name}/__init__.py", mode='r') as f:
            lines = f.readlines()
            for line in lines:
                if "__version__" in line:
                    version2 = line.split("=")[-1].strip()
    except FileNotFoundError:
        return 0

    if not (clear_string(version1) == clear_string(version2)):
        print(f"Version in pyproject.toml is '{version1}', but version in __init__.py is '{version2}'")
        return 1

    return 0


# if __name__ == '__main__':
#     exit(main())


if __name__ == '__main__':
    line = "version = \"0.3\""
    line1 = "version = \"0.3\""
    line2 = "\"0.3\""
    line3 = "version = 0.3"
    line4 = "version = '0.3'"

    assert clear_string(line) == '0.3'
    assert clear_string(line1) == '0.3'
    assert clear_string(line2) == '0.3'
    assert clear_string(line3) == '0.3'
    assert clear_string(line4) == '0.3'
