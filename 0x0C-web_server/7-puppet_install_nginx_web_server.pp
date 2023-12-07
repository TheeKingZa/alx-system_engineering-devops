# 7-puppet_install_nginx_web_server.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "# Nginx default configuration\n
server {\n
    listen 80 default_server;\n
    listen [::]:80 default_server;\n\n
    root /var/www/html;\n
    index index.html index.htm index.nginx-debian.html;\n\n
    server_name _;\n\n
    location / {\n
        try_files \$uri \$uri/ =404;\n
        add_header X-Server-By \$hostname;\n
        return 200 'Hello World!';\n
    }\n\n
    # Redirect /redirect_me to a new location\n
    location /redirect_me {\n
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n
    }\n
}\n",
}

# Create a custom 404 page
file { '/usr/share/nginx/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default', '/usr/share/nginx/html/404.html'],
}
