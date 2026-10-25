import glfw
from OpenGL.GL import *

glfw.init()
window = glfw.create_window(800, 600, "My Lab 1", None, None)
glfw.make_context_current(window)

print("GL %s on %s" % (glGetString(GL_VERSION).decode(),
                       glGetString(GL_RENDERER).decode()))

while not glfw.window_should_close(window):
    glClearColor(0.55, 0.10, 0.35, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()