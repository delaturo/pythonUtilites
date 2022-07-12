import time
import Log

# print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
print(Log.style.BLACK + "Test BLACK" + Log.style.RESET)
print(Log.style.RED + "Test RED" + Log.style.RESET)
print(Log.style.GREEN + "Test GREEN" + Log.style.RESET)
print(Log.style.YELLOW + "Test YELLOW" + Log.style.RESET)
print(Log.style.BLUE + "Test BLUE" + Log.style.RESET)
print(Log.style.MAGENTA + "Test MAGENTA" + Log.style.RESET)
print(Log.style.CYAN + "Test CYAN" + Log.style.RESET)
print(Log.style.WHITE + "Test WHITE" + Log.style.RESET)
print(Log.style.UNDERLINE + "Test UNDERLINE" + Log.style.RESET)
print(Log.style.ITALIC + "Test ITALIC" + Log.style.RESET)
print(Log.style.BOLD + "Test BOLD" + Log.style.RESET)


Log.log("Hello World!")
Log.log("Hello World in Green!", Log.style.GREEN)

styles=[Log.style.BLACK, Log.style.RED, Log.style.GREEN, Log.style.YELLOW, Log.style.BLUE,
        Log.style.MAGENTA, Log.style.CYAN, Log.style.WHITE, Log.style.UNDERLINE, Log.style.ITALIC, Log.style.BOLD]

for i in range(11):
    Log.logAsProgress("This is a progress at "+ str(i) +" out of 10", logStyle=styles[i] )
    time.sleep(0.5)
Log.log("")

for i in range(11):
    Log.logAsProgress("This is an animated progress...", animated=True,  logStyle=styles[10-i])
    time.sleep(0.25)
Log.log("")

for i in range(21):
    p = i/20
    Log.logAsProgress("This is a progress bar...", progress=p ,  logStyle=styles[10-i])
    time.sleep(0.5)
Log.log("")

for i in range(21):
    p = i/20
    Log.logAsProgress("This is a animated progress bar...", progress=p, animated=True ,  logStyle=styles[10-i])
    time.sleep(0.25)

Log.log("Done", Log.style.GREEN)