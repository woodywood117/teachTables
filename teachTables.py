#!/usr/bin/python

import os

os.system("clear")

answer = ""

print "So, as I see it, there are three fundamental parts to IPTables: tables, chains, and targets. Tables are the different ways that IPTables sorts the different packets that enter and exit the system. On the other hand, there are chains which is the list of rules that the packets are checked against. It is important to remember that tables have chains, but chains don't have tables. The last fundamentel, targets, is the decided fate of the packet. The target decides whether the packet is altered, dropped, rejected, or allowed to pass through.\n"
raw_input("Hit enter to continue")
os.system("clear")

print "There are five types of tables:"

print "Type 1:"
print "    filter (default)"
print "        + This table is pretty self explanitory, it's used to filter packets"
print "        + 3 built-in chains:"
print "            - INPUT: Rules that check packets sent to local sockets"
print "            - FORWARD: Rules that check packets routed through the system"
print "            - OUTPUT: Rules that check locally generated packets\n"
raw_input("Hit enter to continue")
os.system("clear")

print "Type 2:"
print "    nat"
print "        + This table handles packets that generate new connections"
print "        + 3 built-in chains:"
print "            - PREROUTING: Rules for altering packets as they come in"
print "            - OUTPUT: Rules for locally generated packets before they're routed"
print "            - POSTROUTING: Rules for altering packets as they're going out\n"
raw_input("Hit enter to continue")
os.system("clear")

print "Type 3:"
print "    mangle"
print "        + Table specialized for altering packets"
print "        + 5 built-in chains:"
print "            - PREROUTING: Rules for altering packets before routing"
print "            - OUTPUT: Rules for altering locally generated packets before routing"
print "            - INPUT: Rules for altering packets coming into to system"
print "            - FORWARD: Rules for altering packets routed through the system"
print "            - POSTROUTING: Rules for altering packets as they're about to go out\n"
raw_input("Hit enter to continue")
os.system("clear")

print "Type 4:"
print "    raw"
print "        + This table is mostly used for exemptions from connection tracking in combonation witht the NOTRACK target."
print "        + It's also notable that it registers at netfilter hooks with a high priority and is called before ip_conntrack or any other IPTable"
print "        + 2 built-in chains:"
print "            - PREROUTING: Rules for any packet arriving on any network interface"
print "            - OUTPUT: Rules for any locally generated packet going out on any network interface\n"
raw_input("Hit enter to continue")
os.system("clear")

print "Type 5:"
print "    security"
print "        + This table is used for mandatory access control (MAC) networking rules like the ones enabled by SECMARK and CONNSECMARK targets"
print "        + MAC is implemented by Linux security modules like SELinux"
print "        + Notably, this table is called after the filter table so any Discretionary access control (DAC) rules can take effect before MAC rules"
print "        + 3 built-in chains:"
print "            - INPUT: Rules for packets coming into the system"
print "            - FORWARD: Rules for altering packets routed through the system"
print "            - OUTPUT: Rules for altering locally generated packets before routing\n"
raw_input("Hit enter to continue")
os.system("clear")

print "Not too bad right? Only 5 tables to learn."

while "MANGLE" not in answer.upper():
    if answer != "":
        answer = str(raw_input("Nope, try again.\n"))
    else:
        answer = str(raw_input("So, what table would you use to alter packets as they go through?\n"))

answer = ""
os.system("clear")

while "FILTER" not in answer.upper():
    if answer != "":
        answer = str(raw_input("Nope, try again.\n"))
    else:
        answer = str(raw_input("Ok, so what table would you use if you wanted to disallow a packet by some rule?\n"))

answer = ""
os.system("clear")

while "SECURITY" not in answer.upper():
    if answer != "":
        answer = str(raw_input("Nope, try again.\n"))
    else:
        answer = str(raw_input("Final table question: What table always comes after the Filter table?\n"))

answer = ""
os.system("clear")

print "Nice job! Now on to the fun part.\n"
raw_input("Hit enter to continue")
os.system("clear")

print "So, the basic structure of calling this command is:"
print "    iptables [-t table] <command> [paramaters...] [-j target | -g chain]"
print "It's **VERY IMPORTANT** to remember that the order of rules in a table matter. The program goes down the chain, so the first rules trigger first. This can lead to a lot of frustration when packets aren't getting through. Trust me, it happened to me when I was setting up my firewall."
print "The three common built-in targets are ACCEPT, DROP, and REJECT"
print "    ACCEPT allows packets through"
print "    DROP acts as if the machine never recieved the packet"
print "    REJECT sends a reply back telling the other end that the traffic was rejected"
print "\n\nSo, you remember where I said this was the fun part? Yeah, I lied. This is the part where you get to memorize a crap-ton of options\n"
raw_input("Hit enter to continue")
os.system("clear")

print "There are 3 types of options: commands, parameters, and other misc options"
print "Commands control the flow of the program, they're how you add, delete, and replace rules as well as get info from the program"
print "Parameters are how match packets to a specific rule"
print "The other misc options mostly have to do with the way the program prints out info\n"
raw_input("Hit enter to continue")
os.system("clear")

