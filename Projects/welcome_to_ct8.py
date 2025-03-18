
###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("winter")
mySprite = codesters.Sprite("fish")
mySprite.say("Good job eating me!")
mySprite = codesters.Sprite("baseball",-230,230)
mySprite = codesters.Sprite("fight",20,50)
print("\n\nWhen you have found the FISH, click here, then use CTRL C to end the program\n\n")