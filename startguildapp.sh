source ~/Dev/guildapp/venv/bin/activate
export FLASK_APP=guildapp.py
cd ~/Dev/guildapp
flask run -h 172.27.9.123 -p 8080 &
