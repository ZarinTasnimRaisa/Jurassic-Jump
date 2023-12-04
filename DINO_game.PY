from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def dinosaur():
    glColor3f(0, 0, 0)
    #head
    midpoint(90, 200, 105, 200)
    midpoint(90, 200, 90, 195)
    midpoint(85, 195, 90, 195)
    midpoint(85, 195, 85, 190)
    midpoint(80, 190, 85, 190)
    midpoint(80, 190, 80, 110)
    midpoint(105, 200, 105, 195)
    midpoint(105, 195, 112, 195)
    midpoint(112, 195, 112, 190)
    midpoint(112, 190, 117, 190)
    midpoint(117, 190, 117, 185)
    midpoint(117, 185, 125, 185)
    midpoint(125, 185, 125, 180)
    midpoint(125, 180, 130, 180)
    midpoint(130, 180, 130, 160)
    midpoint(125, 160, 130, 160)
    midpoint(125, 160, 125, 155)
    midpoint(105, 155, 125, 155)
    #eye
    midpoint(95, 185, 102, 185)
    midpoint(102, 185, 102, 178)
    midpoint(95, 178, 102, 178)
    midpoint(95, 185, 95, 178)
    #body
    midpoint(105, 155, 105, 115)
    midpoint(105, 115, 110, 115)
    midpoint(110, 115, 110, 110)
    midpoint(110, 110, 115, 110)
    midpoint(115, 110, 115, 70)
    midpoint(110, 70, 115, 70)
    midpoint(110, 70, 110, 65)
    midpoint(102, 65, 110, 65)
    midpoint(102, 65, 102, 60)
    midpoint(47, 60, 90, 60)
    midpoint(50, 110, 80, 110)
    midpoint(50, 110, 50, 105)
    midpoint(45, 105, 50, 105)
    midpoint(45, 105, 45, 100)
    midpoint(40, 100, 45, 100)
    midpoint(40, 100, 40, 95)
    midpoint(35, 95, 40, 95)
    midpoint(35, 95, 35, 90)
    #tail
    midpoint(15, 90, 35, 90)
    midpoint(15, 90, 15, 85)
    midpoint(15, 85, 20, 85)
    midpoint(20, 85, 20, 80)
    midpoint(20, 80, 25, 80)
    midpoint(25, 80, 25, 75)
    midpoint(25, 75, 35, 75)
    midpoint(35, 75, 35, 60)
    midpoint(47, 60, 50, 60)
    #leg front 1
    midpoint(110, 65, 110, 55)
    midpoint(110, 55, 120, 55)
    midpoint(120, 55, 120, 45)
    midpoint(102, 45, 120, 45)
    midpoint(102, 60, 102, 45)
    #leg front 2 (big one)
    midpoint(102, 60, 102, 45)
    midpoint(102, 45, 110, 45)
    midpoint(110, 45, 110, 35)
    midpoint(90, 35, 110, 35)
    midpoint(90, 60, 90, 35)
    #leg back 1 (big one)
    midpoint(35, 60, 35, 35)
    midpoint(35, 35, 55, 35)
    midpoint(55, 45, 55, 35)
    midpoint(47, 45, 55, 45)
    midpoint(47, 60, 47, 45)
    #leg back 2
    midpoint(47, 60, 47, 45)
    midpoint(47, 45, 65, 45)
    midpoint(65, 55, 65, 45)
    midpoint(55, 55, 65, 55)
    midpoint(55, 55, 65, 55)
    midpoint(55, 60, 55, 55)

def cactus():
    glColor3f(0.0, 0.5, 0.0)

    midpoint(500, 37, 525, 37)
    midpoint(500, 80, 500, 37)
    midpoint(500,200,500,95)
    midpoint(525, 200, 525, 110)
    midpoint(525,90,525,37)
    midpoint(500,200,505,200)
    midpoint(520,200,525,200)
    midpoint(505,205,505,200)
    midpoint(505,205,520,205)
    midpoint(520,205,520,200)

    midpoint(475,80,500,80)
    midpoint(475,85,475,80)
    midpoint(470,85,475,85)
    midpoint(470,85,470,90)
    midpoint(465,90,470,90)
    midpoint(470,90,470,85)
    midpoint(465,150, 465,90)
    midpoint(465,150,470,150)
    midpoint(470,155,470,150)
    midpoint(470,155,475,155)
    midpoint(475,155,475,150)
    midpoint(475,150,480,150)
    midpoint(480,150,480,95)
    midpoint(480,95,500,95)

    midpoint(525,90,560,90)
    midpoint(525,110,554,110)
    midpoint(560,97,560,90)
    midpoint(560,97,567,97)
    midpoint(567,104,567,97)
    midpoint(567,104,574,104)
    midpoint(574,165,574,104)
    midpoint(567,165,574,165)
    midpoint(567,170,567,165)
    midpoint(561,170,567,170)
    midpoint(561,170,561,165)
    midpoint(554,165,561,165)
    midpoint(554,165,554,110)

    
    
    

