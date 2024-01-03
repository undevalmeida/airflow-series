import requests
import json
payload_json = {
    "description": "testando o uso de api para criar variáveis",
    "key": "pumblers",
    "value": json.dumps({
        
        "nome": "André",
        "idade": "23"
    
    }, ensure_ascii=False) # para aceitar acento
}

auth = {
    "admin": "admin"
}

response = requests.post(
    url='http://localhost:8080/api/v1/variables',
    json=payload_json,
    auth=('admin', 'admin')
)

print(response.json())

response.json()
