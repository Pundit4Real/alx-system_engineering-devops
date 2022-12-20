#Time to practice configuring your server with Puppet! Just as 
#you did before, we’d like you to install and configure an Nginx
#server using Puppet instead of Bash.
#add HTTP response header

exec { 'http header':
  command  => 'apt-get update -y;
  apt-get install nginx -y;
  sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart;',
  provider => shell,
}
