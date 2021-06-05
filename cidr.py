import math

class IP() :
    def __init__(self, address, hostbits) :
        self.address = address
        self.hostbits = hostbits
        self.network_mask = 0
        self.max_no_of_subnets = 0
        self.max_no_of_address = 0
        self.start_address = 0
        self.end_address = 0
        self.no_of_subnets = 0


    def Info(self) :
        print("\nConsider Minimum size of a single subnet as 4 address :") 
        self.max_no_of_subnets = (2 ** (self.hostbits - 2))
        print("Maximum number of subnets possible = %d" % self.max_no_of_subnets)

        self.max_no_of_address = (2 ** self.hostbits)
        print("Maximum number of address = %d" % self.max_no_of_address)

        self.start_address = self.address & ~(2 ** hostbits - 1)
        self.end_address = self.address | (2 ** hostbits - 1)

        print("Address Range :")
        print("  Start Address = ", end = '')
        PrintIP(self.start_address, self.hostbits)
        print("  End Address = ", end = '')
        PrintIP(self.end_address, self.hostbits)

        print("Network ID = ", end = '')
        PrintIP(self.address & ~(2 ** self.hostbits - 1), self.hostbits)
        print("Broadcast Address = ", end = '')
        PrintIP(self.address | (2 ** self.hostbits - 1), self.hostbits)

        self.network_mask = ~(2 ** self.hostbits - 1)
        print("Network Mask = ", end = '')
        PrintIP(self.network_mask, self.hostbits)
        

    def Subnets(self):
        print("\nEnter the number of subnets in the range(%d, %d)" % (0, self.max_no_of_subnets ))
        self.no_of_subnets = int(input())
        print("")
        if self.no_of_subnets > self.max_no_of_subnets :
            exit("Error !!! Follow the range")

        subnet_sizes = list()
        print("Enter the number of hosts in each subnet :")
        for i in range(0, self.no_of_subnets) :
            subnet_sizes.append(int(input()) + 2)
            pos = math.ceil(math.log(subnet_sizes[i], 2))
            subnet_sizes[i] = 2**pos

        print("")
        if sum(subnet_sizes) > self.max_no_of_address :
            exit("Subnets cannot accomodate required number hosts")

        print("Subnet Mask, SubnetID and BroadcastID for all the subnets are as follows :")
        networkid = self.start_address

        for i in range(0, self.no_of_subnets) :
            mask = ~(subnet_sizes[i] - 1)
            print("%d) \tSubnetMask :" % (i+1), end = " ")
            PrintMask(mask)

            print("\tSubnetID :", end = " ")
            PrintIP(networkid, math.log(subnet_sizes[i], 2))
            networkid = networkid + subnet_sizes[i]
            print("\tBroadcastID :", end = " ")
            PrintIP(networkid - 1, math.log(subnet_sizes[i], 2))
            print("\tMaskBits : %d" %(32 - math.log(subnet_sizes[i], 2)))
            print("")

def PrintMask(address) :
    print((address & 0xFF000000) >> 24, (address & 0xFF0000) >> 16, (address &
        0xFF00) >> 8, address & 0xFF, sep = ".")

def PrintIP(address, hostbits) :
    print((address & 0xFF000000) >> 24, (address & 0xFF0000) >> 16, (address &
        0xFF00) >> 8, address & 0xFF, sep = ".", end = "")
    print("/%d" % (32 - hostbits))

if __name__ == "__main__" :

    print("Enter the IP address in '/' notation")
    temp = input()
    if '/' not in temp :
        exit("Follow the notation")
    x = list(map(str, temp.split(".")))

    if len(x) != 4 :
        exit("Invalid IP")

    x[3], networkbits = x[3].split('/')
    x = list(map(int, x))

    hostbits = 32 - int(networkbits)
    if hostbits < 3 :
        print("No subnets possible")
        exit()
    for i in x :
        if i < 0 or i > 255 :
            exit("Invalid IP")

    address = 0
    address = x[0] << 24
    address = address + (x[1] << 16)
    address = address + (x[2] << 8)
    address = address + x[3]
    ip = IP(address, hostbits)
    ip.Info()
    ip.Subnets()
