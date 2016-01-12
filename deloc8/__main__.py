import sys
import argparse
import logging


def main():
    if len(sys.argv) == 1:
        sys.argv.append('-h')

    p = argparse.ArgumentParser()
    p.add_argument("--debug", action="store_true", help="Show debug output.")
    sub_parsers = p.add_subparsers(metavar='command', dest='cmd')

    from . import main_listdeps
    main_listdeps.configure_parser(sub_parsers)
    from . import main_versym
    main_versym.configure_parser(sub_parsers)

    args = p.parse_args()

    if args.debug:
        logging.disable(logging.NOTSET)
        logging.basicConfig(level=logging.DEBUG)

    try:
        args.func(args, p)
    except:
        # TODO(rmcgibbo): nice message
        raise


if __name__ == '__main__':
    main()