def bird():
    # Define the bird shape using the midpoint algorithm for drawing points
    midpoint(179, 176, 185, 179)
    midpoint(185, 179, 197, 184)
    midpoint(197, 184, 201, 173)
    midpoint(201, 173, 207, 169)
    midpoint(207, 169, 210, 166)
    midpoint(210, 166, 213, 158)
    midpoint(213, 158, 218, 159)
    midpoint(218, 159, 214, 166)
    midpoint(214, 166, 230, 187)
    midpoint(230, 187, 256, 200)
    midpoint(256, 200, 235, 201)
    midpoint(235, 201, 224, 199)
    midpoint(224, 199, 216, 193)
    midpoint(216, 193, 212, 200)
    midpoint(212, 200, 205, 205)
    midpoint(205, 205, 191, 207)
    midpoint(191, 207, 197, 200)
    midpoint(197, 200, 200, 193)
    midpoint(200, 193, 185, 184)
    midpoint(185, 184, 180, 180)
    midpoint(180, 180, 179, 176)
    midpoint(216, 193, 205, 180)
    midpoint(205, 180, 204, 191)
    midpoint(204, 191, 207, 195)
    midpoint(207, 195, 200, 193)
    midpoint(197, 186, 179, 176)

def land():
    glColor3f(0.65 , 0.165, 0.165)
    midpoint(0, 35, 10000, 35)

def draw_points(x0, y0):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x0,y0)
    glEnd()

def midpoint(x0, y0, x1, y1):
    zone = findZone(x0, y0, x1, y1)
    x0, y0 = zoneConvert0(zone, x0, y0)
    x1, y1 = zoneConvert0(zone, x1, y1)
    dx = x1 - x0
    dy = y1 - y0
    dinit = 2 * dy - dx
    dne = 2 * dy - 2 * dx
    de = 2 * dy
    for i in range(x0, x1):
        a, b = convert0_Original(zone, x0, y0)
        if dinit >= 0:
            dinit = dinit + dne
            draw_points(a, b)
            x0 += 1
            y0 += 1
        else:
            dinit = dinit + de
            draw_points(a, b)
            x0 += 1

def findZone(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dx) > abs(dy): #For Zone 0, 3, 4 & 7
        if dx > 0 and dy > 0:
            return 0
        elif dx < 0 and dy > 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        else:
            return 7
    else: #For zone 1, 2, 5 & 6
        if dx > 0 and dy > 0:
            return 1
        elif dx < 0 and dy > 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        else:
            return 6

def zoneConvert0(zone, x0, y0):
    if zone == 0:
        return x0, y0
    elif zone == 1:
        return y0, x0
    elif zone == 2:
        return -y0, x0
    elif zone == 3:
        return -x0, y0
    elif zone == 4:
        return -x0, -y0
    elif zone == 5:
        return -y0, -x0
    elif zone == 6:
        return -y0, x0
    elif zone == 7:
        return x0, -y0
   
def convert0_Original(zone, x0, y0):
    if zone == 0:
        return x0, y0
    if zone == 1:
        return y0, x0
    if zone == 2:
        return -y0, -x0
    if zone == 3:
        return -x0, y0
    if zone == 4:
        return -x0, -y0
    if zone == 5:
        return -y0, -x0
    if zone == 6:
        return y0, -x0
    if zone == 7:
        return x0, -y0
   
def specialKeyListener(key, left, right):
    glutPostRedisplay()
    pass
    glutPostRedisplay()

def mouseListener(button, state, x, y):
    global ballx, bally, create_new, pauseBoolean, gameOver, score
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
            pass

def animate():
    glutPostRedisplay()
    pass

def iterate():
    glViewport(0, 0, 800, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.9, 0.9, 0.95, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    dinosaur()
    bird()
    cactus()
    land()

    glutSwapBuffers()
    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Jurassic Jump") #window name
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()

