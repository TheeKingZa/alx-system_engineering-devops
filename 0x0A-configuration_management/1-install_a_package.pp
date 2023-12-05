# 1-install_a_package.pp

# Install a specific version of Werkzeug first
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
}

# Define a package resource for Flask
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
}

# Notify to refresh the shell after the packages are installed
notify { 'Refresh Shell':
  subscribe => [Package['Flask'], Package['Werkzeug']],
}
