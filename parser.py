import argparse

class Parser:
    @staticmethod
    def starting_parser(files:list):
        parser = argparse.ArgumentParser(description='-_-')
        parser.add_argument('-f', '--files', nargs='+', type=str, default=files[0],
                            help='Entering file names for calculation')
        parser.add_argument('-r', '--report', type=str, default='average-ctr', help='Entering file name of output file')
        args = parser.parse_args()
        return args