# Puppet manifest to configure OS settings for the holberton user

# Ensure holberton user exists
user { 'holberton':
  ensure => 'present',
}

# Allow holberton user to login
file_line { 'allow_holberton_login':
  path  => '/etc/ssh/sshd_config',
  line  => 'AllowUsers holberton',
  match => '^#?AllowUsers',
}

# Set higher file descriptor limit for holberton user
file_line { 'increase_file_limit':
  path  => '/etc/security/limits.conf',
  line  => 'holberton hard nofile 4096',
  match => '^#?holberton hard nofile',
}

# Notify SSH service to reload configuration
service { 'ssh':
  ensure  => 'running',
  enable  => true,
  require => File_line['allow_holberton_login'],
  subscribe => File_line['increase_file_limit'],
}
