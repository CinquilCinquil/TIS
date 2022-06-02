import pygame as pg
import ctypes
import fs
import os


class Animator:
    def __init__(self, anims, owner, a_type):
        self.owner = owner
        self.names = anims
        self.current = self.names[0]
        self.animations = []
        for i in self.names:
            self.animations.append(Animation(self.owner + '_' + i, 8, 'Graphics/'+a_type+self.owner, a_type, i + '_'))
            
    def addAnimation(self, anim):
        if anim in self.names:
            self.names[self.name.indes(anim)] = Animation(self.owner + '_' + anim, 16, 'Graphics/'+a_type+self.owner, a_type, anim + '_')
        else:
            self.animations.append(Animation(self.owner + '_' + anim, 8, 'Graphics/'+a_type+self.owner, a_type, anim + '_'))
    
    def getCurrentFrame(self):
        return self.animations[self.names.index(self.current)].playActualFrame()

    def play(self, a):
        if a in self.names:
            self.current = a
            return self.animations[self.names.index(a)].play()

    def playFrame(self, a, i):
        if a in self.names:
            self.current = a
            return self.animations[self.names.index(a)].playFrame(i)


class Animation:

    def __init__(self, name, fps, folder, a_type, prefix):
        self.name = name
        self.frames = []
        self.valid = False
        self.idx = 0
        for f in os.listdir(folder + '/'):
            if (f.endswith(".png") and f.startswith(prefix)):
                self.frames.append(pg.image.load(folder + '/'+f).convert_alpha())
                if len(self.frames) == 1:
                    self.valid = True
        self.fps = fps
        

    def play(self): #roda a animação na velocidade normal

        if(self.valid):
            self.idx = fs.loopValue(self.idx, 0, len(self.frames)-1, self.fps/64)
            return self.frames[int(self.idx)]
        
    def playFrame(self, i): #retorna um frame específico da animação
        if(self.valid):
            self.idx = int(i)
            return self.frames[int(self.idx)]

    def playActualFrame(self): #retorna o frame atual da animação
        if(self.valid):
            return self.frames[int(self.idx)]