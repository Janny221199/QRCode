import pyqrcode
import png # pip3 install pypng
import re
import os


OUTPUT_FOLDER = 'QRCodes'


def print_header():
    print('------------------QR-Code------------------')
    print('feel free to report an issue:')
    print('https://github.com/Janny221199/QRCode')
    print('-------------------------------------------')


def ensure_output_folder_exists():
    if not os.path.isdir(OUTPUT_FOLDER):
        print(f'Creating Output Folder: {OUTPUT_FOLDER}')
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def create_qrcode(url, name, color='#000000', background_color='#FFFFFF'):
    ensure_output_folder_exists()
    qrcode = pyqrcode.create(url)
    qrcode.svg(f'{OUTPUT_FOLDER}/{name}.svg', module_color=f'{color}', background=f'{background_color}', scale=8)
    qrcode.eps(f'{OUTPUT_FOLDER}/{name}.eps', module_color=f'{color}', background=f'{background_color}', scale=2)
    qrcode.png(f'{OUTPUT_FOLDER}/{name}.png', module_color=f'{color}', background=f'{background_color}', scale=6)
    # qrcode.show()
    # print(qrcode.terminal(quiet_zone=1))


def get_url():
    url = input('URL: ')
    regex = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
    if not url or not re.match(regex, url):
        print('Please enter a valid URL!')
        return get_url()
    return url
    
    
def get_name():
    name = input('Name: ')
    regex = r'^[a-zA-Z0-9]*$'
    if not name or not re.match(regex, name):
        print('Please enter a valid name! (without special characters')
        return get_name()
    return name
    
    
def get_color():
    color = input('Please enter a hex color code: ')
    regex = r'^#(?:[0-9a-fA-F]{3}){1,2}$'
    if not color or not re.match(regex, color):
        print('Please enter a valid hex color code! (e.g.: #FFFFFF)')
        return get_color()
    return color
    
    
if __name__ == '__main__':
    print_header()
    url = get_url()
    name = get_name()
    if input('Do you wanna specify the color and background color? (Y/N) ').upper() == 'Y':
        print('Color:')
        color = get_color()
        print('Background Color:')
        background_color = get_color()
        create_qrcode(url, name, color, background_color)
    else:
        create_qrcode(url, name)
    # create_qrcode('https://github.com/Janny221199', 'Github_Janny221199')
