## Инструкция по установке
```
Создать .env file

POSTGRES_USER={}
POSTGRTES_PASSWORD={}
POSTGRES_DATABASE={}
SECRET_KEY={}
```
```
sudo docker-compose up -d --build
```

## Создание суперюзера
```
docker exec -it {container_id} python manage.py createsuperuser
```

## Основные методы

### GET city/
Получение списка городов


### GET city/{city_id}/street/
Получение списка улиц относящихся к указанному городу


### POST shop/
    {
        "name": "vkusvill",
        "city": "1",
        "street": "2",
        "address_number": "13a",
        "open_time": "16:00",
        "closing_time": "03:00:PM"
    }
Создание нового магазина


### GET /shop/?street=&city=&open=0/1
Получение списка магазинов. Фильтры необязательны