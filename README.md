# FastAPI 農務提醒 API 練習原型

此 Repository 保存一個早期 FastAPI + SQLAlchemy API 練習，資料模型包含洋蔥栽植提醒與預警報。它與後續的 `RemindApi` 專案主題相近，應視為早期練習紀錄，不應與後續版本重複計算為獨立產品。

## 技術

- Python
- FastAPI
- SQLAlchemy ORM
- SQLite
- Pydantic
- CORS middleware

## 程式內容

- 以 ORM model 表示栽植提醒與預警報。
- 以 SQLite 作為資料庫。
- 提供讀取與新增提醒資料的 API 路由。
- 使用 CRUD functions 將 API 操作與 ORM 資料存取分開。

## 程式現況

目前程式包含數個明確的命名及呼叫不一致問題，例如 metadata 屬性拼寫錯誤、栽植提醒 POST route 呼叫錯誤的 CRUD function，以及 Pydantic Config 命名不符合預期。此 Repository 應定位為學習階段原型，不能宣稱目前可直接啟動。

後續相關作品：[RemindApi](https://github.com/Kouichi1229/RemindApi)
