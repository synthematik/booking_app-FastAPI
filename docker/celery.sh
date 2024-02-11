#!/bin/bash

if [["${1}" == "celery"]]; then
  celery --src==src.tasks.celerys:celery_app worker -l INFO
elif [["${1}" == "flower"]]; then
  flower --src==src.tasks.celerys:celery_app flower
fi
