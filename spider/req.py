<<<<<<< HEAD
# import requests
#
# r = requests.get('https://www.baidu.com')
# print(r.text)

# import requests
# data = {
#     'name': 'gem',
#     'age': 25
# }
# r =requests.get('https://www.httpbin.org/get',params=data)
# print(type(r.text))
# print(r.json())

# 抓取网页
# import re
# import requests
# r =requests.get('https://ssr1.scrape.center/')
# pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)                   #正则表达式
# titles = re.findall(pattern,r.text)
# print(titles)
#
# #抓取内容
# import requests
# r = requests.get('https://portal-app-minio.nwpu.edu.cn/service/%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86-1632993348940.png')
# with open('favicon.png', 'wb') as f:
#     f.write(r.content)

# post
# import requests
#
#
# data = {'name': 'ayin','age':25}
# files = {'file': open('favicon.ico','rb')}
# r = requests.post('https://www.httpbin.org/post', data=data,files=files)
# print(r.text)

# cookie
import requests

cookie ='_octo=GH1.1.1616975558.1713404948; preferred_color_mode=light; tz=Etc%2FGMT-8; _device_id=535ed33d5f17402605ad68826350cfcd; has_recent_activity=1; saved_user_sessions=137845758%3ASu965HAxJLmg3N0v34CagWDtyoI0x5rlmuO17mDwZvN1sBMW; user_session=Su965HAxJLmg3N0v34CagWDtyoI0x5rlmuO17mDwZvN1sBMW; __Host-user_session_same_site=Su965HAxJLmg3N0v34CagWDtyoI0x5rlmuO17mDwZvN1sBMW; tz=Etc%2FGMT-8; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=yuzhou137; _gh_sess=9bZwV8ygnuSZy9U9ARc9MLNSEQgN3slaY055eoOOBp9KWz3dW253cmlrez2C5wkzG%2FKczsdiXdqOVe%2BB5HhAyV%2B9gs9NpMm7EPH9MUiHu5IBoDfEXlNijieGBJhSDGb28Wqp2nFBp3Z84JK7iGwCUEnfGp6RZAlFtQ9y4qLTZ%2B0AXb%2Blu1RS1HZC0B610gD8VrxySqSfA1RUgnrvZuoRuI4MCtYW8EYc7GJDrMZE0V2%2Bci3pcpTE7LG4JK1TLw4MExG7dj3z3HvuJOQAN6Jo98ceZpPecJ4BNj5Qo4Ec5z4XTmYPRh%2Bi8M3QPLyvAW9pmQpzD2R0SmpMPOlPncSyfkQIwufI2TX3jvkmj6eTCAEsOpmCK3UcEg%2F7OkgYO%2B94NCy7bpVj4dqu0A5C2AvlMhGdRJw8vg9joN1ZLM5xeMqLKQCiknZBge0g%2Be8Y2OyFZEmu9IW7fN19bqSmbToEbKSOeSeseu0ldW5VkEP35e0WF3%2Fe3FD5BjdwP2Cwoh1xWwuUwAexhSKx2uz2JsLFWXHN0x1rK873toStwEnGDgVZ79JCRd0CXjmRaAiKC%2FPsY9NSBx%2BKKc6IRSDHODC85jmGI3Cdg6W45k7vtC12IlxagBPlXZw1PqHR79XRiFW9K%2FTtww4y7x1lu60s7sAUlQr8wfaDPvfLYda2l1AWEDN%2FLFx%2F%2BAQRGfSZBy2qX74k%2FHh%2Fc2C0eXcr%2B9h7MM2O%2FnoNAJmHs5QfhdftP%2B70Fpzif8FDu06MQ%2BcTfS6Z5mhPfIQo7okLa9u3v5iLhzLUiffZbCQK6W53cN%2FQQaHe4Ryh%2BtQqwqJSDfeLmf58ayR5IJmDBOG0I%2FZlwdcDUGYdnsrdGvJv8BPDEsPHYbCR8%2FMjA9OJ0rYF2Eyb75cI%2BMnem12ZyPPM1AfFX8daWwfMKEXup8UI62ldys7J9AGPh6RHwlQdcMjPWxYLJPs72j1rarEXat0EvyOgs%2FA3TCMlvQR1047jerhgx6MCtjzq4WHh1tzUsuDpKh7QQMM4aWwShzSFDW57dfCcR4Wn%2BvyEG1EjjWkHAjzXthOo4ZJHydCYo%2FwSXqd4kcxGzXd7zEubOZ6emw%3D%3D--iofyI6qnmzmoVlHs--0Uxvdq1KIaSh1RfeGvw5wA%3D%3D'
cookie =cookie.split(';')
for c in cookie:
    print(c)
