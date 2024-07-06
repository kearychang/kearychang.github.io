import asyncio
import functools
import time
from threading import Thread
from typing import Callable, Any
from pynput import keyboard
from pynput.keyboard import Listener, Key

def async_timed():
	def wrapper(func: Callable) -> Callable:
		@functools.wraps(func)
		async def wrapped(*args, **kwargs) -> Any:
			print(f'starting {func} with args {args} {kwargs}')
			start = time.time()
			try:
				return await func(*args, **kwargs)
			finally:
				end = time.time()
				total = end - start
				print(f'finished {func} in {total:.4f} second(s)')
		return wrapped
	return wrapper

async def q_loop(q):
	while not q.empty():
		item = await q.get()
		await asyncio.sleep(item)
		print(item)

async def q_call(q):
	await asyncio.create_task(q_loop(q))

async def handle_a():
	q = asyncio.Queue()
	q.put_nowait(1)
	print("a")
	await asyncio.create_task(q_call(q))

async def handle_b():
	q = asyncio.Queue()
	q.put_nowait(1)
	q.put_nowait(2)
	print("b")
	await asyncio.create_task(q_call(q))

def on_press(key):
	if key == keyboard.KeyCode(char = 'a'):
		# If 'a' is pressed, put an item into the asyncio 
		#futures.append(asyncio.run_coroutine_threadsafe(handle_key_press(2, time.time() - start), loop))
		#futures.append(asyncio.run_coroutine_threadsafe(handle_key_press(2, time.time() - start), loop))
		asyncio.run(handle_a())
	elif key == keyboard.KeyCode(char = 'b'):
		asyncio.run(handle_b())
	elif key == keyboard.KeyCode(char = 'x'):
		pass
		#for future in futures:
		#	if not future.done():
		#		task = asyncio.Task.all_tasks(loop).intersection(future._asyncio_future).pop()
		#		task.cancel()

# Collect events until released
q = asyncio.Queue()
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
#listener = keyboard.Listener(on_press = on_press) 
#listener.start()
#t = Thread(target=run)
#t.start()