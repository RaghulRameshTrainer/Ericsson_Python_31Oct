from bank import Account

acc=Account('Raghul','Ramesh','1234 5567 2121',10000)
print("Currnet Balance:",acc.getBalance())
print(f"Credentials: \nUser ID:{acc.userid}\nPassword:{acc.password}")
acc.setBalance(190000)
print("Currnet Balance:",acc.getBalance())
