#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CSVファイルを読み込んで、Markdown形式のテーブルを作成するスクリプト
# 使い方: python make_md.py input.csv output.md

import os
import sys
import csv
import pandas as pd

# サムネイルがdefaultで表示されないもののテーブル
thumbnail_table = {"hjSZKHpnY6c": "hqdefault.jpg", "ZjKDKxntinU": "hqdefault.jpg",
                   "FM4JtbphU8o": "hqdefault.jpg", "zNbheLU69hs": "hqdefault.jpg",
                   "gkpM0sJSATk": "hqdefault.jpg", "gJwgKTxg5zU": "hqdefault.jpg",
                   "O3Bs7Cx98qU": "hqdefault.jpg", "dCs-1DzbgCw": "hqdefault.jpg"
                   }

def make_md(input_file, output_file):

    output_text = ""
    
    song_name = ""

    # pandasでCSVファイルを読み込む
    df = pd.read_csv(input_file)

    for index, row in df.iterrows():
        song = row['song']
        id = row['id']

        if song_name != song:
            song_name = song
            output_text += f"\n\n## {song_name}\n"

        # id 例: A-VhqqHnEKk&t=85s の場合は、A-VhqqHnEKk とする (&t=85s は除く)
        thumbnail_id = id.split("&")[0]

        # JPG = "maxresdefault.jpg"
        # JPG = "sddefault.jpg"
        # JPG = "hqdefault.jpg"
        # JPG = "mqdefault.jpg"
        # JPG = "default.jpg"

        if thumbnail_id in thumbnail_table:
            JPG = thumbnail_table[thumbnail_id]
        else:
            JPG = "maxresdefault.jpg"
        
        output_text += f"[<img width=\"240\" src=\"https://img.youtube.com/vi/{thumbnail_id}/{JPG}\">](https://www.youtube.com/watch?v={id})\n"
        # FIXME: 別ATBで開く。下のではダメ
        # output_text += f"[<img width=\"240\" src=\"https://img.youtube.com/vi/{thumbnail_id}/{JPG}\">](https://www.youtube.com/watch?v={id} \"target='_blank'\")\n"

    output_text += "\n"

    # print(output_text)

    # ファイルに書き込む
    with open(output_file, 'w', encoding="utf-8") as f:
        f.write(output_text)

    print(f"write {output_file}")
    

if __name__ == "__main__":

    # 引数の数が適切でない場合はエラーを表示して終了
    if len(sys.argv) != 2:
        print("Usage: python make_README.py dir_name")
        sys.exit(1)
    else:
        dir_name = sys.argv[1]

    if not os.path.exists(dir_name):
        print(f"No directory: {dir_name}")
        sys.exit(1)
        
    in_file = os.path.join(dir_name, f"{dir_name}.csv")
    out_file = os.path.join(dir_name, "README.md")

    make_md(in_file, out_file)

# import pdb; pdb.set_trace()

### Local Variables: ###
### truncate-lines:t ###
### End: ###
