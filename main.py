

from src.read_data import read_file


if __name__ == "__main__":
    res = read_file('output/seiseki.txt', 'shift-jis')
    print(res)
