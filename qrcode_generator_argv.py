import sys
import pyqrcode

path_dir = sys.argv[1]
string_data = sys.argv[2]
delimiter = sys.argv[3]
scale = sys.argv[4]

print(f'Gerando QRCodes no endereço {path_dir}')

data_list = string_data.split(delimiter)

for data in data_list:
    path_arq = f'{path_dir}\\qrcode_{data_list.index(data)}.png'
    qrcode = pyqrcode.QRCode(data)

    if data == '':
        pass

    else:
        try:
            qrcode.png(path_arq, scale = scale)
            print(f'..............arquivo {path_arq} criado!')
        except:
            print(f'erro durante a tentativa de salvar o arquivo {path_arq}')

print('QRCodes gerados!')
