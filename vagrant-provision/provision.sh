echo "==================Update apt-get================================"
sudo apt-get update
sudo apt install net-tools
echo "====================End of Updating apt-get========================="

# Install postgresql
echo "==================Install Postgresql================================"
sudo apt -y install postgresql-12
# Create the user to access the db.
sudo -u postgres psql -c "CREATE USER vagrant WITH SUPERUSER CREATEDB ENCRYPTED PASSWORD 'vagrant'"
sudo -u postgres psql -c "CREATE DATABASE datasc WITH OWNER vagrant"
echo "====================End of Postgresql========================="

echo "==================Install Python================================"
# Install pip3, virtualenv
sudo apt -y install python3.8 python3-pip python3-venv
echo "====================End of Python Installation========================="

echo "==================Install Apache================================"
sudo apt install -y apache2 apache2-dev
sudo apt install libapache2-mod-wsgi-py3
echo "====================End of Apache========================="

echo "==================Create directories================================"
sudo mkdir /vagrant/logs
echo "====================End of creation========================="

echo "==================Process Apache Settings================================"
sudo a2enmod wsgi
sudo cp /etc/apache2/apache2.conf /etc/apache2/apache2.conf.orig
sudo cp /vagrant/vagrant-provision/apache2.conf /etc/apache2/apache2.conf
sudo cp /vagrant/vagrant-provision/django.conf /etc/apache2/sites-available/django.conf
sudo cp /vagrant/vagrant-provision/ports.conf /etc/apache2/ports.conf
sudo a2dissite 000-default
sudo a2ensite django
sudo systemctl restart apache2
echo "==================End of Apache Settings================================"

echo "==================Install Cron================================"
sudo apt install cron
echo "====================End of Cron Installation========================="

echo "==================Install Django and Mod_wsgi================================"
sudo pip3 install Django==3.0.8
echo "====================End of Django and Mod_wsgi========================="

echo "==================Create Python Virtual Env================================"
# create virtual python env
sudo python3 -m venv /env38
echo "====================End of Python virtual Env Creation========================="