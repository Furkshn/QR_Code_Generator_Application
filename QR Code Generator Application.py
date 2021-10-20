import qrcode
import cv2
import time



# QR Code Generator


def generate_qrcode():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4)

    data_for_qrcode = input("Please Attach Data into QR Code:")   # Generating QR Code
    qr.add_data(data_for_qrcode)
    qr.make(fit=True)

    qrcode_img = qr.make_image(fill_color = "black", back_color ="white")   # Making & Saving QR Code Image
    qrcode_file_name = input("Please Name Qr Code File:")
    qrcode_img.save(f"{qrcode_file_name}.png")
    print(".")
    time.sleep(0.3)
    print("..")
    time.sleep(0.3)
    print("...")
    print("QR Code Created !")




    image = cv2.imread(f"{qrcode_file_name}.png")   # Reading QR Code using OpenVC

    cv2.imshow(f"{qrcode_file_name}", image)
    key = cv2.waitKey(0) & 0xFF

    if key == ord("s"):       # Press "s" to close window

        cv2.destroyAllWindows()



generate_qrcode()