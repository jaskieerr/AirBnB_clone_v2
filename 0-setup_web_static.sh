#!/usr/bin/env bash
# setting up your web servers for the deployment of web_static


sudo apt-get update -y
sudo apt-get install nginx -y


sudo mkdir -p /data/ /data/web_static/ /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/

# Create a HTML file for testing purposes
sudo echo '
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="keywords" content="ALX, Web Server, AirBnB Clone, HTML, CSS, JavaScript">
        <meta name="author" content="Abdulqudus Oladega">
        <title>Test Page</title>
    </head>

    <body>
        <header>
            <h1>quick testu</h1>
        </header>

    </body>

</html>
'| sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '41i\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
