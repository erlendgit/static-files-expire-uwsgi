#!/usr/bin/env bash

export NO_DEBUG="1"

uwsgi --chdir=./ --ini=./uwsgi.ini