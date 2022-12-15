

print("=============================================================================================")
print("This program relies on a module called wget. Please install it to proceed.")
print("otherwise, you'll get an error below.")
import wget
print("If you are seeing this, you have wget installed. Good job.")
print("=============================================================================================")
print("Welcome to the E-Safety Quiz by Marcel Ciszewski.")
print("This script is designed to quickly and easily download the latest script, with little effort.")
print("=============================================================================================")
print("Start?")
ask = input()
if ask == "yes" or ask == "Yes":
	print("Alright.")
	print("There are two options.")
	print("Recommended")
	print("===========")
	print("1) Download the entirety of folder, with the offline video, and website.")
	print(" (This is a zip file amounting to about ≈ 30mb, which needs to be extracted.")
	print(" ")
	print("Mininum")
	print("=======")
	print("2) Download just the script (.py) file. Just the bare mininum. You will")
	print("   have the option to download the other files later on.")
	print(">>> Select your option:")
	option = input()
	if option == "1":
		print("Downloading...")
		URL = "https://raw.githubusercontent.com/realinteldiscord2004/python_project_safety/main/complete/complete.zip"
		response = wget.download(URL, "complete.zip")
		print(" ")
		print("==============================================")
		print("Finished!")
		print("Thank you for using the E-Safety Quiz Patcher.")
		print("==============================================")
	elif option == "2":
		print("Downloading...")
		URL = "https://raw.githubusercontent.com/realinteldiscord2004/python_project_safety/main/complete/"
		response = wget.download(URL, "project.py")
		print(" ")
		print("==============================================")
		print("Finished!")
		print("Thank you for using the E-Safety Quiz Patcher.")
		print("==============================================")
	else:
		print("That's not a valid option.")

else:
	print("Alright, go again next time.")
