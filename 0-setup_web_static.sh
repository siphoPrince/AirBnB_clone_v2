#!/usr/bin/env bash
# Script that sets up web servers for the deployment of web_static

# Update package list
sudo apt-get update

# Install Nginx
sudo apt-get -y install nginx

# Allow HTTP traffic through UFW
sudo ufw allow 'Nginx HTTP'

# Create directory structure for web_static
sudo mkdir -p /data/web_static/{releases/test,shared,current}

# Create index.html in test release
sudo tee /data/web_static/releases/test/index.html > /dev/null <<EOL
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOL

# Create symbolic link to the test release
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Set ownership to the ubuntu user
sudo chown -R ubuntu:ubuntu /data/

# Add alias to Nginx configuration
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx
sudo service nginx restart
