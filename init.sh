sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

sudo /etc/init.d/mysql restart

mysql -uroot -e 'drop database test'
mysql -uroot -e 'drop user test'
mysql -uroot -e "create database test character set 'UTF8';"
mysql -uroot -e "grant all privileges on test.* to 'test'@'%' identified by 'test';"

