while True:
    print 'Enter your choice'
    print '1. adding the value to blockchain'
    print '2. printing the blockchain'
    print '3.to mine'
    print "h to manpulate blockchain"
    print 'q. to quit the application'
    print 'p. to print blockchain'
    print '4. to print all participants'
    print '5. to print transaction'
    user_choice = get_user_choice()
    if user_choice == 1:
        recepient,amount = get_input()
        add_value('Deven',recepient=recepient,amount=amount)
    elif user_choice == 2:
        print blockchain
    elif user_choice == 'q':
        break
    
    elif user_choice == 3:
    	mine()
    elif user_choice == 4:
        all_participant()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'p':
    	print blockchain
    elif user_choice == 5:
        get_all_transaction('Deven')
    else:
    	print "enter a valid response"

    if not verify_blockchain():
    	print "Not a valid blockchain"
    	break

print 'successfully quit the application'


