import shaders
from obj import Obj
from gl import Renderer


width = 1024    
height = 1024  


rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader



rend.glLoadModel(filename = "monster.obj",              
                 textureName = "monster.bmp",           
                 translate = (width/2,height/2,0),    
                 rotate = (0,90,0),                   
                 scale = (400,400,400))               



rend.glRender()

rend.glFinish("output.bmp")
