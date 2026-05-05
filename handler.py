import os

class Handler:
    @staticmethod
    def start_up():
        path = f'{os.getcwd()}\\docs'
        files = [files for address, dirs, files in os.walk(path)]
        return files, path

    @staticmethod
    def find_files_to_work_with(args:list, path:str):
        try:
            filename = args.files
            temp = filename[:]

            for file in filename:
                for address, dirs, files in os.walk(path):
                    if file in files:
                        temp.remove(file)
            for file in temp:
                filename.remove(file)
            return filename
        except Exception as exc:
            print(f'Ошибка {exc}, попробуйте еще раз')

    @staticmethod
    def calculating_average(file:str, STORAGE:dict):
        for row in file:
            if row['title'] not in STORAGE and float(row['ctr']) > 15 and float(row['retention_rate']) < 40:
                STORAGE[row['title']] = [float(row['ctr']), float(row['retention_rate'])]
        return STORAGE
