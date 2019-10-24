# the-lord-of-the-certs

This is a small multiple-choice quiz presented as an RPG-battle style game written in Python3.
The player must answer multiple-choice questions to defeat randomly-generated certification exams.
Players who defeat all the certifications in a single run are granted the title of "Master Consultant".

The code is originally based on a Udemy course written by Nick Germaine (https://github.com/nickgermaine), and my original fork (https://github.com/paulbygrave/cert-slayer).
The code is intended to be a fun learning resource for teaching basic Python skills and additional questions/certifications can be added by any Contini who wishes to contribute.


## Running the program as a container

The easiest way to simply try the code is to run the pre-built Docker image in Docker Hub:

$ docker run -it --name lotc paulbygrave/the-Lord-of-the-Certs

### Installing Docker for Mac

If you haven't got Docker installed, follow the below install instructions for MacOS (written for non-techies)!
Just open a Terminal on your Mac and run all the commands in order):

#### Install prerequisite packages:

sudo apt-get update
sudo apt-get -y install \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common

#### Add the Docker GPG key and repository for the Docker software:

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

#### Install Docker CE packages:

sudo apt-get update
sudo apt-get install -y docker-ce=5:18.09.5~3-0~ubuntu-bionic docker-ce-cli=5:18.09.5~3-0~ubuntu-bionic containerd.io

#### Give your user permission to run docker commands:

sudo usermod -a -G docker $(whoami)

**[Exit and then re-open Terminal]**

#### Test the installation by running a simple container:

docker run hello-world


## Running the code locally

Alternatively, you can fork and clone this repository, then execute the code by running:

$ python3 main.py

## Desired feature additions

Shuffle the questions into random order,
External leaderboard for tracking completions,
Additional exams and questions added
