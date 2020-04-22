import colors
import subprocess as sub
import socket


def menu():
    try:
        TCP=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print(colors.color.CYAN + "    ENTER THE IPv4 Address e.g. 192.***.***.***  " + colors.color.ENDC)
        lin=colors.color.UNDERL + colors.color.BLUE + "ping" + colors.color.ENDC
        lin += "> "
        add=input(lin)
        if len(add) < 7:
            print(colors.color.RED + "Wrong input " + colors.color.ENDC)
            menu()
        else:
            print(colors.color.DARKCYAN + "Choose from the options " + colors.color.ENDC)
            try:
                print(colors.color.YELLOW + " [1] Normal ping " + colors.color.ENDC)
                print(colors.color.YELLOW + " [2] Allow pinging Broadcast " + colors.color.ENDC)
                print(colors.color.YELLOW + " [3] Flood ping " + colors.color.ENDC)
                print(colors.color.YELLOW + " [4] Suppress multicast packets " + colors.color.ENDC)
                print(colors.color.YELLOW + " [5] Set count replies " + colors.color.ENDC)
                print(colors.color.YELLOW + " [6] Adaptive ping " + colors.color.ENDC)
                print(colors.color.YELLOW + " [7] Set timeout " + colors.color.ENDC)
                print(colors.color.YELLOW + " [8] Set Deadline " + colors.color.ENDC)
                print(colors.color.YELLOW + " [9] Show user to user latency " + colors.color.ENDC)
                print(colors.color.YELLOW + " [10] Set Interval " + colors.color.ENDC)
                choice=input(lin)

                if choice[0:1] == '1':
                    print(colors.color.GREEN + "pinging ===> " + add + colors.color.ENDC)
                    TCP
                    reply=sub.getoutput('ping ' + add)
                    if reply == 0:
                        print(colors.color.GREEN + "The address up" + colors.color.ENDC)
                        print(colors.color.GREEN + reply + colors.color.ENDC)
                        menu()
                    else:
                        print(colors.color.RED + "The IP address seems to be down" + colors.color.ENDC)
                        print(colors.color.RED + reply + colors.color.ENDC)
                        menu()
                elif choice[0:1] == '2':
                    print(colors.color.GREEN + "pinging ===> " + add + colors.color.ENDC)
                    TCP
                    o2=sub.getoutput('ping -b ' + add )
                    print(colors.color.GREEN + o2 + colors.color.ENDC)
                    menu()
                elif choice[0:1] == '3':
                    print(colors.color.GREEN + "pinging ===> " + add + colors.color.ENDC)
                    TCP
                    o2=sub.getoutput('ping -f ' + add )
                    print(colors.color.GREEN + o2 + colors.color.ENDC)
                    menu()
                elif choice[0:1] == '4':
                    print(colors.color.GREEN + "pinging ===> " + add + colors.color.ENDC)
                    TCP
                    o2=sub.getoutput('ping -L ' + add )
                    print(colors.color.GREEN + o2 + colors.color.ENDC)
                    menu()
                elif choice[0:1] == '5':
                    print(colors.color.GREEN + "pinging ===> " + add + colors.color.ENDC)
                    print(colors.color.BOLD + "Enter the count int" + colors.color.ENDC)
                    count=input(lin)
                    if int(count) < 100 and int(count) > 1:
                        TCP
                        o2=sub.getoutput('ping -c ' + count + add )
                        print(colors.color.GREEN + o2 + colors.color.ENDC)
                        menu()
                    else:
                        print(colors.color.RED + "The input is inavalid " + colors.color.ENDC)
                        menu()
                elif choice[0:1] == '6':
                    print(colors.color.GREEN + "pinging ===> " + add + colors.color.ENDC)
                    TCP
                    o2=sub.getoutput('ping -A ' + add )
                    print(colors.color.GREEN + o2 + colors.color.ENDC)
                    menu()
                elif choice[0:1] == '7':
                    print(colors.color.GREEN + "pinging ===> " + add + colors.color.ENDC)
                    print(colors.color.BOLD + "Enter the timeout int " + colors.color.ENDC)
                    timeout=input(lin)
                    if timeout < 1000:
                        TCP
                        o2=sub.getoutput('ping -b ' + add )
                        print(colors.color.GREEN + o2 + colors.color.ENDC)
                        menu()
                    else:
                        print(colors.color.RED + "The int enterded is too much " + colors.color.ENDC)
                        menu()
                elif choice[0:1] == '8':
                    print(colors.color.GREEN + "pinging ===> " + add + colors.color.ENDC)
                    TCP
                    o2=sub.getoutput('ping -b ' + add )
                    print(colors.color.GREEN + o2 + colors.color.ENDC)
                    menu()
                elif choice[0:1] == '9':
                    print(colors.color.GREEN + "pinging ===> " + add + colors.color.ENDC)
                    TCP
                    o2=sub.getoutput('ping -b ' + add )
                    print(colors.color.GREEN + o2 + colors.color.ENDC)
                    menu()
                elif choice[0:2] == '10':
                    print(colors.color.GREEN + "pinging ===> " + add + colors.color.ENDC)
                    TCP
                    o2=sub.getoutput('ping -b ' + add )
                    print(colors.color.GREEN + o2 + colors.color.ENDC)
                    menu()
                else:   
                    print("Invalid input")
                    menu()
            except (KeyboardInterrupt):
                print(colors.color.RED + "\n[*] (Ctrl + C) Detected, ....EXITING" + colors.color.ENDC)
                print(colors.color.YELLOW + "[*] Thank You For Using Ping" + colors.color.ENDC)

    except(KeyboardInterrupt):
                print(colors.color.RED + "\n[*] (Ctrl + C) Detected, ....Cleaning Temporary files" + colors.color.ENDC)
                print(colors.color.YELLOW + "[*] Thank You For Using Ping" + colors.color.ENDC)


