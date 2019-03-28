# -*- coding:utf-8 -*-


def pickup_overlap_list(firstlist, secondlist):
    """
    2つのリストから、重複要素を検出し、
    同じ要素のリスト、同じ要素を省いたリストを作成する

    Parameters
    -------
    firstlist : list
        比較リスト１
    secondlist : list
        比較リスト２

    Returns
    -------
    overlaplist : list
        重複要素のリスト
    fistlist : list
        重複要素を省いた比較リス１
    secondlist : list
        重複要素を省いた比較リスト２
    """
    overlaplist = []
    # 2つのリスト内で同じ要素を検出
    for first, second in product(firstlist, secondlist):
        if first.compare(second):
            # 同じ要素を抽出する
            overlaplist.append(first)
            firstlist.remove(first)
            secondlist.remove(second)
    return overlaplist, firstlist, secondlist
