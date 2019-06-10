## tt-api Lista de request de prueba

Comando para ejecutar en modo debug el servidor:

```
FLASK_APP=app.py flask run
```

### Comunidades energéticas creación, modificación, consulta y eliminación

curl -X GET \
  http://127.0.0.1:5000/communities \
  -H 'Postman-Token: 3a6117a3-1652-44f5-b458-1ede2efd366a' \
  -H 'cache-control: no-cache'

curl -X POST \
  http://127.0.0.1:5000/communities \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: ee3abd11-dabe-4798-9ebe-b5736b0702c0' \
  -H 'cache-control: no-cache' \
  -d '{
"name": "test1",
"description": "test",
"latitude": 2111,
"longitude": 2111,
"gestorId": 123
}'

curl -X PUT \
  http://127.0.0.1:5000/communities/test1 \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 520d0522-a205-4971-a3f3-ab7bbf10267e' \
  -H 'cache-control: no-cache' \
  -d '{
"description": "test1",
"latitude": 2111,
"longitude": 2111,
"gestorId": 123
}'

curl -X DELETE \
  http://127.0.0.1:5000/communities/test1 \
  -H 'Postman-Token: e94461ce-3825-413d-9b58-479b7c3f4be2' \
  -H 'cache-control: no-cache'

### Inscripción

curl -X GET \
  http://127.0.0.1:5000/members \
  -H 'Postman-Token: ac671268-3df9-405c-b339-a3d201af66c4' \
  -H 'cache-control: no-cache'

curl -X POST \
  http://127.0.0.1:5000/members \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 1d945e07-c7e0-4a8c-8508-51be79a40f03' \
  -H 'cache-control: no-cache' \
  -d '{
	"memberId": "2",
	"name": "Lothar",
	"surname": "Soto",
	"derLatitude": 2111,
	"derLongitude": 2111,
	"derName": "DerTest"
}'