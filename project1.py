###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("winter")

q1 = codesters.Square(100, 100, 200, 'blue')
q2 = codesters.Square(-100, 100, 200, 'LimeGreen')
q3 = codesters.Square(-100, -100, 200, 'black')
q4 = codesters.Square(100,-100,200, 'AliceBlue')

s1 = codesters.Sprite("cat", 100, 100)
s1.set_size(0.3)
s2 = codesters.Sprite("xbox", -100, -100)
s2.set_size(0.09)
s3 = codesters.Sprite("soccerball",100, -100)
s3.set_size(3)
s4 = codesters.Sprite("bikebetter", -100, 100)
s4.set_size(0.09)

message1 = codesters.Text("James Emery",0,220,"green")
message2 = codesters.Text("My Crest",0,-220,"green")