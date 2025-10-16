import glfw
from OpenGL.GL import *
from OpenGL.GLU import *  
import time
import math

vertices = [
    [-2, -1, -1],
    [2, -1, -1],
    [2,  1, -1],
    [-2, 1, -1],
    [-2, -1,  1],
    [2, -1,  1],
    [2,  1,  1],
    [-2, 1,  1]
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  
    (4, 5), (5, 6), (6, 7), (7, 4),  
    (0, 4), (1, 5), (2, 6), (3, 7)   
]

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

if not glfw.init():
    raise Exception("Falha ao inicializar GLFW")

glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_COMPAT_PROFILE)

window = glfw.create_window(800, 600, "Retângulo", None, None)
if not window:
    glfw.terminate()
    raise Exception("Não foi possível criar a janela OpenGL")

glfw.make_context_current(window)
print("Versão OpenGL:", glGetString(GL_VERSION).decode())

glEnable(GL_DEPTH_TEST)

width, height = glfw.get_framebuffer_size(window)
glViewport(0, 0, width, height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, width / height, 0.1, 100.0)

glMatrixMode(GL_MODELVIEW)

start_time = time.time()
while not glfw.window_should_close(window):
    glfw.poll_events()
    elapsed = time.time() - start_time

    glClearColor(0.1, 0.1, 0.1, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    glTranslatef(0.0, 0.0, -5.0)

    scale = 0.5 + 0.5 * math.sin(elapsed)
    glScalef(scale, scale, scale)

    glRotatef(elapsed * 50, 1, 1, 0)

    glColor3f(1, 1, 1)
    glLineWidth(2.0)
    draw_cube()

    glfw.swap_buffers(window)

glfw.terminate()
