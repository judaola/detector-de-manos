import cv2
import mediapipe as mp



# #Programa inicial que solo lee la imagen---------------------------------------------------------------------------------------------------------
# mp_drawing = mp.solutions.drawing_utils  #se usa la biblioteca mediapipe cargandolo con el modulo drawing_utils el cual se usa para hacer anotaciones graficas en las detecciones hechas en mediapipe
# mp_hands = mp.solutions.hands  #Se usa la biblioteca mediapipe cargando el modulo solutions.hands el cual accede a la clase hands y utiliza para detectar imagenes o el flujo de un video

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



# #Programa que lee la imagen y imprime las ubicaciones de cada mano detectada con la probabilidad de que sea verdadero "Score"-------------------------
# mp_drawing = mp.solutions.drawing_utils  #se usa la biblioteca mediapipe cargandolo con el modulo drawing_utils el cual se usa para hacer anotaciones graficas en las detecciones hechas en mediapipe
# mp_hands = mp.solutions.hands  #Se usa la biblioteca mediapipe cargando el modulo solutions.hands el cual accede a la clase hands y utiliza para detectar imagenes o el flujo de un video

# with mp_hands.Hands(
#     static_image_mode=True, #Es verdadero ya que estamos trabajando con una imagen estatica
#     max_num_hands=2,  #Maximo numero de manos por detectar
#     min_detection_confidence=0.5) as hands:  #minima deteccion de confianza por defecto 0.5

#     image = cv2.imread("imagen.jpg") #Cargamos la imagen para leerla con opencv
#     height, width, _ = image.shape
#     image = cv2.flip(image, 1)  #Giramos la imagen ya que esta alrevez de abajo a arriba

#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #Convertimos la imagen de formato BGR (Blue-Green-Red) a formato RGB (Red-Green-Blue).

#     results = hands.process(image_rgb) #guardamos en results la imagen transformada en formato RGB

#     #HANDEDNESS
#     print("Handedness:", results.multi_handedness ) #Imprimimos en la terminal la ubicacion de las manos detectadas en la imagen
    
# cv2.imshow("Image", image) #muestra la imagen en consola
# cv2.waitKey(0)  #Esperamos a que el usuario presione una tecla (0 indica espera indefinida)
# cv2.destroyAllwindows()  #Cierra la ventana al presionar tecla 'ESC'
# ##----------------------------------------------------------------------------------------------------------------------------------------------------



# #Programa que lee la imagen y detecta cada uno de los 21 puntos y conexiones en la mano usando la opcion predeterminada de mediapipe--------------------------------
# mp_drawing = mp.solutions.drawing_utils  #se usa la biblioteca mediapipe cargandolo con el modulo drawing_utils el cual se usa para hacer anotaciones graficas en las detecciones hechas en mediapipe
# mp_hands = mp.solutions.hands  #Se usa la biblioteca mediapipe cargando el modulo solutions.hands el cual accede a la clase hands y utiliza para detectar imagenes o el flujo de un video

# with mp_hands.Hands(
#     static_image_mode=True, #Es verdadero ya que estamos trabajando con una imagen estatica
#     max_num_hands=2,  #Maximo numero de manos por detectar
#     min_detection_confidence=0.5) as hands:  #minima deteccion de confianza por defecto 0.5

#     image = cv2.imread("imagen.jpg") #Cargamos la imagen para leerla con opencv
#     height, width, _ = image.shape
#     image = cv2.flip(image, 1)  #Giramos la imagen ya que esta alrevez de abajo a arriba

#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #Convertimos la imagen de formato BGR (Blue-Green-Red) a formato RGB (Red-Green-Blue).

#     results = hands.process(image_rgb) #guardamos en results la imagen transformada en formato RGB

#     #HANDEDNESS
#     print("Handedness:", results.multi_handedness ) #Imprimimos en la terminal la ubicacion de las manos detectadas en la imagen

#     if results.multi_hand_landmarks is not None:
#         #Dibujando puntos y sus conexiones con mediapipe
#         for hand_landmarks in results.multi_hand_landmarks:
            
#             mp_drawing.draw_landmarks( 
#             #Muestra las conexiones de color blanco y los puntos de color rojo
#             image, hand_landmarks, mp_hands.HAND_CONNECTIONS,

#             #Codigo para cambiar tamaño, grosor y color
#             # color define el color en RGB, thickness define el grosor de la linea tanto circular como en una direccion en especifico es decir de izquierda a derecha o parecidos
#             mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=4, circle_radius=5), 
#             mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=4))
#     image = cv2.flip(image,1)
# cv2.imshow("Image", image) #muestra la imagen en consola
# cv2.waitKey(0)  #Esperamos a que el usuario presione una tecla (0 indica espera indefinida)
# cv2.destroyAllwindows()  #Cierra la ventana al presionar tecla 'ESC'
# #----------------------------------------------------------------------------------------------------------------------------------------------------



