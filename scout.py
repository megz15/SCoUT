'''
    Program: SCoUT
    Version: 1.0
    Author : Meghraj Goswami
    Github : github.com/megz15/SC0UT
'''

search_db = ('sarrusophone:double-reeded musical instrument resembling the bassoon',
             'vermigerous:bearing, containing or infested with worms',
             'metrology:science of weights and measures',
             'jubilate:the third Sunday after Easter',
             'unifilar:having only one thread or wire',
             'yogibogeybox:materials used by a spiritualist',
             'komatik:sled with wooden runners',
             'pomegranate:Shrub or small tree having large red many-seeded fruit'
             'hefty:Of considerable weight and size',
             'bedtick:A tick or bag made of cloth used for inclosing the materials of a bed',
             'obituarily:In the manner of an obituary',
             'parovarium:A group of tubules a remnant of the Wolffian body often found near the ovary or oviduct the epooumlphoron'
             )

import PySimpleGUI as sg
sg.theme('DarkBlack1')
imgsrc = 'res/logo.png'
menu_def = [['&Menu', ['&Clear All','Change &Logo','&About','E&xit','---','Su&rprise']]]
frame_def=[[sg.Listbox(values=[],enable_events=True,size=(18,6),key='-SELECT-'),sg.Multiline(disabled=True,size=(17,6),key='-OUT-')]]

layout = [[sg.Menu(menu_def,tearoff=False)],
          [sg.Text('  '),sg.Image(imgsrc,key='-IMG-')],
          [sg.InputText('Type to Search',size=(33,None),key='-IN-'),sg.Button(key='-SEARCH-',tooltip='Search database',image_filename='res/search.png',button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0)],
          [sg.Frame('Search Results:'+' '*18+'Definitions:'+' '*21,frame_def,border_width=0,visible=False,key='-FRAME-')]]

window = sg.Window('Search',layout,font=('Helvetica', 14))

while True:
    event, values = window.read()
    
    if event in (sg.WIN_CLOSED,'Exit'):
        break
    if event=='-SEARCH-':
        window['-FRAME-'].update(visible=True)
        window['-FRAME-'].unhide_row()
        tup_search = ()
        r_found = False
        for i in search_db:
            if values['-IN-'].lower() in i[:i.find(':')]:
                r_found = True
                tup_search+=i[:i.find(':')].title(),
        if not r_found:
            sg.popup('No Results Found\n')
        window['-SELECT-'].update(tup_search)
    if event=='-SELECT-':
        try:
            sc = [x for x in search_db if values['-SELECT-'][0].lower() in x]
        except IndexError:
            sg.popup('No Results Found\n')
        try:
            window['-OUT-'].update(sc[0][:sc[0].find(':')].title()+'\n\n'+sc[0][sc[0].find(':')+1:].title())
        except (IndexError,NameError):
            pass
    if event=='About':
        #sg.popup('Scout 1.0:\nSearch for stuff stored in tuples\n\nMade in Python 3.8.6 by Meghraj Goswami\n',title='About Program')
        window['-SELECT-'].update(['About Program'])
        window['-OUT-'].update('Scout 1.0:\nSearch for stuff stored in tuples\n\nMade in Python 3.8.6 by Meghraj Goswami\n')
    if event=='Surprise':
        #sg.popup_timed(image='res/qrick.png',auto_close_duration=3,button_type=5,title='Free BTC')
        imgsrc = 'res/qrick.png'
        window['-IMG-'].update(imgsrc)
    if event=='Clear All':
        window['-IN-'].update('Type to Search')
        window['-SELECT-'].update([])
        window['-OUT-'].update('')
        window['-FRAME-'].hide_row()
    if event=='Change Logo':
        if imgsrc=='res/logo.png':
            imgsrc = 'res/glog.png'
            window['-IMG-'].update(imgsrc)
        elif imgsrc == 'res/glog.png':
            imgsrc = 'res/logo.png'
            window['-IMG-'].update(imgsrc)
        else:
            window['-IMG-'].update('res/logo.png')
            imgsrc = 'res/logo.png'

window.close()