#!/usr/bin/env bash
# Install nginx if not already installed
if [ ! -x "$(command -v nginx)" ]; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create fake HTML file
sudo echo "Hello World" > /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update nginx configuration
sudo sed -i '/^http {/a \    server {\n        listen 80 default_server;\n        listen [::]:80 default_server;\n        location /hbnb_static {\n            alias /data/web_static/current/;\n        }\n    }' /etc/nginx/nginx.conf

# Restart nginx
sudo service nginx restart

exit 0
