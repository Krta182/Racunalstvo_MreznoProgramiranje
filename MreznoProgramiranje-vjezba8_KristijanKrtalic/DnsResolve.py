import dns.resolver 

myDnsResolver = dns.resolver.Resolver() 
PrimjerA = myDnsResolver.query("google.com", "A") 
PrimjerMX= myDnsResolver.query("google.com", "MX")
PrimjerPTR= myDnsResolver.query("3.125.194.174.in-addr.arpa", "PTR")  
for data in PrimjerA: 
    print ('A primjer-',data) 
for data in PrimjerMX:
    print ('MX primjer-',data)
for data in PrimjerPTR:
    print ('PTR primjer-',data)             