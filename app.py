# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/home')
def indexe():
    return render_template('golovna.html')


@app.route('/')
def index():
    return render_template('golovna.html')






@app.route('/first_sezon_first_serie')
def firstsfs():
    return render_template('1 sezon/0.html')



@app.route('/first_sezon_second_serie')
def firstsss():
    return render_template('1 sezon/1.html')



@app.route('/first_sezon_third_serie')
def firstsths():
    return render_template('1 sezon/2.html')



@app.route('/first_sezon_fourth_serie')
def firstsfrs():
    return render_template('1 sezon/3.html')



@app.route('/first_sezon_fiveth_serie')
def firstsfvs():
    return render_template('1 sezon/4.html')



@app.route('/first_sezon_sixth_serie')
def firstssxs():
    return render_template('1 sezon/5.html')



@app.route('/first_sezon_seventh_serie')
def firstssvs():
    return render_template('1 sezon/6.html')



@app.route('/first_sezon_eighth_serie')
def firstseis():
    return render_template('1 sezon/7.html')



@app.route('/first_sezon_nineth_serie')
def firstsns():
    return render_template('1 sezon/8.html')



@app.route('/first_sezon_tenth_serie')
def firststs():
    return render_template('1 sezon/9.html')



@app.route('/first_sezon_eleventh_serie')
def firstseleves():
    return render_template('1 sezon/10.html')



@app.route('/first_sezon_twelweth_serie')
def firststws():
    return render_template('1 sezon/11.html')



@app.route('/first_sezon_thirteenth_serie')
def firststhrts():
    return render_template('1 sezon/12.html')




@app.route('/first_sezon_fourteenth_serie')
def firstsfous():
    return render_template('1 sezon/13.html')



@app.route('/first_sezon_fifteenth_serie')
def firstsfiftens():
    return render_template('1 sezon/14.html')

@app.route('/first_sezon_sixteenth_serie')
def firstssixtens():
    return render_template('1 sezon/15.html')


@app.route('/first_sezon_seventeenth_serie')
def firstsseventens():
    return render_template('1 sezon/16.html')


@app.route('/first_sezon_eighteenth_serie')
def firstseightens():
    return render_template('1 sezon/17.html')

@app.route('/first_sezon_nineteenth_serie')
def firstsninetens():
    return render_template('1 sezon/18.html')

@app.route('/first_sezon_twentieth_serie')
def firststwentys():
    return render_template('1 sezon/19.html')




@app.route('/second_sezon_first_serie')
def first():
    return render_template('2 sezon/0.html')


@app.route('/second_sezon_second_serie')
def second():
    return render_template('2 sezon/1.html')


@app.route('/second_sezon_third_serie')
def third():
    return render_template('2 sezon/2.html')


if __name__ == "__main__":
    app.run(debug=True)