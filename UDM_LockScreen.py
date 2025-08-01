from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDIconButton
from kivy.clock import Clock

from UDM_GSM import GSM


class LockScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        iconList = ["account-lock","bank","bird","airport","apple","bone","timer-sand-full","account-cowboy-hat","city","mushroom",
                    "bridge","leaf-maple","fence","rabbit","battery","shark-fin","football","fruit-watermelon","gas-station","pizza",
                    "leaf","snowflake","web-clock","library","microsoft-xbox","jellyfish","android","ice-cream","island","home",
                    "dog","pretzel","timer","flower","lightning-bolt","bug","fire-alert","minecraft","stadium","store",
                    "nintendo-wii","airplane-clock","volcano","castle","duck","terrain","horse","google-downasaur","cow","carrot",
                    "fishbowl","beehive-outline","nintendo-switch","alarm","fish","spider","bow-arrow","baguette","theater","forest",
                    "food-hot-dog","check","arrow-projectile","docker","turkey","tortoise","alphabet-aurebesh","car-clock","lock-clock","bomb",
                    "boomerang","cactus","candy-outline","controller","chess-rook","knife-military","react","medal","egg","pac-man",
                    "koala","linux","dolphin","poker-chip","puzzle","one-up","shark","sack","owl","panda",
                    "unicorn","sword","hamburger","spear","controller-classic","language-swift","space-invaders","treasure-chest","meteor","cylinder"]

        grid = self.ids.LockScreenGrid

        for i in iconList:
            if i == "alphabet-aurebesh":
                btn = MDIconButton (
                icon = i,
                on_release= lambda btn: self.rightBtn()
                )
                grid.add_widget(btn)
            else:  
                btn = MDIconButton (
                    icon = i,
                    on_release= lambda btn: self.wrongBtn()
                )
                grid.add_widget(btn)

    def wrongBtn(self):
        GSM().switchScreen("timeOut")
    
    def rightBtn(self):
        GSM().switchScreen("startScreen")