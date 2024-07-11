import cv2
import datetime

def capture_photo(employee_id):
    # Abre a webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Não foi possível acessar a webcam")

    ret, frame = cap.read()
    if not ret:
        raise Exception("Não foi possível capturar a foto")

    # Define o caminho para salvar a foto
    photo_path = f"screenshots/{employee_id}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
    cv2.imwrite(photo_path, frame)
    cap.release()
    cv2.destroyAllWindows()

    return photo_path
