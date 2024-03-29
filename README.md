# Jupyterhub XAI/Linked Data Development Environment [WORK IN PROGRESS!]

## Installation

Make sure you have Docker and Docker Compose installed.

```bash
git clone https://github.com/matercomus/BScP_jupyterhub_env
cd BScP_jupyterhub_env
./build.sh
```

## Usage
1. In your browser go to 0.0.0.0:9999
1. Click Sign-Up
1. Log in

## /work directory

In the file tree, you will see /work directory.
This directory is private for your user and is persistent meaning you can save your work and come back later

Inside /work there is also /shared_data. This read-only folder is accessible to all users and is used to share files with all users.
You can copy these files into your /work directory to save and edit.

While in /shared_data, you may also clone [BScP_NBs](https://github.com/matercomus/BScP_NBs) which is a set of notebooks that demonstrates how to use jupyter notebooks and the Knowledge Engine to create solutions for Heterogeneous IoT data and IoT interoperability.
