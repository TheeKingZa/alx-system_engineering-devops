#!/usr/bin/env ruby
# Checks if Command-line argument matches the regular expression /School/

if ARGV[0] =~ /Holberton/
  puts ARGV[0]
end
