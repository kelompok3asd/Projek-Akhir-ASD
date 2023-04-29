import os

class FriendList:

	class FriendNode:

		# constructor untuk kelas FriendNode
		def __init__(self, name, id_char, level, total_achievement):
			self.name = name
			self.id_char = id_char
			self.level = level
			self.total_achievement = total_achievement
			self.next = None
			
	# constructor untuk kelas FriendList
	def __init__(self):
		self.head = None
		self.size = 0

	# fungsi untuk menambahkan teman baru
	def add_friend(self, name, id_char, level, total_achievement):

		new_friend = self.FriendNode(name, id_char, level, total_achievement)

		# jika head isinya kosong (linked list blum ada isinya), tambahkan node baru.
		if self.head == None:
			self.head = new_friend
			self.size += 1
		else:

			# jika head sudah ada (menunjuk ke node pertama).
			current = self.head
			# selama node selanjutnya tidak kosong (None), maka next.
			while current.next != None:
				current = current.next
			# jika node selanjutnya kosong (== None), maka tambahkan node baru di akhir list.
			current.next = new_friend
			self.size += 1	
			
	# fungsi untuk menghapus teman dari daftar
	def remove_friend(self, name):

		# jika head isinya kosong (None), kembalikan nilai 'return'
		if self.head == None:
			return 'There is no one to be removed cause there is no friend yet.'
		
		# jika nama dari head adalah nama yang diinput, 
		if self.head.name == name:
			self.head = self.head.next
			self.size -= 1
			return
		
		current = self.head
		while current.next != None:
			if current.next.name == name:
				current.next = current.next.next
				return
			current = current.next
		
	# fungsi merge sort (untuk mendapatkan nilai tengah dalam linked list)
	def get_mid(self, head):
		if head is None:
			return head
		
		slow = head
		fast = head.next
		
		while fast is not None:
			fast = fast.next
			if fast is not None:
				slow = slow.next
				fast = fast.next
		
		return slow

	# fungsi untuk mengembalikan linked list setelah diurutkan menggunakan merge sort secara ascending
	def merge_sort_ascending(self, head):
		if head == None or head.next == None:
			return head
		
		mid = self.get_mid(head)
		mid_next = mid.next
		mid.next = None

		left = self.merge_sort_ascending(head)
		right = self.merge_sort_ascending(mid_next)

		return self.merge_ascending(left, right)
	
	# fungsi untuk mengembalikan linked list setelah diurutkan menggunakan merge sort secara descending
	def merge_sort_descending(self, head):
		if head == None or head.next == None:
			return head
		
		mid = self.get_mid(head)
		mid_next = mid.next
		mid.next = None

		left = self.merge_sort_descending(head)
		right = self.merge_sort_descending(mid_next)

		return self.merge_descending(left, right)
	
	# fungsi untuk menggabungkan dua linked list pada merge sort secara ascending
	def merge_ascending(self, left, right):
		if left == None:
			return right
		if right == None:
			return left
		
		if left.level <= right.level:
			result = left
			result.next = self.merge_ascending(left.next, right)
		else:
			result = right
			result.next = self.merge_ascending(left, right.next)

		return result

	def merge_descending(self, left, right):
		if left == None:
			return right
		if right == None:
			return left
		
		if left.level >= right.level:
			result = left
			result.next = self.merge_descending(left.next, right)
		else:
			result = right
			result.next = self.merge_descending(left, right.next)

		return result

	# fungsi untuk algoritma jump search
	def jump_search(self, name):
		n = self.size
		step = int(n ** 0.5)
		prev = 0
		while prev < n and self.head:
			current = self.head
			# jump to next block
			for x in range(min(step, n-prev)):
				if current.name == name:
					return current
				current = current.next
			prev += step
		# if friend not found in the first block, search linearly
		while current:
			if current.name == name:
				return current
			current = current.next
		return None
	
	# fungsi untuk melihat output list pertemanan in game.
	def print_friends(self):
		result = []
		current = self.head

		if self.head == None:
			return 'Friend list is empty. Go get a friend!'
		
		while current != None:
			result.append(current.name)
			current = current.next
		return ', '.join(result)

	# fungsi untuk melihat output seorang teman beserta atributnya.
	def print_detail(self, name):
		if self.head == None:
			return 'Friend list is empty. Go get a friend!'

		current = self.head
		while current != None:
			if current.name == name:
				friend = f"Name: {current.name}\nID: {current.id_char}\nLevel: {current.level}\nTotal Achievement: {current.total_achievement}"
				return friend
			current = current.next

