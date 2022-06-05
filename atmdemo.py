#atmdemo.py---main program
from atmmenu import menu
import sys
from atmoperations import deposit,withdraw,balenq
from atmexcept import DepositError,WithdrawError,InSuffFundError
while(True):
	menu()
	try:
		ch=int(input("Enter ur Choice:"))
		match(ch):
			case 1: 
				try:
					deposit()
				except ValueError:
					print("\nDon't try to deposit strs/ symbols / alpha-numerics")
				except DepositError:
					print("\nDon't try to deposit -ve / zero value")
			case 2: 
				try:		
					withdraw()
				except ValueError:
					print("\nDon't try to withdraw strs/ symbols / alpha-numerics")
				except WithdrawError:
					print("\nDon't try to withdraw -ve / zero value")
				except InSuffFundError:
					print("\nUr Account does not have sufficient Funds:")
			case 3: 
					balenq()
			case 4: 
					print("Thanks for using this application")
					sys.exit()
			case _:
					print("Ur Selection of Operation is wrong--try again")
	except ValueError:
		print("Don't enter strs or symbols or alpha-numerics for choice of operations")