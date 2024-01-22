# Owlinals Indexer

## Language

- [中文](readme/README.zh_CN.md)

## Introduction

The preliminary indexing work of owlinals was driven by the community and completed by Alex. We crawled 12943 pieces of data, cleaned the data, sorted it according to block height, and completed the preliminary task. The current results show that 9717 Owlinals were confirmed before the Bitcoin block height was `826217` (height<=826217). These are all valid, but the 9718th to 10067th Owlinals are all in the 826218 block, which may be redundant.Currently, the founder has indexed 10,067 Owlinals, but the community has currently indexed 10,000 Owlinals based on block height and inscription number, and the remaining 67 have not yet been indexed.

You can check your owlinals through this [page](https://github.com/OwlinalsDAO/index/blob/main/inscriptions.json) by search `id` or `number`.

You can download this [output.csv](https://github.com/OwlinalsDAO/index/blob/main/output.csv) to see the result. (raw data of each page is in outputs.zip)

Or 

You can get the data by the following instructions.

## Instructions

```
# install
pip install -r requirements.txt

# collect data
python3 main.py

# clean data
python3 clean.py
```

## Data source

- URL：https://geniidata.com/user/daveed/owlinals (This is the data created by the founder and he wants to crawl, he said in discord.)

  <img width="819" alt="image" src="https://github.com/OwlinalsDAO/index/assets/157193953/1bc39153-22da-4c13-80e0-2f969c5063b1">


- Interface：https://www.geniidata.com/api/dashboard/chart/public/data?chartId=276771&pageSize=100&page={page}&searchKey=&searchValue=

## Contribute me a Coffee

ERC20: 0xEfCa8f001dBe23B872e7ca1584421d53b915ae29, Thanks!

<img width="312" alt="image" src="https://github.com/OwlinalsDAO/index/assets/157193953/39f034c4-c656-4883-bc8e-de68ad72284d">

