with open('data/addresses.txt', 'r', encoding='utf-8-sig') as file:
    addresses = [line.strip() for line in file]

with open('data/sybil_wallets.txt', 'r', encoding='utf-8-sig') as file:
    sybil_wallets = {line.strip() for line in file}

with open('data/result_sybil_wallets.txt', 'w', encoding='utf-8-sig') as result_file:
    for address in addresses:
        if address in sybil_wallets:
            result_file.write(address + '\n')
