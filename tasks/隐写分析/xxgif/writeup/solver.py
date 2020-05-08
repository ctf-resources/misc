f = open('../task/xx.gif', 'rb').read()
new_f = open('flag.gif', 'wb')
new_f.write('GIF8'+f)
new_f.close()