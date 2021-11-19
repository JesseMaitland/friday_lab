from argparse import ArgumentParser  # This is the standard library arg parser, and it works great.
from dotenv import load_dotenv
from .beans import beans
from .eggs import show_eggs

# load my .env file at the top level of my __init__.py file so I know it will always be loaded
# no matter what entry point is called
load_dotenv()


def parse_args():

    # This is the root node of the main parser tree.
    parser = ArgumentParser()
    sub_parser = parser.add_subparsers(dest='command')
    sub_parser.required = True

    # parser for the infamous beans command
    beans_command_parser = sub_parser.add_parser('beans', description="Use this command to order some beans!")
    beans_command_parser.set_defaults(func=beans)

    beans_command_parser = sub_parser.add_parser('eggs', description="Use this command to order some beans!")
    beans_command_parser.set_defaults(func=show_eggs)

    # Parse the arguments passed into the program from the entry point.
    return parser.parse_args()
