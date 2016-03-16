sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

mysql -uroot -e 'drop database db_mysql'
mysql -uroot -e 'drop user root'
mysql -uroot -e "create database db_mysql character set 'UTF8';"
sudo /etc/init.d/mysql restart
