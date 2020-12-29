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

echo "==================Create Python Virtual Env================================"
# create virtual python env
sudo python3 -m venv /env38
echo "====================End of Python virtual Env Creation========================="

echo "==================Install Required Python Packages================================"
source /env38/bin/activate
# wheel for package dependency; psycopg2-binary for ubuntu / psycopg2 for windows
# Install required packages
sudo pip3 install -r /vagrant/requirements.txt
echo "==================End of Installing Required Python Packages======================"

echo "==================Django Migration Start======================"
sudo python3 /vagrant/manage.py migrate
deactivate
echo "==================Django Migration End======================"