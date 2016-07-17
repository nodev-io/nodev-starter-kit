# Ubuntu 16.04
#
# run docker-engine-setup.sh first

# sync
sudo apt-get update
sudo apt-get -y dist-upgrade

# install docker-engine on ubuntu 16.04
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | sudo tee /etc/apt/sources.list.d/docker.list
sudo apt-get update
sudo apt-get install -y docker-engine

# check that everything is running
sudo docker ps
