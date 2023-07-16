# cargo_fastapi

FastAPI + Tortoise ORM + PostgreSQL

Реализован эндпоинт для подсчета стоимости страховки на основании типа груза, даты и объявленной стоимости.

Для получения актуального тарифа для указанного груза реализована имитация внешнего сервиса.

Документация основного приложения доступна по адресу http://localhost:8080/docs.

Для имитационного сервиса тарифов -- по адресу http://localhost:8888/docs.

## Инструкции по запуску

Для запуска необходимо запустить команду
```
docker-compose up -d
```
