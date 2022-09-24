import wmi

#carregando informações...
c = wmi.WMI()
system = c.win32_ComputerSystem()[0]
#mostrando os resultados...
print(f'Marca: {system.Manufacturer}')
print(f'Modelo: {system.Model}')
print(f'Nome: {system.Name}')
print(f'Quantidade CPU: {system.NumberOfProcessors}')
print(f'Arquitetura: {system.SystemType}')
print(f'Familia: {system.SystemFamily}')
