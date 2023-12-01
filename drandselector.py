
# converts Drand's random string into a number between 1 and limit
def DrandSelector(randomstring, limit):
    dec = int(randomstring[:15], 16)
    base = dec % (10 ** 16) / (10 ** 16)
    reduced = int(base * limit) + 1
    reduced = 1 if reduced < 1 else reduced
    return min(reduced, limit)

# list of unique participating wallets
walletlist = {
    1: {'address': '4564SFRUYZNCVGW4IQOV7AH4DUMUXTLBE5GDC2VOPVH3OOK2SXLD3T3HR4', 'roundtime': 1657258972},
    2: {'address': 'FVNTCVBP62N7G3YL6SBEAAER6NUOWYYMWC3JQTCCBXYBSX26YS3EVXUJDA', 'roundtime': 1651204601},
    3: {'address': 'QPIWEWD6H24FNDO3FUZHBRH3QH62W2AVSG5EIJF5M3YAHK5P2B2FL4OQ2E', 'roundtime': 1650934206},
    4: {'address': 'ZWLKFCOPNWGC33T3YFDXMH72BR7BI45ZVAMONVWAS7BA33Q7PNLLTGUIAY', 'roundtime': 1650912006},
    5: {'address': '5FUG3IUJDTW2IWJFUI2MZOCLZGTO2TENQTPI6QIE7BRWRAFEQX56VQZOBE', 'roundtime': 1650890405},
    6: {'address': 'RTLMUAX6Q7ZGUHL7MHJVDRNUVEQ3MQDNWALGJNYC3ETXB2DMXQGUWGDHTQ', 'roundtime': 1650885907},
    7: {'address': '6UNXWUKWNBAY6TAIFVQACA2GFDT35JNIXJC7QVTN5GQJ53GSPPIFQCCJXE', 'roundtime': 1650879905},
    8: {'address': 'ETK4LDZAN6RAPA2I3FJ2SLKSS75AJAZCB4YSODICI634SGVXQ35RTHOIOI', 'roundtime': 1650860406},
    9: {'address': 'DLTJXMU5XV33IHQTN25CA5QKIFHV7535CEBHCEQ5QZ7BWCHILALSXM6AXI', 'roundtime': 1650850507},
   10: {'address': 'IME6H6JV36XRHYOXVOFK6SYKF4WHLSGPDCZC5KTUQR3FKRDBL5KAYXZMPM', 'roundtime': 1650823210},
}

# we reverse the timestamp before sorting it, this makes it impossible to predetermine your position, due to the blockchain's nature
for record in walletlist.values():
    record['roundtime'] = str(record['roundtime'])[::-1]

# sort the list by reverse roundtime
sorted_walletlist = dict(enumerate(sorted(walletlist.values(), key=lambda x: str(x['roundtime'])), 1))


print("new list sorted by reverse roundtime\n")
for index, record in sorted_walletlist.items():
    print(index, record['address'], record['roundtime'])

# drand random string
randomstring = '48abb268277c19989bef43a5b74a096f4be64352785abc7b48d514aafa881dd3'
limit = len(sorted_walletlist)

# calculate the winner position
winnerposition = DrandSelector(randomstring, limit)
print("\nwinner position:",winnerposition)

print("\nand the winner is:\n")
print(sorted_walletlist[winnerposition]['address'])


