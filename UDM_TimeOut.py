from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

from UDM_GSM import GSM


class TimeOut(Screen):
    def on_enter(self):
        self.countDown = 10
        self.countdown_event = Clock.schedule_interval(self.updateCountdown, 1)

    def updateCountdown(self, dt):
        if self.countDown > 0:
            mins = self.countDown // 60
            sec = self.countDown % 60

            self.ids.CountDown.text = f"{mins:02}:{sec:02}"
            self.countDown -= 1
        else:
            self.ids.CountDown.text = "00:00"
            self.countdown_event.cancel()
            GSM().switchScreen("lockScreen")

    def on_leave(self):
        if hasattr(self, 'countdown_event') and self.countdown_event:
            self.countdown_event.cancel()
            self.countdown_event = None