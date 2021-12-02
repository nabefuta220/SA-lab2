"""
プログラム実行時の根幹部分
"""

from src.read_data import read_file
import pandas as pd

if __name__ == "__main__":
    res = read_file('output/seiseki.txt', 'shift-jis')
    res.pop()
    data = pd.DataFrame(res[1:], columns=res[0])
    print(data)
