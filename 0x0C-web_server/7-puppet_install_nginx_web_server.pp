# File: 7-puppet_install_nginx_web_server.pp
class nginx_web_server {
  # Update package list
  package { 'nginx':
    ensure => latest,
  }

  # Create a default HTML file with "Hello World!"
  file { '/var/www/html/index.html':
    ensure  => present,
    content => 'Hello World!',
  }

  # Configure Nginx to use the custom HTML file
  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => template('nginx/default.erb'),
    require => Package['nginx'],
  }

  # Enable Nginx site
  exec { 'enable_nginx_site':
    command => 'ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/',
    path    => ['/bin', '/usr/bin'],
    creates => '/etc/nginx/sites-enabled/default',
    require => File['/etc/nginx/sites-available/default'],
  }

  # Configure 301 redirect
  nginx::resource::location { '/redirect_me':
    ensure    => present,
    location  => '/new_location',
    vhost     => 'default',
    port      => 80,
    ssl       => false,
    server    => 'localhost',
    proxy     => 'http://localhost/new_location',
    ssl_proxy => false,
  }

  # Notify Nginx to reload after changes
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Exec['enable_nginx_site'],
    notify  => Exec['nginx_reload'],
  }

  # Reload Nginx after configuration changes
  exec { 'nginx_reload':
    command => 'systemctl reload nginx',
    path    => ['/bin', '/usr/bin'],
    refreshonly => true,
  }
}

include nginx_web_server
