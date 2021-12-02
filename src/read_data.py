"""
データファイルを読み込む
"""


def split_tab(data):
    """
    文字列をタブ区切りに分割する
    """
    return data.split('\t')


def read_file(file, encoding):
    """
    ファイルを読み込む

    Parameters
    ----------
    file : str
        読み込むファイル
    encoding : str
        ファイルのエンコーディング

    Returns
    -------
    data : [[str]]
        読み込んだデータの二次元配列
    """
    # baseball.txtでは、shift-jisでもデコードエラーがでされたため、UTF-8で読み込む
    with open(file, 'r', encoding=encoding) as file_obj:
        data = file_obj.read()
        data = list(map(split_tab, data.split("\n")))
    return data
