data = open('../task/flag.jpg', 'rb').read()
data = data[::-1]
f = open('flag.png', 'wb')
f.write(data)
f.close()