# dictionary untuk menyimpan data user dan object linked list.
users = {}
friend_lists = {}

def friend_menu(friend):

	while True:
		
		print(f'IN GAME FRIEND LIST \n \
			1. Show friend list \n \
			2. Show detailed info about a friend \n \
			3. Add friend \n \
			4. Unfriend  \n \
			5. Sort by level (ascending) \n \
			6. Sort by level (descending) \n \
			7. Back')
		try:
			usr_input =  int(input('Select your need : '))

			if usr_input == 1:
				os.system('cls')
				print(friend.print_friends())

				null = input('More? (y/n) : ')
				if null == 'y':
					break
				else:
					break

			elif usr_input == 2:

				os.system('cls')
				name = input('Type the name : ')
				friend = friend.jump_search(name)
				if friend:
					print(f"Friend found!")
					print(friend.print_detail(name))
				else:
					print("Friend not found")

				null = input('More? (y/n) : ')
				if null == 'y':
					break
				else:
					break

			elif usr_input == 3:

				os.system('cls')
				name = input('Name : ')
				id_char = int(input('ID : '))
				level = int(input('Level : '))
				avt = int(input('Total achievement : '))

				os.system('cls')
				friend.add_friend(name, id_char, level, avt)
				print('Friend succesfully added!')
				print(friend.print_friends())

				null = input('More? (y/n) : ')
				if null == 'y':
					break
				else:
					break

			elif usr_input == 4:
				
				os.system('cls')
				unfriend = input('Input the name you want to unfriend : ')
				friend.remove_friend(unfriend)

				null = input('More? (y/n) : ')
				if null == 'y':
					break
				else:
					print('Byeee~')
					break
			
			elif usr_input == 5:
				
				friend.head = friend.merge_sort_ascending(friend.head)
				print(friend.print_friends())

				null = input('More? (y/n) : ')
				if null == 'y':
					break
				else:
					break

			elif usr_input == 6:

				friend.head = friend.merge_sort_descending(friend.head)
				print(friend.print_friends())

				null = input('More? (y/n) : ')
				if null == 'y':
					break
				else:
					break

			elif usr_input == 7:

				ask = input('Back to previous menu? (Y/N) : ')

				if ask.lower() == 'y':
					break

		except TypeError as t:
			# print('Wrong input!')
			print(t)
			break

def register():

	us = input('New username : ')
	pw = input('New password : ')

	if us in users:
		print("Error: Username already exists.")
		return
	
	# Create a new instance of FriendList for the user
	friend_lists[us] = FriendList()
	
	# Store the user's data, including the FriendList instance, in the users dictionary
	users[us] = {"password": pw, "friend_list": friend_lists[us]}
	
	print("User registered successfully.")
	print(users)
	print(friend_lists)
	login()

def login():

	us = input('Username : ')
	pw = input('Password : ')

	if us not in users:
		print("Error: Username does not exist.")
		return False
	
	if users[us]["password"] != pw:
		print("Error: Incorrect password.")
		return False
	
	print("Logged in as:", us)
	friend_menu(users[us]["friend_list"])  # Pass the user's FriendList to the friend menu

os.system('cls')
def main_menu():
	while True:
		print('''
		1. Register
		2. Login
		3. Quit
		''')
		action = input('Select your choice (1-3) : ')
		if action == '1':
			register()
		elif action == '2':
			login()
		elif action == '3':
			print('Byee~')
			break
		else:
			print('invalid input')

main_menu()
