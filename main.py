import tabulate, os

from handler import Handler
from input_file import InputFile
from output_file import OutputFile
from parser import Parser

files, path = Handler.start_up()
args = Parser.starting_parser(files)
filenames = Handler.find_files_to_work_with(args, path)
STORAGE = {}
for file in filenames:
    file = InputFile.get_data_from_csv(os.path.join(path, file))
    Handler.calculating_average(file, STORAGE)
    # print(STORAGE)
STORAGE = dict(sorted(STORAGE.items(), key=lambda x: x[1][0], reverse=True))
# print(STORAGE)

output_filename = args.report + '.csv'
OutputFile.upload_data_to_csv(output_filename, STORAGE)
output_tab = []
count = 1
for key, value in (STORAGE.items()):
    output_tab.append((count, key, value[0], value[1]))
    count += 1
print(tabulate.tabulate(output_tab, headers=['', 'country', 'ctr', 'retention_rate'], tablefmt='grid'))