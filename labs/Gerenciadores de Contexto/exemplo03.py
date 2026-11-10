from contextlib import contextmanager
from os import chdir, getcwd

@contextmanager
def cd(path):
    # __enter__
    old_path = getcwd()
    try:
        chdir(path)
        yield # ponto de parada
    except FileNotFoundError:
        pass
    finally:
        chdir(old_path)


print(getcwd())
with cd('/'):
    print(getcwd())
print(getcwd())