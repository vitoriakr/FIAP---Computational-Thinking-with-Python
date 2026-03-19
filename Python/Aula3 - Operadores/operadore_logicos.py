stored_user = 'admin'
stored_password = '1234'
user = input("Digite o  login: ")
password = input("Digite o senha: ")

is_acess_granted = (stored_user == user ) and  (stored_password == password)
print(f' Acesso está: {is_acess_granted}')