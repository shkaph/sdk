#!/usr/bin/env python3

# sudo apt install python3-pip
# pip3 install websocke

import sys
import asyncio
import websockets
import json



class Cell:
	options = [ i for i in range(1, 10) ]
	value = -1

	def serialize(self):
		res = '{'
		res += ' "options" : ' + json.dumps(self.options) + ','
		res += ' "value": ' + str( self.value )
		res += ' }'
		return res

class Playfield:
	cells = []

	def __init__(self):
		for i in range(0, 9):
			row = []
			for j in range(0, 9):
				row.append( Cell() )
			self.cells.append( row )

	def serialize(self):
		res = '{ "cells" : ['
		i = 0
		for row in self.cells:
			res += ' ['
			j = 0
			for cell in row:
				res += cell.serialize()
				j += 1
				if j < 9:
					res += ', '
			i += 1
			if i < 9:
				res += '],'
			else:
				res += ']'
		res += ' ] }'
		return res

'''
stencil = Cell()
print(stencil.options)
demo = json.dumps(stencil.options)
print(demo)

print(7 in stencil.options)
print(24 in stencil.options)

k = [i for i in range(1, 6)]
print(k)


# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York", "IDs" : [2, 7, 456]}'
# parse x:
y = json.loads(x)


# the result is a Python dictionary:
#print(y["age"])
#print(y["IDs"][1])
print(y)
z = json.dumps(y)
print(z)
'''

playfield = Playfield()
y = playfield.serialize()  # fake serialization - do not se it!
#print(y)



async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    await websocket.send(y)
    #print(f"> {greeting}")
    #print(f"> {y}")

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



'''

def main():
	print ('Python 3.x.x must be installed')
	argv = sys.argv
	argc = len(argv)
	print (argc, argv)

if __name__ == '__main__':
	main()'''