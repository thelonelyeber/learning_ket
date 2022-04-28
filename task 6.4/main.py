from class_task import BankClient, ShopClient

client = BankClient('Ivanov', 1234567, 2000000, 2022, 12, 31)
client.put(50000)
client.get(20000)
client.person_display()
client.percent()
client.put(client.bonus())
print(f'Сумма вклада: {client.summa_bank}')
'''==========================================='''

client1 = ShopClient()
client1.new_buy()
client1.summa_buy -= client1.bonus()
print(f'К оплате: {client1.summa_buy}')
client1.new_buy()
client1.summa_buy -= client1.bonus()
print(f'К оплате: {client1.summa_buy}')
