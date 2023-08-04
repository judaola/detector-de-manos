import cv2
import mediapipe as mp



# #Programa inicial que solo lee la imagen---------------------------------------------------------------------------------------------------------
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands

# with mp_hands.Hands(
#     static_image_mode=True, #Es verdadero ya que estamos trabajando con una imagen estatica
#     max_num_hands=2,  #Maximo numero de manos por detectar
#     min_detection_confidence=0.5) as hands:  #minima deteccion de confianza por defecto 0.5

#     image = cv2.imread("imagen.jpg") #Cargamos la imagen para leerla con opencv
#     height, width, _ = image.shape
#     image = cv2.flip(image, 1)  #Giramos la imagen ya que esta alrevez de abajo a arriba

  

# cv2.imshow("Image", image) #muestra la imagen en consola
# cv2.waitKey(0)  #Esperamos a que el usuario presione una tecla (0 indica espera indefinida)
# cv2.destroyAllwindows()  #Cierra la ventana al presionar tecla 'ESC'
# #-----------------------------------------------------------------------------------------------------------------------------------------------------



##Programa que lee la imagen y imprime las ubicaciones de cada mano detectada con la probabilidad de que sea verdadero "Score"-------------------------
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands

# with mp_hands.Hands(
#     static_image_mode=True,
#     max_num_hands=2,
#     min_detection_confidence=0.5) as hands:

#     image = cv2.imread("imagen.jpg")
#     height, width, _ = image.shape
#     image = cv2.flip(image, 1)

#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     results = hands.process(image_rgb)

#     #HANDEDNESS
#     print("Handedness:", results.multi_handedness )
    
#     image = cv2.flip(image,1)
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllwindows()
# ##----------------------------------------------------------------------------------------------------------------------------------------------------



##Programa que lee la imagen y detecta cada uno de los 21 puntos y conexiones en la mano usando la opcion predeterminada de mediapipe--------------------------------
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands

# with mp_hands.Hands(
#     static_image_mode=True,
#     max_num_hands=2,
#     min_detection_confidence=0.5) as hands:

#     image = cv2.imread("imagen.jpg")
#     height, width, _ = image.shape
#     image = cv2.flip(image, 1)

#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     results = hands.process(image_rgb)

#     #HANDEDNESS
#     print("Handedness:", results.multi_handedness )

#     if results.multi_hand_landmarks is not None:
#         #Dibujando puntos y sus conexiones con mediapipe
#         for hand_landmarks in results.multi_hand_landmarks:
            
#             mp_drawing.draw_landmarks( 
#             #Muestra las conexiones de color blanco y los puntos de color rojo
#             # image, hand_landmarks, mp_hands.HAND_CONNECTIONS,

#             #Codigo para cambiar tamaño, grosor y color
#             # color define el color en RGB, thickness define el grosor de la linea tanto circular como en una direccion en especifico es decir de izquierda a derecha o parecidos
#             mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=4, circle_radius=5), 
#             mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=4)
            
#     image = cv2.flip(image,1)
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllwindows()
##----------------------------------------------------------------------------------------------------------------------------------------------------



# ##Programa que lee los puntos especificos de la mano los cuales son (4, 8, 12, 16, 20) uno por uno----------------------------------------------------------------
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands

# with mp_hands.Hands(
#     static_image_mode=True,
#     max_num_hands=1,
#     min_detection_confidence=0.5) as hands:

#     image = cv2.imread("imagen.jpg")
#     height, width, _ = image.shape
#     image = cv2.flip(image, 1)

#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     results = hands.process(image_rgb)

#     #HANDEDNESS
#     print("Handedness:", results.multi_handedness ) 

#     if results.multi_hand_landmarks is not None:
#         #Accediendo a puntos claves de acuerdo al nombre que tengan segun el archivo 'puntos de referencia de las manos'
#         for hand_landmarks in results.multi_hand_landmarks:
#             #Pulgar
#             x1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * width) #colocando int volvemos la coordenada en entero
#             y1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * height)
#             #Indice
#             x2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * width)
#             y2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height)
#             #Dedo medio
#             x3 = int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * width)
#             y3 = int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * height)
#             #Anular
#             x4 = int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x * width)
#             y4 = int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * height)
#             #Meñique
#             x5 = int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * width)
#             y5 = int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * height)

#             print(x1, x2, x3, x4, x5, y1, y2, y3, y4, y5)

#             cv2.circle(image, (x1, y1), 3, (255, 0, 0), 3)
#             cv2.circle(image, (x2, y2), 3, (255, 0, 0), 3)
#             cv2.circle(image, (x3, y3), 3, (255, 0, 0), 3)
#             cv2.circle(image, (x4, y4), 3, (255, 0, 0), 3)
#             cv2.circle(image, (x5, y5), 3, (255, 0, 0), 3)
            
#     image = cv2.flip(image,1)
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllwindows()
##----------------------------------------------------------------------------------------------------------------------------------------------------



# Programa que lee los puntos especificos de la mano los cuales son (4, 8, 12, 16, 20) mediante una lista, mas reducido en codigo---------------------
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands

# with mp_hands.Hands(
#     static_image_mode=True,
#     max_num_hands=2,
#     min_detection_confidence=0.5) as hands:

#     image = cv2.imread("imagen.jpg")
#     height, width, _ = image.shape
#     image = cv2.flip(image, 1)

#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     results = hands.process(image_rgb)

#     #HANDEDNESS
#     print("Handedness:", results.multi_handedness ) 

#     if results.multi_hand_landmarks is not None:
#         #Accediendo a puntos claves de acuerdo al nombre que tengan segun el archivo 'puntos de referencia de las manos'
#         index = [ 4, 8, 12, 16, 20]
#         for hand_landmarks in results.multi_hand_landmarks:
#             for (i, points) in enumerate(hand_landmarks.landmark):
#                 if i in index:
#                     x = int(points.x * width)
#                     y = int(points.y * height)
#                     cv2.circle(image, (x, y), 3, (255, 0, 0), 3)
            
#     image = cv2.flip(image,1)
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllwindows()
# ##----------------------------------------------------------------------------------------------------------------------------------------------------



# ##Programa que lee la camara y detecta en tiempo real--------------------------------
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# with mp_hands.Hands(
#     static_image_mode = False,
#     max_num_hands=2,
#     min_detection_confidence=0.5) as hands:

#     while True:
#         ret, frame = cap.read()
#         if ret == False:
#             break
        
#         height, width, _ = frame.shape
#         frame = cv2.flip(frame,1)
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         results = hands.process(frame_rgb)

#         if results.multi_hand_landmarks is not None:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 mp_drawing.draw_landmarks(
#                     frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
#         cv2.imshow("Frame", frame)
#         if cv2.waitKey(1) & 0xFF == 27:
#             break
        
# cap.release()
# cv2.destroyAllWindows() 
# ##----------------------------------------------------------------------------------------------------------------------------------------------------





# ##Programa --------------------------------
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands

# cap = cv2.VideoCapture('video')

# while True:
#     ret, frame = cap.read()
#     if ret == False: break
      
#     cv2.imshow('frame', frame)

#     k = cv2.waitKey(70) & 0xFF
#     if k == 27:
#         break
    



        
# cap.release()
# cv2.destroyAllWindows() 
# ##----------------------------------------------------------------------------------------------------------------------------------------------------