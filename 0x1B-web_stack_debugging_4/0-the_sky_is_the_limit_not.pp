# Puppet manifest to optimize Nginx web server and eliminate failed requests

# Install required packages
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx settings
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Define Nginx service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/nginx.conf'],
}

# Custom Nginx site configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default-site.erb'),
  notify  => Service['nginx'],
}

# Remove default Nginx default site configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => 'absent',
}

# Restart Nginx when configuration changes
exec { 'nginx-reload':
  command     => 'service nginx reload',
  refreshonly => true,
  subscribe   => [File['/etc/nginx/sites-available/default']],
  require     => Service['nginx'],
}
