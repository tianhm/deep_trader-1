# Deep Trader

# 構成

## データ収集部

学習用の時系列データを取得する

## 学習部

### 教師あり学習

時系列データを元に予想する．
予想を元にルールベースの操作を行う．

### 教師なし学習

DQNを用いて利益を最大化するような方策込の学習を行う

## 操作部

実際に売買を行う．
スクレイピング？　画像処理？

## バッグランドテスト環境

本番投入前にテスト環境

## Install

```
git clone git@tkg.pgw.jp:fintech/deep_trader.git
cd deep_trader
docker-compose up
```
