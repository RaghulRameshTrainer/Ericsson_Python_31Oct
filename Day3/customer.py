import sys

if len(sys.argv) != 3:
    print("USAGE: {} {} {}".format(sys.argv[0], "cust_name", "policy_number"))
    print("Please run with cust name and policy number")
    sys.exit()

print("Program name:",sys.argv[0])
print("Customer name:", sys.argv[1])
print("Policy Number:", sys.argv[2])
