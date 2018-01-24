exec { 'fix that file':
  cwd     => /var/www/html/
  command => sed -i 's/phpp/php/' wp-settings.php
}