headers ={
    'Cookie':'_octo=GH1.1.1616975558.1713404948; preferred_color_mode=light; tz=Etc%2FGMT-8; _device_id=535ed33d5f17402605ad68826350cfcd; has_recent_activity=1; saved_user_sessions=137845758%3ASu965HAxJLmg3N0v34CagWDtyoI0x5rlmuO17mDwZvN1sBMW; user_session=Su965HAxJLmg3N0v34CagWDtyoI0x5rlmuO17mDwZvN1sBMW; __Host-user_session_same_site=Su965HAxJLmg3N0v34CagWDtyoI0x5rlmuO17mDwZvN1sBMW; tz=Etc%2FGMT-8; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=yuzhou137; _gh_sess=9bZwV8ygnuSZy9U9ARc9MLNSEQgN3slaY055eoOOBp9KWz3dW253cmlrez2C5wkzG%2FKczsdiXdqOVe%2BB5HhAyV%2B9gs9NpMm7EPH9MUiHu5IBoDfEXlNijieGBJhSDGb28Wqp2nFBp3Z84JK7iGwCUEnfGp6RZAlFtQ9y4qLTZ%2B0AXb%2Blu1RS1HZC0B610gD8VrxySqSfA1RUgnrvZuoRuI4MCtYW8EYc7GJDrMZE0V2%2Bci3pcpTE7LG4JK1TLw4MExG7dj3z3HvuJOQAN6Jo98ceZpPecJ4BNj5Qo4Ec5z4XTmYPRh%2Bi8M3QPLyvAW9pmQpzD2R0SmpMPOlPncSyfkQIwufI2TX3jvkmj6eTCAEsOpmCK3UcEg%2F7OkgYO%2B94NCy7bpVj4dqu0A5C2AvlMhGdRJw8vg9joN1ZLM5xeMqLKQCiknZBge0g%2Be8Y2OyFZEmu9IW7fN19bqSmbToEbKSOeSeseu0ldW5VkEP35e0WF3%2Fe3FD5BjdwP2Cwoh1xWwuUwAexhSKx2uz2JsLFWXHN0x1rK873toStwEnGDgVZ79JCRd0CXjmRaAiKC%2FPsY9NSBx%2BKKc6IRSDHODC85jmGI3Cdg6W45k7vtC12IlxagBPlXZw1PqHR79XRiFW9K%2FTtww4y7x1lu60s7sAUlQr8wfaDPvfLYda2l1AWEDN%2FLFx%2F%2BAQRGfSZBy2qX74k%2FHh%2Fc2C0eXcr%2B9h7MM2O%2FnoNAJmHs5QfhdftP%2B70Fpzif8FDu06MQ%2BcTfS6Z5mhPfIQo7okLa9u3v5iLhzLUiffZbCQK6W53cN%2FQQaHe4Ryh%2BtQqwqJSDfeLmf58ayR5IJmDBOG0I%2FZlwdcDUGYdnsrdGvJv8BPDEsPHYbCR8%2FMjA9OJ0rYF2Eyb75cI%2BMnem12ZyPPM1AfFX8daWwfMKEXup8UI62ldys7J9AGPh6RHwlQdcMjPWxYLJPs72j1rarEXat0EvyOgs%2FA3TCMlvQR1047jerhgx6MCtjzq4WHh1tzUsuDpKh7QQMM4aWwShzSFDW57dfCcR4Wn%2BvyEG1EjjWkHAjzXthOo4ZJHydCYo%2FwSXqd4kcxGzXd7zEubOZ6emw%3D%3D--iofyI6qnmzmoVlHs--0Uxvdq1KIaSh1RfeGvw5wA%3D%3D'
}
r = requests.get('https://github.com', headers=headers)
with open('recall.txt','wb') as f:
    f.write(r.content)
# print(r.text)

