# 0-strace_is_your_friend.pp
# Fixes a file

# Executing a shell command to replace occurrences
# of ".phpp" with ".php" in the wp-settings.php file
exec {'replaces wrong php filetype':
  command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/',
  # Specify the path for the shell command
  onlyif  => 'test -f /var/www/html/wp-settings.php'
  # Execute only if the file exists
}
