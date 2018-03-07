from app import app
from app.gw2data4 import *
from app.guildstats import * 
from flask import render_template, request, redirect
from app import app
from app.forms import LoginForm

@app.route('/', methods=['GET', 'POST'])

def index():
	form = LoginForm()
	a = guildstats()
	a.gthreads()
	guildy = {}
	ranks = a.guildcall("ranks")
	if request.method == 'POST':
		a.i = int(request.form.to_dict()['number'])
		for rank in ranks: 
			guildy[rank['id']] = a.bombling(a.called['members'],rank['id'])
		if a.i == 0:
			dict = {'Table1':guildy['Fiery Bomb'], 'Table2':guildy['Bomb'][a.i:a.i+10], 'Table3':guildy['Bombling'], 'Table4':'', 'pram':10}
			a.i = a.i + 10 
			return render_template('formaction.html', form=form, **dict)
		elif a.i >= 10:
			dict = {'Table1':guildy['Fiery Bomb'], 'Table2':guildy['Bomb'][a.i:a.i+10], 'Table3':guildy['Bombling'], 'Table4':'', 'pram':10}
			a.i = a.i + 10 
			return render_template('formaction.html', form=form, **dict)
	return render_template('form.html', title='Button Test', form=form)

@app.route('/hw')
def hw():
	a = guildstats()
	a.gthreads()
	logging.info(threading.enumerate())
	guildy = {}
	
	ranks = a.guildcall("ranks")
	for rank in ranks: 
		guildy[rank['id']] = a.bombling(a.called['members'],rank['id'])
	logging.info(guildy.keys())
	
	Firey = a.member_rank(guildy['Fiery Bomb'])
	Bomb = a.member_rank(guildy['Bomb'])
	
	logging.debug(Firey)
	logging.debug(Bomb)
	a.unpack_and_org(*a.called['log'])
	
	lst2string = lambda x: " ".join(x)
	t1 = lst2string(Firey)
	t2 = a.withdrawal_stats(*a.withdrawal)
	t3 = a.withdrawal_stats(*a.deposit)
	dict = {'Table1':guildy['Fiery Bomb'], 'Table2':guildy['Bomb'], 'Table3':t2, 'Table4':t3, 'pram':4}
	return render_template('tables.html', **dict)