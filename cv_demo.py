import cv2  # Importing the OpenCV library

def load_image(image_path):
    """Load an image from a file path."""
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Image not found at {image_path}")
        exit()
    return image

def convert_to_grayscale(image):
    """Convert an image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def detect_edges(image, low_threshold=50, high_threshold=150):
    """Detect edges in an image using the Canny algorithm."""
    return cv2.Canny(image, low_threshold, high_threshold)

def display_images(images, titles):
    """Display a list of images with titles."""
    for i, (image, title) in enumerate(zip(images, titles)):
        cv2.imshow(title, image)
    cv2.waitKey(0)  # Wait for a key press to close the images
    cv2.destroyAllWindows()

def main():
    # Path to the image file
    image_path = 'path_to_your_image.jpg'

    # Load the image
    image = load_image(image_path)

    # Convert image to grayscale
    gray_image = convert_to_grayscale(image)

    # Detect edges
    edges = detect_edges(gray_image)

    # Display the images
    display_images([image, gray_image, edges], ['Original Image', 'Grayscale Image', 'Edges'])

if __name__ == "__main__":
    main()
