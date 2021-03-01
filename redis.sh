#!/bin/sh

sudo apt-get update
sudo apt-get install redis-server
redis-cli
expire Hash 60
expire Time 60
expire "Bitcoin value" 60
expire "Dollar value" 60