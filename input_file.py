import csv

class InputFile:
    @staticmethod
    def get_data_from_csv(path: str):
        try:
            file = csv.DictReader(open(path, 'r'))
            return file
        except Exception as exc:
            return [{'status': 'Error', 'message': exc}]