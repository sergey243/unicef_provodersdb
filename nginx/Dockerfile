FROM nginx:latest
# Adding config files
RUN mkdir -p /etc/certs
COPY nginx/conf.d/certs/ /etc/certs/
COPY nginx/conf.d/proxy.conf /etc/nginx/proxy.conf
COPY nginx/conf.d/fastcgi.conf /etc/nginx/fastcgi.conf
COPY nginx/conf.d/mime.types /etc/nginx/conf/mime.types
COPY  nginx/conf.d/nginx.conf /etc/nginx/nginx.conf
#COPY  nginx/sites-available/pgadmin.conf /etc/nginx/sites-available/pgadmin.conf
#COPY  nginx/sites-available/scrapyd.conf /etc/nginx/sites-available/scrapyd.conf
#COPY  nginx/sites-available/scanner.conf /etc/nginx/sites-available/scanner.conf

RUN mkdir -p /etc/nginx/sites-enabled
RUN  ln -s /etc/nginx/sites-available/scanner.conf /etc/nginx/sites-enabled/scanner.conf
#RUN  ln -s /etc/nginx/sites-available/pgadmin.conf /etc/nginx/sites-enabled/pgadmin.conf
#RUN  ln -s /etc/nginx/sites-available/scrapyd.conf /etc/nginx/sites-enabled/scrapyd.conf

# Install csudo apt update
#RUN apt install snapd
#certbot
#RUN install core; sudo snap refresh core
#RUN snap install --classic certbot
#RUN ln -s /snap/bin/certbot /usr/bin/certbot
RUN apt-get update
#RUN apt install python-certbot-apache -y

# Copy renew cron script
RUN apt install -y cron
COPY nginx/renew /etc/periodic/daily/renew
RUN chmod +x /etc/periodic/daily/renew

RUN mkdir /var/lib/certbot

# Copy entrypoint
COPY nginx/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# nginx config
#COPY nginx/conf.d/nginx.conf /etc/nginx/nginx.conf

# Something to serve
RUN mkdir /var/lib/website
COPY nginx/index.html /var/lib/website/

ENTRYPOINT [ "./entrypoint.sh" ]