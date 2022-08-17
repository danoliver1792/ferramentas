import win32com.client as win32 #biblioteca PyWin32

outlook = win32.Dispatch('outlook.application')

email = outlook.CreateItem(0)

email.To = 'danrlei.jesus@hotmail.com'
email.Subject = 'Teste com Python'
email.HTMLBody = '''
<p>Olá, mundo!</p>'''

email.send()

print('e-mail enviado com sucesso!')
