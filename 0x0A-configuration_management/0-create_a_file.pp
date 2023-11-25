# Puppet manifest to create a file in /tmp

# Define the file resource
file { '/tmp/school':
  ensure  => 'file',       # Ensure that it is a regular file
  path    => '/tmp/school', # path
  mode    => '0744',        # Set file permissions to 0744
  owner   => 'www-data',    # Set file owner to www-data
  group   => 'www-data',    # Set file group to www-data
  content => 'I love Puppet',  # Set the content of the file
}

# End of Puppet manifest
