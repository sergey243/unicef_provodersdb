#!/bin/sh

# Get certs
#certbot certonly -n -d .local \
#  --standalone --preferred-challenges http --email sergeyassu@gmail.com --agree-tos --expand

# Kick off cron
#service cron  start
#crond -f -d 8 &

# Test nginx

nginx -t
service nginx restart
# Start nginx
nginx -g "daemon off;"
service nginx status
# Check nginx status
