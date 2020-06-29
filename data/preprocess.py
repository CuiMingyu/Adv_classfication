# -*- coding: utf-8 -*-
import pandas as pd

def convert_txt_to_csv(data_path):
    with open(data_path) as f:
        data = f.readlines()
    orig = [data[i].split("\t")[1].strip() for i in range(0, len(data), 3)]
    adv = [data[i+1].split("\t")[1].strip() for i in range(0,len(data), 3)]
    assert len(orig) == len(adv)

    original_df = pd.read_csv("data/TaskA/train.csv")
    print(len(original_df), len(orig))
    for _, row in original_df.iterrows():
        sent0, sent1, label = row["sent0"], row["sent1"], row["label"]
        # print(sent0, sent1, label)
    

if __name__ == "__main__":
    data_path = "data/adversaries.txt"
    convert_txt_to_csv(data_path)