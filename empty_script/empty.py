import argparse
import os
import re
from colorama import init, Fore, Back, Style

# Best way to have colorama is to initialize virtual environment
# and install colorama there:
# 1. python -m venv myenv
# 2. pip install colorama


def main():

    parser = argparse.ArgumentParser(prog="Empty Script",
        description='TODO: Provide description of the script here')
    parser.add_argument('-t', "--target", type=str, help='TODO: provide description of the param here')

    args = parser.parse_args()

    print(Fore.GREEN + "This will be owsome script some day")



if __name__ == '__main__':
    exitCode = main()
    print(Style.RESET_ALL)
    exit(exitCode)