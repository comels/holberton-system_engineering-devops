# Install puppet-lint
exec { 'install flask':
  command => 'sudo pip3 install flask==2.1.0',
  path    => '/usr/bin',
  }
