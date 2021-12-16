"""
pokemon.txtを主成分分析する
"""
import pandas as pd

from src.pca import pc_analyze
from src.read_data import read_file

if __name__ == "__main__":
    # ファイルの読み込み
    res = read_file('output/pokemon.txt', 'shift-jis')
    data = pd.DataFrame(res[1:], columns=res[0])
    # 他の比例係数に大きく関わる変数を削除する
    data = data.drop(columns=['against_bug', 'against_dark', 'against_dragon', 'against_electric',
                     'against_fairy', 'against_fight', 'against_fire', 'against_flying', 'against_ghost', 'against_grass', 'against_ground',
                              'against_ice', 'against_normal', 'against_poison', 'against_psychic', 'against_rock',
                              'against_steel', 'against_water','base_total'], axis=1)
    # 名義変数、もしくはそれに近い変数を削除する
    data = data.drop(columns=['abilities',
                     'classfication', 'name', 'japanese_name',
                              'generation', 'pokedex_number'], axis=1)
    data = data.drop(columns=[], axis=1)
    data = data.drop( columns=['type1'],axis=1)
    #data = pd.get_dummies(data, columns=['type1'])
    data = data[data.is_legendary == '0']
    data = data.drop(columns=['is_legendary'], axis=1)
    # 欠損値が含まれる行を削除
    data = data.dropna(axis=0).astype('float64')

    print(f"data:\n{data.head()}")
    # 主成分分析を行う
    pc_analyze(data, 'pokemon')
