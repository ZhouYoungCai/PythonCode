01、线程基本使用
	image
	image
	def main():
		print("在扔一个苹果")

	if __name__ == "__main__":
		main()
02、小丑扔三个苹果
	image
	image
	import threading
	import time
	def apple_1():
		print("苹果1")
		time.sleep(1)
	def apple_2():
		print("苹果2")
		time.sleep(1)
	def main():
		thread = threading.Thread(target=apple_1)
		thread2 = threading.Thread(target=apple_2)
		thread.start()
		thread2.start()
		print("苹果3")
		print("有多少小小丑？ ", threading.active_count())
		print("这些小丑是谁呢？", threading.enumerate())

	if __name__ == "__main__":
		main()
03、GIL
	import threading
	import time

	def task():
		a = 0
		while a < 9999*9999:
			a += 1


	def main():
		start_time = time.time()
		thread = threading.Thread(target=task)
		thread2 = threading.Thread(target=task)
		thread2.start()
		thread.start()
		thread.join()
		thread2.join()
		task()
		print("all time: ", time.time() - start_time)