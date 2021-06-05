import math

class IP() :
    def __init__(self, address) :
        self.address = address
        self.subnet_mask = 0
        self.ip_class = ""
        self.no_of_subnets = 0
        self.subnet_power = 0

    def NetworkClass(self) :
        x = self.address >> 24
        if 0 <= x <= 127 :
            print("The IP Address belongs to : Class A")
            self.ip_class = "Class A"
        elif 128 <= x <= 191 :	
            print("The IP Address belongs to : Class B")
            self.ip_class = "Class B"
        elif 192 <= x <= 223 :
            print("The IP Address belongs to : Class C")
            self.ip_class = "Class C"
        elif 224 <= x <= 239 :
            print("The IP Address belongs to : Class D")
            self.ip_class = "Class D"
            exit("Subnetting is not possible")
        elif 240 <= x <= 255 :
            print("The IP Address belongs to : Class E")
            self.ip_class = "Class E"
            exit("Subnetting is not possible")
        else :
            exit("Invalid IP address")

    def FixedSubnets(self) :

        if self.ip_class == 'Class A' :
            print("\nEnter the number 'n' such that network is divided in 2^n subnets and n is in range(%d, %d)" % (0, 22))
            self.subnet_power = int(input()) 
            if self.subnet_power > 22 :
                exit("Error !!! Follow the range")
            self.no_of_subnets = 2**self.subnet_power

            print("\nThe number of subnets are : %d" % self.no_of_subnets)

            self.subnet_mask = 0xFF000000 | (~(2 ** (24-self.subnet_power) - 1))
            print("\nSubnet Mask is :")
            PrintIP(self.subnet_mask)

            size = int((2**24) / self.no_of_subnets)
            
            print("\nThe Network and Broadcast IDs for all subnets are :")
            networkid = self.address & 0xFF000000 
            for i in range(0, self.no_of_subnets) :
                x = (networkid + (i * size))
                y = (networkid + ((i + 1) * size)) - 1
                print("%d) \tSubnetID   : " % (i + 1), end = '')
                PrintIP(x)
                print("\tBroadcastID : ", end = '')
                PrintIP(y)
                print("")

        elif self.ip_class == 'Class B' :
            print("\nEnter the number 'n' such that network is divided in 2^n subnets and n is in range(%d, %d)" % (0, 14))
            self.subnet_power = int(input()) 
            if self.subnet_power > 14 :
                exit("Error !!! Follow the range")
            self.no_of_subnets = 2**self.subnet_power

            print("\nThe number of subnets are : %d" % self.no_of_subnets)

            self.subnet_mask = 0xFFFF0000 | (~(2 ** (16-self.subnet_power) - 1))
            print("\nSubnet Mask is :")
            PrintIP(self.subnet_mask)

            size = int((2**16) / self.no_of_subnets)
            
            print("\nThe Network and Broadcast IDs for all subnets are :")
            networkid = self.address & 0xFFFF0000 
            for i in range(0, self.no_of_subnets) :
                x = (networkid + (i * size))
                y = (networkid + ((i + 1) * size)) - 1
                print("%d) \tSubnetID   : " % (i + 1), end = '')
                PrintIP(x)
                print("\tBroadcastID : ", end = '')
                PrintIP(y)
                print("")

        elif self.ip_class == 'Class C' :
            print("\nEnter the number 'n' such that network is divided in 2^n subnets and n is in range(%d, %d)" % (0, 6))
            self.subnet_power = int(input()) 
            if self.subnet_power > 6 :
                exit("Error !!! Follow the range")
            self.no_of_subnets = 2**self.subnet_power

            print("\nThe number of subnets are : %d" % self.no_of_subnets)

            self.subnet_mask = 0xFFFFFF00 | (~(2 ** (8-self.subnet_power) - 1))
            print("\nSubnet Mask is :")
            PrintIP(self.subnet_mask)

            size = int((2**8) / self.no_of_subnets)
            
            print("\nThe Network and Broadcast IDs for all subnets are :")
            networkid = self.address & 0xFFFFFF00 
            for i in range(0, self.no_of_subnets) :
                x = (networkid + (i * size))
                y = (networkid + ((i + 1) * size)) - 1
                print("%d) \tSubnetID   : " % (i + 1), end = '')
                PrintIP(x)
                print("\tBroadcastID : ", end = '')
                PrintIP(y)
                print("")

    def VariableSubnets(self) :

        if self.ip_class == 'Class A' :
            print("\nEnter the number of subnets in the range(%d, %d)" % (0, 2**22))
            self.no_of_subnets = int(input())
            print("")
            if self.no_of_subnets > 2**22 :
                exit("Error !!! Follow the range")

            subnet_sizes = list()
            print("Enter the number of hosts in each subnet :")
            for i in range(0, self.no_of_subnets) :
                subnet_sizes.append(int(input()) + 2)
                pos = math.ceil(math.log(subnet_sizes[i], 2))
                subnet_sizes[i] = 2**pos 

            print("")
            if sum(subnet_sizes) > (2**24) :
                exit("Subnets cannot accomodate required number hosts")

            print("Subnet Mask, NetworkID and BroadcastID for all the subnets are as follows :")
            networkid = self.address & 0xFF000000
            for i in range(0, self.no_of_subnets) :
                self.subnet_mask = 0xFF000000 | (~(subnet_sizes[i] - 1))
                print("%d) \tSubnetMask :" % (i+1), end = " ")
                PrintIP(self.subnet_mask)
                print("\tSubnetID :", end = " ")
                PrintIP(networkid)
                networkid = networkid + subnet_sizes[i]
                print("\tBroadcastID :", end = " ")
                PrintIP(networkid-1)
                print("")
                
        elif self.ip_class == 'Class B' :
            print("\nEnter the number of subnets in the range(%d, %d)" % (0, 2**14))
            self.no_of_subnets = int(input())
            print("")
            if self.no_of_subnets > 2**16 :
                exit("Error !!! Follow the range")

            subnet_sizes = list()
            print("Enter the number of hosts in each subnet :")
            for i in range(0, self.no_of_subnets) :
                subnet_sizes.append(int(input()) + 2)
                pos = math.ceil(math.log(subnet_sizes[i], 2))
                subnet_sizes[i] = 2**pos 

            print("")
            if sum(subnet_sizes) > (2**16) :
                exit("Subnets cannot accomodate required number hosts")

            print("Subnet Mask, NetworkID and BroadcastID for all the subnets are as follows :")
            networkid = self.address & 0xFFFF0000
            for i in range(0, self.no_of_subnets) :
                self.subnet_mask = 0xFFFF0000 | (~(subnet_sizes[i] - 1))
                print("%d) \tSubnetMask :" % (i+1), end = " ")
                PrintIP(self.subnet_mask)
                print("\tSubnetID :", end = " ")
                PrintIP(networkid)
                networkid = networkid + subnet_sizes[i]
                print("\tBroadcastID :", end = " ")
                PrintIP(networkid-1)
                print("")

        elif self.ip_class == 'Class C' :
            print("\nEnter the number of subnets in the range(%d, %d)" % (0, 2**6))
            self.no_of_subnets = int(input())
            print("")
            if self.no_of_subnets > 2**6 :
                exit("Error !!! Follow the range")

            subnet_sizes = list()
            print("Enter the number of hosts in each subnet :")
            for i in range(0, self.no_of_subnets) :
                subnet_sizes.append(int(input()) + 2)
                pos = math.ceil(math.log(subnet_sizes[i], 2))
                subnet_sizes[i] = 2**pos 

            print("")
            if sum(subnet_sizes) > (2**8) :
                exit("Subnets cannot accomodate required number hosts")

            print("Subnet Mask, NetworkID and BroadcastID for all the subnets are as follows :")
            networkid = self.address & 0xFFFFFF00
            for i in range(0, self.no_of_subnets) :
                self.subnet_mask = 0xFFFFFF00 | (~(subnet_sizes[i] - 1))
                print("%d) \tSubnetMask :" % (i+1), end = " ")
                PrintIP(self.subnet_mask)
                print("\tSubnetID :", end = " ")
                PrintIP(networkid)
                networkid = networkid + subnet_sizes[i]
                print("\tBroadcastID :", end = " ")
                PrintIP(networkid-1)
                print("")

def PrintIP(address) :
    print((address & 0xFF000000) >> 24, (address & 0xFF0000) >> 16, (address &
        0xFF00) >> 8, address & 0xFF, sep = ".")

if __name__ == "__main__" :

    print("Enter the IP address")
    try :
        temp = list(map(int, input().split(".")))
    except :
        exit("Error")

    if len(temp) != 4 :
        exit("Invalid IP Address")

    address = 0
    address = temp[0] << 24
    address = address + (temp[1] << 16)
    address = address + (temp[2] << 8)
    address = address + temp[3]
    ip = IP(address)
    ip.NetworkClass()
    print("\nSelect the type of Subnetting :\n'1' for FIXED and '2' for VARIABLE :")
    typ = int(input())
    if typ == 1:
        ip.FixedSubnets()
    elif typ == 2 :
        ip.VariableSubnets()
