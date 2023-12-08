# 101-setup_web_static.pp

# Install Nginx
package { 'nginx':
  ensure => 'installed',
}

# Allow Nginx HTTP through UFW
class { 'ufw':
  before => Package['nginx'],
}

ufw::allow { 'Nginx HTTP':
  port => 80,
}

# Create directories
file { '/data/':
  ensure => 'directory',
}

file { [
  '/data/web_static/',
  '/data/web_static/releases/',
  '/data/web_static/shared/',
  '/data/web_static/releases/test/',
]:
  ensure => 'directory',
}

# Create index.html
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  force  => true,
}

# Set permissions
file { '/data/':
  recurse => true,
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Configure Nginx
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'file',
  content => "server {\n  listen 80 default_server;\n  location /hbnb_static {\n    alias /data/web_static/current/;\n  }\n}\n",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

