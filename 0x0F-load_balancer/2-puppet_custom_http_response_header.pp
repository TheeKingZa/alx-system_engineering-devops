# 2-puppet_custom_http_response_header.pp

# Install Nginx
class { 'nginx':
  ensure => 'installed',
}

# Define custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    # Other configuration settings...

    location / {
      add_header X-Served-By ;
      # Other location settings...
    }

    # Other server settings...
}",
  notify  => Service['nginx'],
}

# Enable the site
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

# Restart Nginx after making changes
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