print "Commands:"
print "    -A, --append <chain> <rulespec>: This command appends a/multiple rule/s to the end of a chain\n        (it's important to remember that when a hostname resolves to more that one address, a rule is made for every combonation of address)\n"
print "    -C, --check <chain> <rulespec>: Checks if a specified rule exists in a chain\n"
print "    -D, --delete <chain> (<rulespec>|<rulenum>): Deletes the specified rulespec or rulenum from a given chain\n"
print "    -I, --insert <chain> [rulenum] <rulespec>: Inserts one or more rule as given rulenum, default = 1, or head of list\n"
print "    -R, --replace <chain> <rulenum> <rulespec>: Replace a rule. The command will fail if hostname resolves to more than one address\n"
print "    -L, --list [chain]: List the rules in a given table. If no chain is given all are shown\n"
print "    -S, --list-rules [chain]: Similar to -L, but doesn't show packet/byte counters"
print "    -F, --flush [chain]: Flush all rules (in a given chain)\n"
print "    -Z, --zero [chain [rulenum]]: Zeroes the packet and byte counters for table/chain/rule\n"
print "    -N, --new-chain <chain>: Creates a new chain(name cannot match existing target name)\n"
print "    -X, --delete-chain [chain]: Deletes a/all user defined chain/s in a table(chain must be empty)\n"
print "    -P, --policy <chain> <target>: Sets the policy for built-in chains(must be ACCEPT or DROP)\n"
print "    -E, --rename-chain <old> <new>: Renames a user-defined chain w/o altering the rules\n\n"
raw_input("Hit enter to continue")
os.system("clear")

print "Almost there! I know it's a lot to take in, but we're almost done!\n"
raw_input("Hit enter to continue")
os.system("clear")

print "Parameters (for rulespecs):"
print "    -4, --ipv4 or -6, --ipv6: these parameters don't do anything but tell the ip(6)tables-restore to ignore the rule of the opposite ipv#\n"
print "[!] -p, --protocol <proto>: Specifies protocol for the rule"
print "        (tcp,udp,udplite,icmp,icmpv6,esp,ah,sctp,mh,or all)\n"
print "[!] -s, --source <address>[/mask][,...]: Specifies source/s for rule. Can be a network-name, hostname, or IP address (with /mask)\n"
print "[!] -d, --destination <address>[/mask][,...]: Same as -s, but for destination\n"
print "[!] --sport <portnum>: Specifies the source port number for the rule\n"
print "[!] --dport <portnum>: Specifies the destination port number for the rule\n"
print "    -m, --match <match>: Rule checks for specific matched property in packet\n"
print "    -j, --jump <target>: Specifies the target of a rule. Either a chain, built-in target, or an extension"
print "        (if not specified, counter increments if packet matches, but doesn't affect packet\n"
print "    -g, --goto <chain>: Similar to -j, but doesn't continue in current chain, only in newly specified chain\n"
print "[!] -i, --in-interface <name>: Specifies interface for rule. Only works in PREROUTING, INPUT, and FORWARD\n"
print "[!] -o, --out-interface <name>: Specifies interface for rule. Only works in FORWARD, OUTPUT, and POSTROUTING"
print "        (in -i and -o, a \"+\" at the end of interface name matches anything starting with the string)\n"
print "[!] -f, --fragment: Causes rule to only match packets that are fragmented(IPv4 only)\n"
print "    -c, --set-counters <packet> <byte>: Initializes the packet/byte counters of a rule (during insertion/append/replacement to table)\n\n"
raw_input("Hit enter to continue")
os.system("clear")

print "Ok, the next list of options isn't required, they're only really useful for formatting output. You can skip them if you want.\n"
raw_input("Hit enter to continue")
os.system("clear")

print "Misc Options:"
print "    -v, --verbose: Verbose output from commands\n"
print "    -w, --wait [seconds]: Wait for xtables lock before launching program. Times out after [seconds]\n"
print "    -n, --numeric: Numeric output of ports/addresses\n"
print "    -x, exact: Prints exact number for packet/byte counters, not rounded to K, M, or G\n"
print "    --line-numbers: Numbers the lines when listing rules\n"
print "    --modprobe=<command>: When adding/inserting rules, use <command> to load any necessary modules\n"
raw_input("Hit enter to continue")
os.system("clear")

print "Quiz time!"
raw_input("Hit enter to continue")
os.system("clear")

while "-A INPUT" not in answer and "--dport 80" not in answer and ("-j REJECT" not in answer or "-j DROP" not in answer):
    if answer != "":
        answer = str(raw_input("Nope, try again.\n"))
    else:
        answer = str(raw_input("What command would you type in to block all incoming traffic to port 80?\n"))

answer = ""
os.system("clear")

while "-C INPUT" not in answer and "--dport 80" not in answer and ("-j REJECT" not in answer or "-j DROP" not in answer):
    if answer != "":
        answer = str(raw_input("Nope, try again.\n"))
    else:
        answer = str(raw_input("What command would you type to see if the rule you typed in the previous question is in the list?\n"))

answer = ""
os.system("clear")

while answer != "iptables -t nat -P OUTPUT DROP":
    if answer != "":
        answer = str(raw_input("Nope, try again.\n"))
    else:
        answer = str(raw_input("If you wanted to change the default OUTPUT policy for the nat table to DROP, what command would you type?\n"))

answer = ""
os.system("clear")

print "Good job! You made it out the other side alive! Only two more small things left:\n\n"
print "iptables-save: How you save rules in a format to restore them later"
print "    To use: iptables-save > /path/to/file"
print "and"
print "iptables-restore: How you restore saved iptables rules"
print "    To use: iptables-restore /path/to/file\n"
raw_input("Hit enter to continue")
os.system("clear")

print "THE END"
raw_input("Hit enter to exit")
os.system("clear")
