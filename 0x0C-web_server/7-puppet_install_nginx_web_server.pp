# 7-puppet_install_nginx_web_server.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '# Nginx configuration file\nserver {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\n\troot /var/www/html;\n\tindex index.html index.htm index.nginx-debian.html;\n\n\tserver_name _;\n\n\tlocation / {\n\t\ttry_files  / =404;\n\t}\n\n\tlocation /redirect_me {\n\t\treturn 301 http://example.com;\n\t}\n\n\tlocation ~ \.php$ {\n\t\tinclude snippets/fastcgi-php.conf;\n\t\tfastcgi_pass unix:/var/run/php/php7.4-fpm.sock;\n\t\tfastcgi_param SCRIPT_FILENAME ;\n\t\tinclude fastcgi_params;\n\t}\n}\n',
  require => Package['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => File['/etc/nginx/sites-available/default'],
}

# Create Hello World index.html
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}
