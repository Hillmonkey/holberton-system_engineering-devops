# this puppet manifest fixes throttled file limit for user holbertion
exec { 'fix limits.conf hard':
  command => 'sed -i "s/hard nofile 5/rd nofile 1024/g" limits.conf',
  path    => '/bin/',
  cwd     => '/etc/security/',
}
exec { 'fix limits.conf soft':
  command => 'sed -i "s/soft nofile 4/ft nofile 1023/g" limits.conf',
  path    => '/bin/',
  cwd     => '/etc/security/',
}
