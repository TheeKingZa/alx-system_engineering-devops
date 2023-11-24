# Puppet manifest to install Flask from pip3

# Define the package resource for Flask
package { 'Flask':
  ensure   => '2.1.0',  # Ensure the specific version 2.1.0 is installed
  provider => 'pip3',   # Use pip3 as the package provider
  require  => Package['python3-pip'],  # Ensure python3-pip is installed first
}

# End of Puppet manifest
