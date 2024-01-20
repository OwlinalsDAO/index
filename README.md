# Owlinals Indexer

## Introduction

The preliminary indexing work of owlinals was driven by the community and completed by Alex. We crawled 12943 pieces of data, cleaned the data, sorted it according to block height, and completed the preliminary task. The current results show that 9717 Owlinals were confirmed before the Bitcoin block height was `826217` (height<=826217). These are all valid, but the 9718th to 10067th Owlinals are all in the 826218 block, which is redundant. The legality of the 67 NFTs cannot be guaranteed because it is related to the official page server data of Owlinals. The community does not have any data, so it cannot be decided for the time being.

## Instructions

```
# install
pip install -r requirements.txt

# collect data
python3 main.py

# clean data
python3 clean.py
```

