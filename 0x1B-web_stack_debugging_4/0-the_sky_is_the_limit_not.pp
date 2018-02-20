# this puppet manifest fixes a throttled file limit
exec { 'fix etc-default-nginx':
  before  => Exec['restart nginx'],
  command => '/bin/sed -i "s/-n 15/-n 4096/g" /etc/default/nginx',
}
exec { 'restart nginx':
  command => '/etc/init.d/nginx restart',
}
