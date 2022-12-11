#!/bin/sh
python data/fill_db.py
echo "Bases are created"
echo "Start to use bio-app"
sleep 2000
echo "Oops, rebuild containers!"