# Puppet manifest to kill a process named killmenow

# Define the exec resource to run the pkill command
exec { 'killmenow':
  command     => 'pkill -f killmenow',  # The pkill command to terminate the process
  path        => '/usr/bin:/bin',       # Set the path for the command
  refreshonly => true,                   # Only run the command if notified
}

# End of Puppet manifest
