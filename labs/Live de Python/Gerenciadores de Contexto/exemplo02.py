from sys import stdout

class PrintMock:
    def __enter__(self):
        self.old_print = stdout.write
        self.file = open('log.txt', 'a')
        stdout.write = self.log

    def log(self, arg):
        self.file.write(f'{arg}\n')

    def __exit__(self, type, value, traceback):
        stdout.write = self.old_print
    