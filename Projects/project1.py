###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("summer")
q1 = codesters.Square(100, 100, 200, 'pink')
q2 = codesters.Square(-100, 100, 200, 'misty rose')
q3 = codesters.Square(-100, -100, 200, 'white')
q4 = codesters.Square(100, -100, 200, 'powder blue')


s1 = codesters.Sprite("malaya_sarani", 100, 100)
s1.set_size(0.2)
s2 = codesters.Sprite("coolsun", -100, -100)
s2.set_size(0.5)
s3 = codesters.Sprite("seattle", 100, -100)
s3.set_size(0.1)
s4 = codesters.Sprite("hateschool", -100, 100)
s4.set_size(0.3)


message1 = codesters.Text("Malaya",0,220,"deep pink")
message2 = codesters.Text("yay!!",0,-220,"deep pink")