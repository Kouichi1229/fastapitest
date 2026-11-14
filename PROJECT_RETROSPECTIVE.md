# 技術回顧｜FastAPI 農務提醒 API 練習原型

## 專案定位

這是較早期的 FastAPI、SQLAlchemy 與 SQLite 練習，嘗試建立洋蔥栽植提醒及預警報的 API。後續有主題相近的 `RemindApi` Repository，因此本專案應作為早期學習版本記錄，不重複計算為獨立產品。

## 可由程式確認的實作

- 使用 FastAPI 建立 API application。
- 使用 SQLAlchemy declarative models 定義 PlantMsg 與 AlerMsg。
- 使用 SQLite engine 與 SQLAlchemy session。
- 以 CRUD functions 封裝資料查詢與新增。
- 使用 Pydantic model 描述提醒資料欄位。
- 設定 CORS middleware。
- 讀取 endpoints 使用 `skip`、`limit` 參數。

## 路由概念

- `GET /Remind/plant)：取得栽植提醒。
- `GET /Remind/aler`：取得預警報。
- `POST /Remind/plant)：預期新增栽植提醒。
- `POST /Remind/aler`：預期新增預警報。

以上是路由意圖的描述；目前程式存在呼叫錯誤，不能據此認定 POST 路由已正常工作。

## 技術能力紀錄

- Python
- FastAPI routing / dependency injection
- SQLAlchemy ORM
- SQLite
- Pydantic schemas
- CRUD separation
- CORS configuration

## 靜態檢視發現

1. `main.py` 使用 `models.Base.metadate.create_all`，`metadate` 拼寫錯誤，應為 `metadata`；這會影響應用啟動時建立資料表。
2. `POST /Remind/plant` 將 `plantMsg` 傳入 `crud.create_AlerMsg`，函式簽章與資料模型不相符。
3. `POST /Remind/aler` 也呼叫 `create_AlerMsg`；雖然與預警報 CRUD 函式名稱相符，但其 schema/model 欄位需再確認。
4. `schemas.py` 使用小寫 `class config`，而 Pydantic v1 ORM 設定慣例為 `class Config`；依使用版本不同，ORM serialization 設定可能不生效。
5. `schemas.py` 包含直接寫在原始碼中的示例提醒文字，這些是範例資料，不應視為資料庫中實際部署的內容。
6. 沒有看到完整測試或部署驗證紀錄。

## 與後續作品的關係

`RemindApi` 是同一應用主題的後續 Repository。整理作品集時，建議以後續版本作為主要專案，將本 Repository 當作 API / ORM 學習歷程的補充材料。

## 驗證範圍

本回顧依原始碼進行靜態檢視，沒有執行伺服器或資料庫測試，不宣稱目前可啟動或 API 路由可正常使用。
