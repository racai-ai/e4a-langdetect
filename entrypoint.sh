#!/bin/bash

uwsgi --http 0.0.0.0:5000 --wsgi-file enrichforall_api.py --callable app
