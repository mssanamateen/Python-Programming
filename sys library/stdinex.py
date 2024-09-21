import sys
''' stdin uses input() function internally and also adds a \n at the end of each sentence'''
for w in sys.stdin:
	if 'quit' ==w.rstrip():
		break
	print(f'Input:{w}')
print("exit")