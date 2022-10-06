# Upgrade limit requests

exec { 'ulimit':
  command => 'sed -i s/15/2000/ /etc/default/nginx',
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
} ->

exec { 'restart':
  command => 'sudo service nginx restart',
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}