module { 'puppetlabs/stdlib':
  ensure   => installed,
}

file { '/tmp/eureka.txt':
  ensure => present,
}->
file_line { 'Append a line to /tmp/eureka.txt':
  path => '/tmp/eureka.txt',
  line => 'Hello Eureka',
  match   => "^Hello.*$",
}
