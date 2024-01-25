# Fix problem of high amount of requests

# Executing a shell command to replace the ulimit configuration in /etc/default/nginx
exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],  # Ensure this is executed before the restart
}

# Executing a shell command to restart the Nginx service
exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
