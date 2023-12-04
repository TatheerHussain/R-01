# worker_intelligence_ner
工人智慧 命名實體識別

隱私保護與醫學數據標準化競賽：解碼臨床病例、讓數據說故事
## 分數
|  User   | Rank  | 子任務 1：病患隱私資訊擷取 | 子任務 2：時間資訊正規化 | 
|  :---:  | :---: | :---------------------:  | :--------------------: |
| zhaorui|3.00 (1)| 0.8660 (5)                | 0.8685 (1) |





## 環境
* 作業系統：Windows 11 專業版 Insider Preview
* CPU：12th Gen Intel(R) Core(TM) i9-12900   2.40 GHz
* RAM : 32.0 GB
* 程式語言：Python 3.11.5
* 文字編輯器 : vscode 1.84.2


### python 函式庫
* pandas 2.0.3


# 使用說明

## 比賽輸出
### clone
```
git clone https://github.com/zhao-rui-NB/worker_intelligence_ner.git
cd worker_intelligence_ner
```

### 產生answer.txt
手動複製 opendid_test病例資料夾 到 worker_intelligence_ner\data\opendid_test
```
python main.py
```
可在.output取得answer.txt

## 小工具
### file_open 
    自動以VSCODE開啟該病例
* -f 檔案編號
* -i 開始位置索引

```
python tool/file_open.py -f 1097 -i 438
```





## ORGANIZATION 字典來源
### dict V2 : 
* https://www.50pros.com/fortune500
* https://www.sec.gov/files/rules/other/4-460list.htm

