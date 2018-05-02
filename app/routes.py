from app import app
from app.memberobject import *
from flask import render_template, request, redirect, jsonify
from app import app
from app.forms import LoginForm
import sqlite3


@app.route('/', methods=['GET', 'POST'])
def index():
    a = memberobj()
    a.gthreads()
    a.unpack_and_org(*a.called['log'])
    guildy = {}
    form = LoginForm()

    if request.method == 'POST':
        a.stat_threads(a.withdrawal)
        a.member(*a.thread_data, action='withdraw')
        a.stat_threads(a.deposit)
        a.member(*a.thread_data, action='deposit')
        a.i = int(request.form.to_dict()['number'])
        for rank in a.called['ranks']:
            guildy[rank['id']] = a.bombling(a.called['members'], rank['id'])
        dict = {'Table3': a.withdrawal[a.i:a.i + 10], 'Table4': a.deposit[a.i:a.i + 10], 'pram': 10,
                'Bombling': guildy['Bombling'], 'Bomb': guildy['Bomb'], 'FlashBomb': guildy['Flash Bomb'],
                'FieryBomb': guildy['Fiery Bomb'], 'FizzlingBomb': guildy['Fizzling Bomb'],
                'RogueBomb': guildy['Rogue Bomb'], 'StrangeBomb': guildy['Strange Bomb']}
        if a.i == 0:
            a.i = a.i + 10
            return render_template('formaction.html', form=LoginForm(td=a.thread_data), **dict)
        elif a.i >= 10:
            a.i = a.i + 10
            return render_template('formaction.html', form=LoginForm(td=a.thread_data), **dict)
    return render_template('form.html', title='Button Test', form=form)


@app.route('/hw')
def hw():
    a = guildstats()
    a.gthreads()
    logging.info(threading.enumerate())
    guildy = {}

    ranks = a.guildcall("ranks")
    for rank in ranks:
        guildy[rank['id']] = a.bombling(a.called['members'], rank['id'])
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
    dict = {'Table1': guildy['Fiery Bomb'], 'Table2': guildy['Bombling'], 'Table3': t2, 'Table4': t3, 'pram': 4}
    return render_template('tables.html', **dict)


@app.route('/test')
def test():
    a = memberobj()
    a.gthreads()
    a.unpack_and_org(*a.called['log'])
    guildy = {}
    for rank in a.called['ranks']:
        guildy[rank['id']] = a.bombling(a.called['members'], rank['id'])

    dict = {
        'Bombling': guildy['Bombling'],
        'Bomb': guildy['Bomb'],
        'FlashBomb': guildy['Flash Bomb'],
        'FieryBomb': guildy['Fiery Bomb'],
        'FizzlingBomb': guildy['Fizzling Bomb'],
        'RogueBomb': guildy['Rogue Bomb'],
        'StrangeBomb': guildy['Strange Bomb']
    }

    return render_template('test.html', **dict)


@app.route('/members')
def members():
    a = memberobj()
    a.gthreads()
    a.unpack_and_org(*a.called['log'])
    guildy = {}
    for rank in a.called['ranks']:
        guildy[rank['id']] = a.bombling(a.called['members'], rank['id'])

    dict = {
        'Bombling': guildy['Bombling'],
        'Bomb': guildy['Bomb'],
        'FlashBomb': guildy['Flash Bomb'],
        'FieryBomb': guildy['Fiery Bomb'],
        'FizzlingBomb': guildy['Fizzling Bomb'],
        'RogueBomb': guildy['Rogue Bomb'],
        'StrangeBomb': guildy['Strange Bomb']
    }

    return render_template('tables.html', **dict)


@app.route('/recruit_stats')
def rt():
    a = memberobj()
    a.gthreads()
    a.unpack_and_org(*a.called['log'])

    def dict_factory(cursor, row):
       d = {}
       for idx, col in enumerate(cursor.description):
           d[col[0]] = row[idx]
       return d

    conn = sqlite3.connect('guild.db')
    conn.row_factory = dict_factory
    gdb = conn.cursor()

    # Create table if doesn't exist
    try:
        gdb.execute('''CREATE TABLE invited (invitied_by text, date text, user TEXT UNIQUE ON CONFLICT REPLACE)''')
    except:
        print("Table Already Exists")
        pass
    #
    for invitees in a.invited:
        gdb.execute("INSERT INTO invited VALUES ('{invited_by}', '{time}', '{user}')".format(**invitees))

    conn.commit()
    gdb.execute("Select invitied_by, count(invitied_by) as count from invited group by invitied_by")
    data = gdb.fetchall()

    for q in data:
        print(q)

    return render_template('recruit_stats.html', data=data)