# session维持
=======
# import requests
#
# r = requests.get('https://www.baidu.com')
# print(r.text)

# import requests
# data = {
#     'name': 'gem',
#     'age': 25
# }
# r =requests.get('https://www.httpbin.org/get',params=data)
# print(type(r.text))
# print(r.json())

# 抓取网页
# import re
# import requests
# r =requests.get('https://ssr1.scrape.center/')
# pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)                   #正则表达式
# titles = re.findall(pattern,r.text)
# print(titles)
#
# #抓取内容
# import requests
# r = requests.get('https://portal-app-minio.nwpu.edu.cn/service/%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86-1632993348940.png')
# with open('favicon.png', 'wb') as f:
#     f.write(r.content)

# post
# import requests
#
#
# data = {'name': 'ayin','age':25}
# files = {'file': open('favicon.ico','rb')}
# r = requests.post('https://www.httpbin.org/post', data=data,files=files)
# print(r.text)

# cookie
import requests

cookie ='_octo=GH1.1.1616975558.1713404948; preferred_color_mode=light; tz=Etc%2FGMT-8; _device_id=535ed33d5f17402605ad68826350cfcd; has_recent_activity=1; saved_user_sessions=137845758%3ASu965HAxJLmg3N0v34CagWDtyoI0x5rlmuO17mDwZvN1sBMW; user_session=Su965HAxJLmg3N0v34CagWDtyoI0x5rlmuO17mDwZvN1sBMW; __Host-user_session_same_site=Su965HAxJLmg3N0v34CagWDtyoI0x5rlmuO17mDwZvN1sBMW; tz=Etc%2FGMT-8; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=yuzhou137; _gh_sess=9bZwV8ygnuSZy9U9ARc9MLNSEQgN3slaY055eoOOBp9KWz3dW253cmlrez2C5wkzG%2FKczsdiXdqOVe%2BB5HhAyV%2B9gs9NpMm7EPH9MUiHu5IBoDfEXlNijieGBJhSDGb28Wqp2nFBp3Z84JK7iGwCUEnfGp6RZAlFtQ9y4qLTZ%2B0AXb%2Blu1RS1HZC0B610gD8VrxySqSfA1RUgnrvZuoRuI4MCtYW8EYc7GJDrMZE0V2%2Bci3pcpTE7LG4JK1TLw4MExG7dj3z3HvuJOQAN6Jo98ceZpPecJ4BNj5Qo4Ec5z4XTmYPRh%2Bi8M3QPLyvAW9pmQpzD2R0SmpMPOlPncSyfkQIwufI2TX3jvkmj6eTCAEsOpmCK3UcEg%2F7OkgYO%2B94NCy7bpVj4dqu0A5C2AvlMhGdRJw8vg9joN1ZLM5xeMqLKQCiknZBge0g%2Be8Y2OyFZEmu9IW7fN19bqSmbToEbKSOeSeseu0ldW5VkEP35e0WF3%2Fe3FD5BjdwP2Cwoh1xWwuUwAexhSKx2uz2JsLFWXHN0x1rK873toStwEnGDgVZ79JCRd0CXjmRaAiKC%2FPsY9NSBx%2BKKc6IRSDHODC85jmGI3Cdg6W45k7vtC12IlxagBPlXZw1PqHR79XRiFW9K%2FTtww4y7x1lu60s7sAUlQr8wfaDPvfLYda2l1AWEDN%2FLFx%2F%2BAQRGfSZBy2qX74k%2FHh%2Fc2C0eXcr%2B9h7MM2O%2FnoNAJmHs5QfhdftP%2B70Fpzif8FDu06MQ%2BcTfS6Z5mhPfIQo7okLa9u3v5iLhzLUiffZbCQK6W53cN%2FQQaHe4Ryh%2BtQqwqJSDfeLmf58ayR5IJmDBOG0I%2FZlwdcDUGYdnsrdGvJv8BPDEsPHYbCR8%2FMjA9OJ0rYF2Eyb75cI%2BMnem12ZyPPM1AfFX8daWwfMKEXup8UI62ldys7J9AGPh6RHwlQdcMjPWxYLJPs72j1rarEXat0EvyOgs%2FA3TCMlvQR1047jerhgx6MCtjzq4WHh1tzUsuDpKh7QQMM4aWwShzSFDW57dfCcR4Wn%2BvyEG1EjjWkHAjzXthOo4ZJHydCYo%2FwSXqd4kcxGzXd7zEubOZ6emw%3D%3D--iofyI6qnmzmoVlHs--0Uxvdq1KIaSh1RfeGvw5wA%3D%3D'
cookie =cookie.split(';')
for c in cookie:
    print(c)
