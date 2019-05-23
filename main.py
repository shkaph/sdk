#!/usr/bin/env python3

import sys
import asyncio
import websockets
import json



class Cell:
	options	 = [ i for i in range(1, 10) ]
	value = -1

class Playfield:
	cells = []

	def __init__(self):
		for i in range(0, 9):
			cells.insert([])
			for j in range(0, 9):
				cells[i].insert(Cell())

	'''
	def __init__(self):
		:
			self.digits.append(i + 20)'''

stencil = Stencil()
print(stencil.digits)
demo = json.dumps(stencil.digits)
print(demo)

print(20 in stencil.digits)
print(24 in stencil.digits)

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





async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    #await websocket.send(greeting)
    await websocket.send(z)
    #print(f"> {greeting}")
    print(f"> {z}")

start_server = websockets.serve(hello, 'localhost', 8765)

#asyncio.get_event_loop().run_until_complete(start_server)
#asyncio.get_event_loop().run_forever()



'''

def main():
	print ('Python 3.x.x must be installed')
	argv = sys.argv
	argc = len(argv)
	print (argc, argv)

if __name__ == '__main__':
	main()'''