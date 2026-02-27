from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics.texture import Texture

import cv2
import mediapipe as mp

class CamApp(App):
    def build(self):
        self.img = Image()
        self.btn = Button(text="Tomar Foto", size_hint=(1, 0.1))
        self.btn.bind(on_press=self.take_photo)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.img)
        layout.add_widget(self.btn)

        # MediaPipe
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False,
                                         max_num_hands=1,
                                         min_detection_confidence=0.5)

        self.cap = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0/30.0)

        self.frame = None

        return layout

    def update(self, dt):
        ret, frame = self.cap.read()
        if not ret:
            return

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                h, w, _ = frame.shape
                x = int(hand_landmarks.landmark[4].x * w)
                y = int(hand_landmarks.landmark[4].y * h)
                # Dibujar círculo rojo en la punta del pulgar
                cv2.circle(frame, (x, y), 15, (0, 0, 255), cv2.FILLED)

        self.frame = frame  # guardamos frame actual para foto

        # Convertir a textura para Kivy
        buf = cv2.flip(frame, 0).tobytes()
        tex = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        tex.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.img.texture = tex

    def take_photo(self, instance):
        if self.frame is not None:
            cv2.imwrite('foto_pulgar_kivy.jpg', self.frame)
            print("¡Foto tomada y guardada como foto_pulgar_kivy.jpg!")

    def on_stop(self):
        self.cap.release()

if __name__ == '__main__':
    CamApp().run()


