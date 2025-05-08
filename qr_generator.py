import qrcode
import qrcode.image.svg # Import the SVG image factory

def generate_qr_code(data, filename):
    """Generates a QR code from the given data and saves it to a file."""
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            image_factory=qrcode.image.svg.SvgPathImage  # Use SVG image factory
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="#1490e7", back_color="white")
        img.save(filename)
        print(f"QR code saved as {filename} successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    data_to_encode = input("Enter the data or URL for the QR code: ")
    output_filename = input("Enter the desired filename for the QR code image (e.g., my_qr.svg): ")

    if not output_filename.lower().endswith(('.svg')):
        # If it's not explicitly an svg, check for other common image types to avoid accidental overwrite with wrong extension
        if output_filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            print(f"Warning: Outputting as SVG, but filename '{output_filename}' has a raster image extension. Consider using '.svg'.")
            # Keep user's extension if they provided a different one, but SVG will be the format
        else:
            output_filename += '.svg' # Default to .svg if no extension or a non-image extension is provided
            print(f"No valid SVG extension provided, defaulting to {output_filename}")

    generate_qr_code(data_to_encode, output_filename)
