# Лабораторная 1

```
curl --head www.youtube.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 301 Moved Permanently
Content-Type: application/binary
X-Content-Type-Options: nosniff
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Pragma: no-cache
Expires: Mon, 01 Jan 1990 00:00:00 GMT
Date: Tue, 12 Sep 2023 17:57:42 GMT
Location: https://www.youtube.com/
Content-Length: 0
Server: ESF
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
```

**Content-Type** - заголовок, который используется для указания исходного мультимедиа ресурса


**X-Content-Type-Options** - это маркер, используемый сервером для указания того, что типы MIME, объявленные в заголовках Content-Type, следует соблюдать и не изменять


**Cache-Control** - содержит директивы — как в запросах, так и в ответах — которые управляют кешированием в браузерах и общих кешах


**Pragma** - это заголовок, зависящий от реализации, который может иметь различные эффекты в цепочке запрос-ответ.  Этот заголовок служит для обратной совместимости с кэшами HTTP/1.0, у которых нет заголовка Cache-Control HTTP/1.1.


**Expires** - содержит дату/время, после которого ответ считается просроченным.


**Date** - заголовок содержит дату и время создания сообщения.


**Location** -  указывает URL-адрес, на который нужно перенаправить страницу. 


**Content-Length** -  указывает размер тела сообщения в байтах, отправляемого получателю


**Server** - описывает программное обеспечение, используемое исходным сервером, который обработал запрос, то есть сервером, сгенерировавшим ответ


**X-XSS-Protection** - это функция Internet Explorer, Chrome и Safari, которая останавливает загрузку страниц при обнаружении отраженных атак с использованием межсайтовых сценариев


**X-Frame-Options** - можно использовать, чтобы указать, разрешено ли браузеру отображать страницу в `frame`, `iframe`, `embed` или `object`.