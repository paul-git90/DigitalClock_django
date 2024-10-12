from django.shortcuts import render
import datetime


def digital_clock(request):
    ora_curenta = datetime.datetime.now()
    ora_formatata = ora_curenta.strftime('%H:%M:%S %p')
    ora_formatata = ora_formatata.replace(':', "o")
    dict_clock = {
        '0': [' _ ',
              '| |',
              '|_|'],

        '1': ['   ',
              '  |',
              '  |'],

        '2': [' _ ',
              ' _|',
              '|_ '],

        '3': [' _ ',
              ' _|',
              ' _|'],

        '4': ['   ',
              '|_|',
              '  |'],

        '5': [' _ ',
              '|_ ',
              ' _|'],

        '6': [' _ ',
              '|_ ',
              '|_|'],

        '7': [' _ ',
              '  |',
              '  |'],

        '8': [' _ ',
              '|_|',
              '|_|'],

        '9': [' _ ',
              '|_|',
              '  |'],

        'o': ['   ',
              ' o ',
              '   ']
    }
    output_line = ['', '', '']
    for caracter in ora_formatata:
        if caracter in dict_clock:
            numar = dict_clock[caracter]
            for i in range(3):
                output_line[i] += numar[i] + '   '
    return render(request, 'clock_digital/clock.html', {'output_line': output_line})
