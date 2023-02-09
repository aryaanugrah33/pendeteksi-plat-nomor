import glob
import cv2
import easyocr

def read_image():
    folder = glob.glob("C:/Users/aryat/OneDrive/Pictures/New folder (3)/DeteksiPlatNomor-main/data/*jpg") 
    images = []

    for file in folder:
        images.append(file)

    count = 1

    for image in images:
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        reader = easyocr.Reader(["en"])
        result = reader.readtext(gray)
        for (bbox, text, prob) in result:
            print(count, "Plat Nomor:", text, "| "
            "persentase:", prob)
            count += 1

        cv2.imshow("Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()