# ##Programa que lee los puntos especificos de la mano los cuales son (4, 8, 12, 16, 20) uno por uno----------------------------------------------------------------
# mp_drawing = mp.solutions.drawing_utils  #se usa la biblioteca mediapipe cargandolo con el modulo drawing_utils el cual se usa para hacer anotaciones graficas en las detecciones hechas en mediapipe
# mp_hands = mp.solutions.hands  #Se usa la biblioteca mediapipe cargando el modulo solutions.hands el cual accede a la clase hands y utiliza para detectar imagenes o el flujo de un video

# with mp_hands.Hands(
#     static_image_mode=True, #Es verdadero ya que estamos trabajando con una imagen estatica
#     max_num_hands=2,  #Maximo numero de manos por detectar
#     min_detection_confidence=0.5) as hands:  #minima deteccion de confianza por defecto 0.5

#     image = cv2.imread("imagen.jpg") #Cargamos la imagen para leerla con opencv
#     height, width, _ = image.shape
#     image = cv2.flip(image, 1)  #Giramos la imagen ya que esta alrevez de abajo a arriba

#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #Convertimos la imagen de formato BGR (Blue-Green-Red) a formato RGB (Red-Green-Blue).

#     results = hands.process(image_rgb) #guardamos en results la imagen transformada en formato RGB

#     #HANDEDNESS
#     print("Handedness:", results.multi_handedness ) #Imprimimos en la terminal la ubicacion de las manos detectadas en la imagen

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

#               #imprime la coordenada en entero de cada uno de los puntos especificos a encontrar
#             print(x1, x2, x3, x4, x5, y1, y2, y3, y4, y5)

#             cv2.circle(image, (x1, y1), 3, (255, 0, 0), 3) #crea un circulo al encontrar la coordenada con el siguiente formato grosor/color RGB/ tamaño
#             cv2.circle(image, (x2, y2), 3, (255, 0, 0), 3) #crea un circulo al encontrar la coordenada con el siguiente formato grosor/color RGB/ tamaño
#             cv2.circle(image, (x3, y3), 3, (255, 0, 0), 3) #crea un circulo al encontrar la coordenada con el siguiente formato grosor/color RGB/ tamaño
#             cv2.circle(image, (x4, y4), 3, (255, 0, 0), 3) #crea un circulo al encontrar la coordenada con el siguiente formato grosor/color RGB/ tamaño
#             cv2.circle(image, (x5, y5), 3, (255, 0, 0), 3) #crea un circulo al encontrar la coordenada con el siguiente formato grosor/color RGB/ tamaño
            
# cv2.imshow("Image", image) #muestra la imagen en consola
# cv2.waitKey(0)  #Esperamos a que el usuario presione una tecla (0 indica espera indefinida)
# cv2.destroyAllwindows()  #Cierra la ventana al presionar tecla 'ESC'
# #----------------------------------------------------------------------------------------------------------------------------------------------------



# Programa que lee los puntos especificos de la mano los cuales son (4, 8, 12, 16, 20) mediante una lista, mas reducido en codigo---------------------
# mp_drawing = mp.solutions.drawing_utils  #se usa la biblioteca mediapipe cargandolo con el modulo drawing_utils el cual se usa para hacer anotaciones graficas en las detecciones hechas en mediapipe
# mp_hands = mp.solutions.hands  #Se usa la biblioteca mediapipe cargando el modulo solutions.hands el cual accede a la clase hands y utiliza para detectar imagenes o el flujo de un video

# with mp_hands.Hands(
#     static_image_mode=True, #Es verdadero ya que estamos trabajando con una imagen estatica
#     max_num_hands=2,  #Maximo numero de manos por detectar
#     min_detection_confidence=0.5) as hands:  #minima deteccion de confianza por defecto 0.5

#     image = cv2.imread("imagen.jpg") #Cargamos la imagen para leerla con opencv
#     height, width, _ = image.shape
#     image = cv2.flip(image, 1)  #Giramos la imagen ya que esta alrevez de abajo a arriba

#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #Convertimos la imagen de formato BGR (Blue-Green-Red) a formato RGB (Red-Green-Blue).

#     results = hands.process(image_rgb) #guardamos en results la imagen transformada en formato RGB

#     #HANDEDNESS
#     print("Handedness:", results.multi_handedness ) #Imprimimos en la terminal la ubicacion de las manos detectadas en la imagen

