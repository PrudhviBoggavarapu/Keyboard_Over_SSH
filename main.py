# Import the pygame module
import pygame
from pygame.locals import *
from time import sleep
import paramiko
ssh = paramiko.SSHClient()
holderForSshFile = open('.gitignore/sshSTUFF', 'r').read().splitlines()
host = holderForSshFile[0]
UserName = holderForSshFile[1]
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=UserName)

pygame.mixer.quit()

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
key_list ={K_UP:'Up',
K_DOWN:'Down',
K_LEFT:'Left',
K_RIGHT:'Right',
K_ESCAPE:'Escape',
KEYDOWN:'KEYDOWN',
QUIT:'QUIT',
KMOD_ALT:'Alt_L',
KMOD_CAPS:'Caps_Lock',
KMOD_CTRL:'Control_L',
KMOD_LALT:'Alt_L',
KMOD_LCTRL:'Control_L',
KMOD_LMETA:'Meta_L',
KMOD_LSHIFT:'Shift_L',
KMOD_META:'Meta_R',
KMOD_MODE:'KMOD_MODE',
KMOD_NONE:'KMOD_NONE',
KMOD_NUM:'KMOD_NUM',
KMOD_RALT:'KMOD_RALT',
KMOD_RCTRL:'KMOD_RCTRL',
KMOD_RMETA:'KMOD_RMETA',
KMOD_RSHIFT:'KMOD_RSHIFT',
KMOD_SHIFT:'KMOD_SHIFT',
K_AMPERSAND:'K_AMPERSAND',
K_ASTERISK:'K_ASTERISK',
K_AT:'K_AT',
K_BACKSLASH:'backslash',
K_BACKSPACE:'BackSpace',
K_BREAK:'Break',
K_SPACE:'space',
K_TAB:'Tab',
13:'Return',
1073742051:'Super_L'


}
# Initialize pygame
pygame.init()
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
display_width = 800
display_height = 600
black = (225,225,225)
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def message_display(text):
    screen.fill((0,0,0))
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Variable to keep the main loop running
running = True
Key ='Nothing Yet'
changer = False
def sendKey(l):
    if l == '':
        Command = 'DISPLAY=:0 xdotool getactivewindow key '+ TrueNumber
    else:
        Command = 'DISPLAY=:0 xdotool getactivewindow key '+ l
    stdin, stdout, stderr = ssh.exec_command(Command)
message_display(Key)
while running:
    sleep(.05)
    # Look at every event in the queue
    if changer == True:
        sendKey(Key)
        message_display(Key)
        changer = False
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            try:
                Key = key_list[event.key]
                TrueNumber = event.key

                changer = True
            except:
                try:
                    Key = chr(event.key)
                    TrueNumber = event.key

                    changer = True

                except:
                    Key = str(event.key)

                    TrueNumber = event.key
                    changer = True
            if event.key == K_ESCAPE:
                running = False


        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
ssh.close()
exit()





































            #
