import face_recognition
from PIL import Image, ImageDraw

def face_rec():
    hardy_face_img = face_recognition.load_image_file('img/gosha_1.jpg')
    hardy_face_location = face_recognition.face_locations(hardy_face_img)

    s_saninoy_face_img = face_recognition.load_image_file('img/gosha_3.jpg')
    s_saninoy_face_location = face_recognition.face_locations(s_saninoy_face_img)

    print(hardy_face_location)
    print(s_saninoy_face_location)
    print(f'Found {len(hardy_face_location)} face(s) in this image')
    print(f'Found {len(s_saninoy_face_location)} face(s) in this image')

    pil_img1 = Image.fromarray(hardy_face_img)
    draw1 =  ImageDraw.Draw(pil_img1)

    for(top, right, bottom, left) in hardy_face_location:
        draw1.rectangle(((left, top), (right, bottom)), outline=(255,255,0), width=4)

    del draw1
    pil_img1.save('img/new_gosha_1.jpg')


    pil_img2 = Image.fromarray(s_saninoy_face_img)
    draw2 = ImageDraw.Draw(pil_img2)

    for (top, right, bottom, left) in s_saninoy_face_location:
        draw2.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4)

    del draw2
    pil_img2.save('img/new_gosha_3.jpg')

def extracting_faces(img_path):
    count = 0
    faces = face_recognition.load_image_file(img_path)
    faces_locations = face_recognition.face_locations(faces)

    for face_location in faces_locations:
        top, right, bottom, left = face_location

        face_img = faces[top:bottom, left:right]
        pil_img = Image.fromarray(face_img)
        pil_img.save(f'img/{count}_face_img.jpg')
        count += 1

    return f'Found {count} face(s) in this photo'

def compare_faces(img1_path, img2_path):
    img1 = face_recognition.load_image_file(img1_path)
    img1_encodings = face_recognition.face_encodings(img1)[0]
    #print(img1_encodings)

    img2 = face_recognition.load_image_file(img2_path)
    img2_encodings = face_recognition.face_encodings(img2)[0]

    result = face_recognition.compare_faces([img1_encodings], img2_encodings)
    # print(result)

    if result[0]:
        print("Welcome to the club, buddy!")
    else:
        print("Not today: anal penitration")
def main():
    face_rec()
    print(extracting_faces('img/group.jpg'))
    compare_faces('img/gosha_1.jpg', 'img/s_saninoy.jpg')

if __name__ == '__main__':
     main()
