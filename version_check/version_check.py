from typing import Optional, Sequence
import os


# Note: It would be easier to use some toml parsing library, but since there is
# none in the python standard library we don't want to add a dependency to an
# external library just to read the version and package name from the
# "pyproject.toml" file


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

            # Get the package name from the pyproject.toml file -> we will
            # assume the __init__ file containing the __version__ variable is in
            # a folder whose name is the package name
            for line in lines:
                if "name" in line:
                    # The line with package name in the pyproject.toml file is
                    # something such as
                    # name = "package_name"
                    #
                    # We can get the project name (without quotes) with the line
                    # below
                    package_name = line.split("=")[-1].strip()[1:-1]
                    break

            # Get the version from the pyproject.toml file
            for line in lines:
                if "version" in line:
                    version1 = line.split("=")[-1].strip()
                    # Break the for loop -> When dependencies are optional they
                    # their line in `pyproject.toml` is something similar to
                    # `library_name = {version = "^5.01", optional = true}`
                    #
                    # If we do not break the loop the last line with "version"
                    # string will be the one used and thus the version returned
                    # will be the version of some optional dependency instead of
                    # the main project. Assume the version of the main project
                    # comes before in the toml file we can fix this by breaking
                    # the first time we find a "version" string.
                    break
    except FileNotFoundError:
        return 0

    try:
        with open(f"{package_name}/__init__.py", mode='r') as f:
            lines = f.readlines()

            # Get the version from the __init__ file
            for line in lines:
                if "__version__" in line:
                    version2 = line.split("=")[-1].strip()
    except FileNotFoundError:
        print(f"There is no '{package_name}/__init__.py' file in folder {os.getcwd()} -> version check will just pass")
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
