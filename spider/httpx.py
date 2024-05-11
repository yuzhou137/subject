# 这玩意玩不了啊
import httpx

response = httpx.get('https://www.httpbon.org/get')
print(response.text)