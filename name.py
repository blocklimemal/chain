from hash import hash_block

blockchain = []
genesis = {
	'prev_hash':'',
	'index':1,
	'transactions':[]
}
blockchain = [genesis]
owner = 'Deven'
open_transaction = []


def get_balance(owner = 'Deven'):
	tx_sender = [[data['amount'] for data in block['transactions'] if data['sender'] == owner]for block in blockchain]
	# print (tx_sender)
	total_sent = 0 
	for amt in tx_sender:
		if len(amt)==0:
			continue
		else:
			total_sent  = total_sent+int(amt[0])
	
	tx_recevied = [[data['amount'] for data in block['transactions'] if data['recepient'] == owner]for block in blockchain]
	total_received = 0
	for amt in tx_recevied:
		if len(amt)==0:
			continue
		else:
			total_received  =total_received+int(amt[0])
	print (total_received -total_sent)

def get_choice():
	return input("enter your choice ")
def get_data():
	recepient = str(input("enter the person whom you want to send "))
	amount = input("enter the amount ")
	return (recepient,amount)
def add_val(recepient,amount):
	new_transaction = {
		'sender':owner,
		'recepient':recepient,
		'amount':amount
 	}
	open_transaction.append(new_transaction)

def mine():
	# prev_block
	# print (open_transaction)
	if len(blockchain) == 1:
		prev_block = blockchain[0]
		blocks = open_transaction.copy()
		hashed  = hash_block(prev_block)
		newblock = {
		'prev_hash' :hashed,
		'index':len(blockchain)+1,
		'transactions' :blocks
		}
		# print (newblock)
		blockchain.append(newblock)
		open_transaction[:] = []
	else:
		new_prev_block = blockchain[-1]
		blocks = open_transaction.copy()
		hashed  = hash_block(new_prev_block)
		newblock = {
		'prev_hash' :hashed,
		'index':len(blockchain)+1,
		'transactions' :blocks
		}
		

		blockchain.append(newblock)
		open_transaction[:] = []
while True:
	print("1. adding the transaction ")
	print("2. for printing the blockchain ")
	print("3. for mining the block ")
	print("q. for quitting the blockchain ")
	print("b to get balance")
	user_choice = get_choice()

	if user_choice == '1':
		user_input = get_data()
		recepient ,amount = user_input
		add_val(recepient,amount)
	elif user_choice == '2':
		print (blockchain)
	elif user_choice == '3':
		 mine()
	elif user_choice == 'q':
		break
	elif user_choice == 'b':
		get_balance('Deven')
print("Sucessfully quit the application ")
print("Done!!")