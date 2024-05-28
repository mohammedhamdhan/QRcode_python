import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, SquareModuleDrawer, GappedSquareModuleDrawer, CircleModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import ImageColor

website_link = input("Input your website link to create a QR code: ")

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(website_link)
qr.make()

def qrgen(style, fill_color):
    if style == '1':
        module_drawer = SquareModuleDrawer()
    elif style == '2':
        module_drawer = GappedSquareModuleDrawer()
    elif style == '3':
        module_drawer = CircleModuleDrawer()
    elif style == '4':
        module_drawer = RoundedModuleDrawer()
    else:
        print("Error: wrong number")
        return
    
    # Ensure the fill color is in RGB format
    try:
        front_color = ImageColor.getrgb(fill_color)
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    color_mask = SolidFillColorMask(back_color=(255, 255, 255), front_color=front_color)
    
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=module_drawer, color_mask=color_mask)
    img.save('generated_img.png')
    print("QR code generated successfully")

user_input = input("Enter '1' for Standard Square Module, '2' for Gapped Square Module, '3' for Circle Module or '4' for Rounded module, followed by a comma and the desired color (e.g., 'red' or '#FF0000'): ")

try:
    style, fill_color = user_input.split(',')
    fill_color = fill_color.strip()  # Remove any leading/trailing spaces
    qrgen(style, fill_color)
except ValueError:
    print("Error: Please provide both style number and color.")
except Exception as e:
    print(f"An error occurred: {e}")
