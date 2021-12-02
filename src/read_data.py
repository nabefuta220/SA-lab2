"""
データファイルを読み込む
"""


def split_tab(str):
    """
    文字列をタブ区切りに分割する
    """
    return str.split('\t')


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
        str = file_obj.read()
        str = list(map(split_tab, str.split("\n")))
    return str
