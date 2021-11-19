from argparse import Namespace


def show_eggs(cmd: Namespace) -> None:
    print("here are the eggs!")
    print(cmd)