headers ={
    'Cookie':'_octo=GH1.1.1616975558.1713404948; preferred_color_mode=light; tz=Etc%2FGMT-8; _device_id=535ed33d5f17402605ad68826350cfcd; has_recent_activity=1; saved_user_sessions=137845758%3ASu965HAxJLmg3N0v34CagWDtyoI0x5rlmuO17mDwZvN1sBMW; user_session=Su965HAxJLmg3N0v34CagWDtyoI0x5rlmuO17mDwZvN1sBMW; __Host-user_session_same_site=Su965HAxJLmg3N0v34CagWDtyoI0x5rlmuO17mDwZvN1sBMW; tz=Etc%2FGMT-8; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=yuzhou137; _gh_sess=9bZwV8ygnuSZy9U9ARc9MLNSEQgN3slaY055eoOOBp9KWz3dW253cmlrez2C5wkzG%2FKczsdiXdqOVe%2BB5HhAyV%2B9gs9NpMm7EPH9MUiHu5IBoDfEXlNijieGBJhSDGb28Wqp2nFBp3Z84JK7iGwCUEnfGp6RZAlFtQ9y4qLTZ%2B0AXb%2Blu1RS1HZC0B610gD8VrxySqSfA1RUgnrvZuoRuI4MCtYW8EYc7GJDrMZE0V2%2Bci3pcpTE7LG4JK1TLw4MExG7dj3z3HvuJOQAN6Jo98ceZpPecJ4BNj5Qo4Ec5z4XTmYPRh%2Bi8M3QPLyvAW9pmQpzD2R0SmpMPOlPncSyfkQIwufI2TX3jvkmj6eTCAEsOpmCK3UcEg%2F7OkgYO%2B94NCy7bpVj4dqu0A5C2AvlMhGdRJw8vg9joN1ZLM5xeMqLKQCiknZBge0g%2Be8Y2OyFZEmu9IW7fN19bqSmbToEbKSOeSeseu0ldW5VkEP35e0WF3%2Fe3FD5BjdwP2Cwoh1xWwuUwAexhSKx2uz2JsLFWXHN0x1rK873toStwEnGDgVZ79JCRd0CXjmRaAiKC%2FPsY9NSBx%2BKKc6IRSDHODC85jmGI3Cdg6W45k7vtC12IlxagBPlXZw1PqHR79XRiFW9K%2FTtww4y7x1lu60s7sAUlQr8wfaDPvfLYda2l1AWEDN%2FLFx%2F%2BAQRGfSZBy2qX74k%2FHh%2Fc2C0eXcr%2B9h7MM2O%2FnoNAJmHs5QfhdftP%2B70Fpzif8FDu06MQ%2BcTfS6Z5mhPfIQo7okLa9u3v5iLhzLUiffZbCQK6W53cN%2FQQaHe4Ryh%2BtQqwqJSDfeLmf58ayR5IJmDBOG0I%2FZlwdcDUGYdnsrdGvJv8BPDEsPHYbCR8%2FMjA9OJ0rYF2Eyb75cI%2BMnem12ZyPPM1AfFX8daWwfMKEXup8UI62ldys7J9AGPh6RHwlQdcMjPWxYLJPs72j1rarEXat0EvyOgs%2FA3TCMlvQR1047jerhgx6MCtjzq4WHh1tzUsuDpKh7QQMM4aWwShzSFDW57dfCcR4Wn%2BvyEG1EjjWkHAjzXthOo4ZJHydCYo%2FwSXqd4kcxGzXd7zEubOZ6emw%3D%3D--iofyI6qnmzmoVlHs--0Uxvdq1KIaSh1RfeGvw5wA%3D%3D'
}
r = requests.get('https://github.com', headers=headers)
with open('recall.txt','wb') as f:
    f.write(r.content)
# print(r.text)

# session维持
>>>>>>> 57fe6b7a40858ab9697896513bc199f264a51c7f
