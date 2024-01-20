# Owlinals 索引

## 简介
owlinals 的初步索引工作是由社区驱动并由Alex完成的，我们爬取了12943条数据，并对数据进行清洗，按照区块高度排序，完成了初步任务。当前结果显示，有 9717 个 Owlinals 是在比特币区块高度为 826217(height<=826217) 前确认的，也就是说这些都是有效的，但是第 9718 至 10067 个 Owlinals 均处在 826218 区块中被确认，多余的 67 个NFT的合法性是无法保证的，因为这与 Owlinals 的官方页面服务器数据有关，社区没有任何数据，因此暂时不能决定。

简而言之：前 9717 个被确认的是没问题的，余下的 9718 至 10067 个需要探讨是通缩还是将多余的 67 个视为合法。

你可以在这个 [页面](https://github.com/OwlinalsDAO/index/blob/main/inscriptions.json) 搜索 id 或者铭文编号 number 查看你的 Owlinals 是否在 9717 个中。

你也可以下载数据 [output.csv](https://github.com/OwlinalsDAO/index/blob/main/output.csv) 来查看结果。 (每一页爬取的原始数据在 outputs.zip 中)

当然，你还可以自己动手爬取，所有代码已开源

## 使用

```
# 安装包文件
pip install -r requirements.txt

# 收集数据
python3 main.py

# 情绪数据
python3 clean.py

# 最后请你打开表格按照区块高度升序排序
```

## 数据来源

数据来自创始人在 Discord Announcement 中他提供的所有统计数据（注意这是乱序的，Magic Eden上也有不合法的，创始人之前是一个个手动索引，并没有先排序后索引）

- 链接：https://geniidata.com/user/daveed/owlinals

  <img width="819" alt="image" src="https://github.com/OwlinalsDAO/index/assets/157193953/1bc39153-22da-4c13-80e0-2f969c5063b1">

- 接口：https://www.geniidata.com/api/dashboard/chart/public/data?chartId=276771&pageSize=100&page={page}&searchKey=&searchValue=

## 请我喝杯咖啡吧
目前我已将索引提供给OKX，等待合并，在购买时请看清区块高度！
如果您觉得我的工作对社区有帮助，请我喝杯咖啡吧～

ERC20: 0xEfCa8f001dBe23B872e7ca1584421d53b915ae29, Thanks!

<img width="312" alt="image" src="https://github.com/OwlinalsDAO/index/assets/157193953/39f034c4-c656-4883-bc8e-de68ad72284d">
