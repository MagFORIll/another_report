import csv

class OutputFile:
    @staticmethod
    def upload_data_to_csv(new_path: str, data):
        with open(new_path, 'w', newline='') as output_file:
            output_file = csv.writer(output_file)
            output_file.writerow(['title', 'ctr', 'retention_rate'])
            for line in data: # line data[line][0] data[line][1]
                output_file.writerow([line, data[line][0], data[line][1]])