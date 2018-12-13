## How to crack GitAhead.
---
This doc will tell you how to make a license server for GitAhead to use the Commercial features .
And I will give some operations under CentOS 7 env.
This server will use : ngnix+uwsgi+flask
## Need components 
### Nginx web server 
	1. install nginx 
```
# yum install epel-release
# yum install nginx 
```
	2. create ssl certs for https 
```
# cd /etc/nginx/
# openssl genrsa -des3 -out server.key 2048 
# openssl req -new -key server.key -out server.csr
# cp server.key server.key.org
# openssl rsa -in server.key.org -out server.key
# openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```
	3. config nginx 
The needed configure license server in nginx.conf, you can create a file gitahead.conf in nginx conf dir ,such as /etc/nginx/conf.d/
and write the fellowing content in it, this confiration will enable SSL feature . 
```
server {
    listen       443;
    server_name  localhost;

    ssl          on;
    ssl_certificate      /etc/nginx/server.crt;
    ssl_certificate_key  /etc/nginx/server.key;
    keepalive_timeout    70;

    access_log  /var/log/nginx/host.access.log  main;

    location / {
        include        uwsgi_params;
        uwsgi_pass     127.0.0.1:8001;
    }

    #error_page  404              /404.html;

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

}
```
### 2, uwsgi 

	1. install flask & python 
```
yum install -y python-devel
pip install flask 
```
	2. install uwsgin 
```
pip install uwsgi
```
	3. deploy the server code 
```
mkdir -p  /var/licserver
```
copy the code to the dir . 
	4. config uswgi in uwsgi.ini
```
[uwsgi]
module = wsgi:app
socket = 127.0.0.1:8001
# processor num
processes = 5

```

## Run the server 
	1. start nginx 
```
#	systemctl start nginx 
```
	2. start uswgi 
```
uwsgi -d --ini uwsgi.ini
```


## Redirect the host to server IP addr by change windows C:\Windows\System32\drivers\etc\hosts
```
	<ip addres>  helios.scitools.com
```