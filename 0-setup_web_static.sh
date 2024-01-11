#!/usr/bin/env bash
#  Prepare your web servers

trap 'exit 0' ERR

if ! command -v nginx &> /dev/null; then
    sudo apt update
    sudo apt install nginx -y
fi

sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir -p "/data/web_static/shared/"

body="Holberton School"
index_content="<html>
  <head></head>
  <body>$body</body>
</html>"

echo "$index_content" | sudo tee "/data/web_static/releases/test/index.html" > /dev/null

rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR loubna:loubna "/data/"

sudo wget -q -O /etc/nginx/sites-available/default http://exampleconfig.com/static/raw/nginx/ubuntu20.04/etc/nginx/sites-available/default
config="/etc/nginx/sites-available/default"

sudo cp "$config" "$config.bak"

if [ ! -e "$config" ]; then
    sudo wget -q -O "$config" http://exampleconfig.com/static/raw/nginx/ubuntu20.04/etc/nginx/sites-available/default
fi

sudo sed -i '/^}$/i \ \n\tlocation \/redirect_me {return 301 https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4;}' $config
sudo sed -i '/^}$/i \ \n\tlocation @404 {return 404 "Ceci n'\''est pas une page\\n";}' $config
sudo sed -i 's/=404/@404/g' $config
sudo sed -i "/^server {/a \ \tadd_header X-Served-By $HOSTNAME;" $config
sudo sed -i '/^server {/a \ \n\tlocation \/hbnb_static {alias /data/web_static/current/;index index.html;}' $config
sudo service nginx restart