#     if results.multi_hand_landmarks is not None:
#         #Accediendo a puntos claves de acuerdo al nombre que tengan segun el archivo 'puntos de referencia de las manos'
#         index = [ 4, 8, 12, 16, 20]  #Creamos una lista con los numeros de coordenadas las cuales nos serviran para decirle donde debe dibujar los puntos
#         for hand_landmarks in results.multi_hand_landmarks: #Creamos un bucle for q recorra toda las coordenadas de las manos
#             for (i, points) in enumerate(hand_landmarks.landmark):  #Guardamos en i las coordenadas encontradas y hacen el bucle for para hallar los ya puestos en la lista ya creado
#                 if i in index:  #Ejecuta el if el cual se traduce "si en la lista index ahi alguna de las coordenadas guardadas en i marcar el punto"
#                     x = int(points.x * width) #Convertimos en entero las coordenadas x encontradas cooncidentes
#                     y = int(points.y * height)  #Convertimos en entero las coordenadas y encontradas coocidentes
#                     cv2.circle(image, (x, y), 3, (255, 0, 0), 3) #crea un circulo en la cooordenada al encontrar el punto referente con el siguiente formato grosor/color RGB/ tamaño
            
# cv2.imshow("Image", image) #muestra la imagen en consola
# cv2.waitKey(0)  #Esperamos a que el usuario presione una tecla (0 indica espera indefinida)
# cv2.destroyAllwindows()  #Cierra la ventana al presionar tecla 'ESC'
# ##----------------------------------------------------------------------------------------------------------------------------------------------------



##Programa que lee la camara y detecta en tiempo real--------------------------------
# mp_drawing = mp.solutions.drawing_utils  #se usa la biblioteca mediapipe cargandolo con el modulo drawing_utils el cual se usa para hacer anotaciones graficas en las detecciones hechas en mediapipe
# mp_hands = mp.solutions.hands  #Se usa la biblioteca mediapipe cargando el modulo solutions.hands el cual accede a la clase hands y utiliza para detectar imagenes o el flujo de un video

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# with mp_hands.Hands(
#     static_image_mode = False,  #Es falso ya que estamos trabajando con un video de la camara en tiempo real
#     max_num_hands=2,  #Maximo numero de manos por detectar
#     min_detection_confidence=0.5) as hands:  #minima deteccion de confianza por defecto 0.5

#     while True: #Esto inicia un bucle infinito que continuará hasta que se rompa explícitamente con un break.
#         ret, frame = cap.read()  #Lee un fotograma del video de la cámara utilizando el objeto
#         if ret == False:  #Si no se lee el fotograma se ejecuta el break y no muestra ningun punto en pantalla
#             break
        
#         height, width, _ = frame.shape  #Obtiene el alto y el ancho del fotograma capturado en las variables height y width.
#         frame = cv2.flip(frame,1)  #Voltea el fotograma horizontalmente. Esto puede hacerse para obtener un espejo de la imagen si se muestra en una ventana.
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  #Convierte el fotograma del espacio de color BGR (Blue-Green-Red) al espacio de color RGB (Red-Green-Blue). MediaPipe trabaja con imágenes en formato RGB.

#         results = hands.process(frame_rgb)  #Aquí se utiliza la instancia del modelo de detección de manos (hands) para procesar el fotograma convertido a RGB. Esto devuelve los resultados de la detección y el seguimiento de manos, 
#                                             #incluyendo la ubicación y los puntos clave de las manos detectadas.

#         if results.multi_hand_landmarks is not None:  #Comprueba si se detectaron manos en el fotograma actual. Si es así, continúa con el siguiente bloque de código.
#             for hand_landmarks in results.multi_hand_landmarks:  # Itera sobre las manos detectadas en el fotograma. El objeto results.multi_hand_landmarks contiene una lista de landmarks (puntos clave) para cada mano detectada.
#                 mp_drawing.draw_landmarks(  
#                     frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)  # Dibuja los landmarks y conexiones de la mano en el fotograma frame utilizando la función draw_landmarks del módulo drawing_utils de MediaPipe (mp_drawing). Esto mostrará los puntos clave de las manos y las conexiones entre ellos como líneas.
                
#         cv2.imshow("Frame", frame)  #Muestra el fotograma con las anotaciones gráficas en una ventana con el título "Frame". Esto mostrará el video en tiempo real con las manos detectadas y las anotaciones gráficas dibujadas.
#         if cv2.waitKey(1) & 0xFF == 27:  #Espera una pequeña cantidad de tiempo (1 milisegundo) y verifica si se ha presionado la tecla "Esc" (código 27 en la tabla ASCII) para salir del bucle. Si se presiona "Esc", el bucle se romperá y la captura de video se detendrá.
#             break
        
# cap.release()  #Libera el objeto cap, lo que cierra la conexión con la fuente de video (en este caso, la cámara).
# cv2.destroyAllwindows()  #Cierra la ventana al presionar tecla 'ESC'
# # ##----------------------------------------------------------------------------------------------------------------------------------------------------





































###Programa en coonstruccion-----------------------------------------------##





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