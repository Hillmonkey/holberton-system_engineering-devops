exec { 'fix that file':
  cwd     => '/var/www/html',
  command => '/bin/sed -i "s/phpp/php/g" wp-settings.php',
}

