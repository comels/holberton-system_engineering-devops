# Upgrade requests

exec { 'change_default':
  command => 'sed -i s/15/2000/ /etc/default/nginx',
  path    =>  [ '/bin/', '/usr/sbin/' ]
} ->

exec { 'restart':
  command => 'sudo service nginx restart',
  path    =>  [ '/bin/', '/usr/sbin/' ]
}