# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 21:34:52 2025

@author: orion
"""

from cmu_graphics import*
gameActive = True

# Fill me in!

app.background = 'skyBlue'
Rect(0, 100, 400, 300, fill='forestGreen')
Rect(0, 200, 400, 150, fill=gradient('Gray', 'dimGray', start='top'))
centerLines = Line(0, 250, 400, 250, fill='gold', lineWidth=5, dashes=(25, 30))
centerLines2 = Line(0, 300, 400, 300, fill='gold', lineWidth=5, dashes=(25, 30))

mountain1 = Polygon(175, 100, 212, 52, 230, 54, 245, 31, 290, 100, fill=rgb(95, 155, 200))
mountain2 = Polygon(100, 105, 125, 70, 140, 80, 160, 55, 195, 105, fill=rgb(95, 110, 175))

progressBar = Line(45, 40, 50, 40, fill=gradient('royalBlue', 'mediumBlue', start='right'), lineWidth=20)
Rect(335, 30, 20, 20)
Rect(335, 30, 8, 10, fill='white')
Rect(344, 40, 9, 10, fill='white')
Rect(45, 30, 310, 20, fill=None, border='slateGrey', borderWidth=3)

def finishLine(xPos, primed):
    finishHitbox = Rect(180, 200, 50, 150, fill='whiteSmoke', visible=primed),
    Rect(180, 200, 25, 25, fill='black', visible=primed),
    Rect(205, 225, 25, 25, fill='black', visible=primed),
    Rect(180, 250, 25, 25, fill='black', visible=primed),
    Rect(205, 275, 25, 25, fill='black', visible=primed),
    Rect(180, 300, 25, 25, fill='black', visible=primed),
    Rect(205, 325, 25, 25, fill='black', visible=primed)


# Vehicles
car = Polygon(0, 211, 3, 210, 12, 210, 15, 211, 30, 211, 33, 210, 45, 210, 48, 220,
              48, 230, 45, 240, 33, 240, 30, 239, 15, 239, 12, 240, 3, 240, 0, 239,
              fill=gradient('royalBlue', 'mediumBlue'))
frontWindow = Polygon(40, 215, 42, 225, 40, 235, 30, 234, 30, 216)
backWindow = Rect(5, 215, 5, 20)
top = Polygon(10, 215, 30, 216, 30, 234, 10, 235, fill=None, border='black', borderWidth=1,)

enemy1 = Rect(315, 210, 48, 30, fill='fireBrick')
Polygon(318, 210, 325, 210, 343, 220, 345, 212, 352, 212, 355, 220, 355, 210, 363, 210, 363, 240, 355, 240, 355, 230, 352, 238, 345, 238, 343, 230, 325, 240, 318, 240, 315, 225, fill=None)
hitbox1 = Oval(338, 225, 45, 30, fill=None)

enemy2 = Rect(310, 260, 48, 30, fill='fireBrick')
hitbox2 = Oval(333, 275, 45, 30, fill=None)

enemy3 = Rect(320, 310, 48, 30, fill='fireBrick')
hitbox3 = Oval(343, 325, 45, 30, fill=None)

### Logo###
mainLogo = Label("Racin' Prototype", 200, 80, size=30, font='orbitron', bold=True, fill=gradient('royalBlue', 'mediumBlue', start='top'), border='midnightBlue', borderWidth=1)
subtitle = Label("Hold Space to Play", 200, 105, size=15)

### To Restart Game ###

# Add this after your other UI elements
restartButton = Rect(150, 145, 100, 40, fill=gradient('royalBlue', 'mediumBlue', start='top'), border='midnightBlue', borderWidth=2, visible=False)
restartLabel = Label("Restart", 200, 165, size=20, font='orbitron', bold=True, fill='lightSteelBlue', visible=False)

def showRestart():
    global gameActive
    restartButton.visible = True
    restartLabel.visible = True
    gameActive = False

def resetGame():
        global gameActive, mountain1, mountain2
        # Reset positions of all objects
        # Reset car body
        car.left = 0
        car.top = 211

        # Reset car windows and top using left/top and centerX/centerY
        frontWindow.left = 40
        frontWindow.top = 215
        frontWindow.centerX = 35  # original centerX
        frontWindow.centerY = 225 # original centerY

        backWindow.left = 5
        backWindow.top = 215
        backWindow.centerX = 7.5  # original centerX
        backWindow.centerY = 225  # original centerY

        top.left = 10
        top.top = 215
        top.centerX = 20  # original centerX
        top.centerY = 225 # original centerY

        enemy1.left = 315
        enemy1.top = 210
        hitbox1.centerX = 338
        hitbox1.centerY = 225

        enemy2.left = 310
        enemy2.top = 260
        hitbox2.centerX = 333
        hitbox2.centerY = 275

        enemy3.left = 320
        enemy3.top = 310
        hitbox3.centerX = 343
        hitbox3.centerY = 325

        mountain1.centerX = 212
        mountain1.bottom = 100
        mountain2.centerX = 144
        mountain2.bottom = 105

        centerLines.x1 = 0
        centerLines.x2 = 400
        centerLines.centerX = 200
        centerLines2.x1 = 0
        centerLines2.x2 = 400
        centerLines2.centerX = 200

        progressBar.x2 = 50

        mainLogo.value = "Racin' Prototype"
        mainLogo.fill = gradient('royalBlue', 'mediumBlue', start='top')
        mainLogo.border = 'midnightBlue'
        mainLogo.borderWidth = 1
        mainLogo.centerY = 80
        mainLogo.size = 30

        subtitle.visible = True

        restartButton.visible = False
        restartLabel.visible = False

        gameActive = True # <-- Set game as active again

### Functions ###
def onMousePress(mouseX, mouseY):
    if restartButton.visible and restartButton.hits(mouseX, mouseY):
        resetGame()

def steerCar(topPosition):
    car.top = topPosition
    frontWindow.top = topPosition + 5
    backWindow.top = topPosition + 5
    top.top = backWindow.top
    
def onKeyHold(keys):
    if not gameActive:
        return
    
    if ('space' in keys):
        centerLines.centerX -= 22.5
        centerLines.x2 = 400
        centerLines2.centerX -= 22.5
        centerLines2.x2 = 400
        subtitle.visible=False
        
        mountain1.centerX -= 4
        mountain2.centerX -= 6
        if (mountain1.right < 0):
           mountain1.left = 400
        if (mountain2.right < 0):
           mountain2.left = 400
        
        enemy1.centerX -= 15
        hitbox1.centerX -= 15
        if (enemy1.right < 0):
            enemy1.left = 450
            hitbox1.left = 450
        
        enemy2.centerX -= 10
        hitbox2.centerX -= 10
        if (enemy2.right < 0):
            enemy2.left = 425
            hitbox2.left = 425
        
        enemy3.centerX -= 17.5
        hitbox3.centerX -= 17.5
        if (enemy3.right < 0):
            enemy3.left = 475
            hitbox3.left = 475
           
        if ('s' in keys) or ('down' in keys):
            if(car.bottom < 345):
                steerCar(car.top + 5)
        if ('w' in keys) or ('up' in keys):
            if(car.top > 205):
                steerCar(car.top - 5)
        if ('d' in keys) or ('right' in keys):
            if(car.right < 390):
                car.centerX +=5
                frontWindow.centerX +=5
                backWindow.centerX +=5
                top.centerX +=5
        if ('a' in keys) or ('left' in keys):
            if(car.left > 0):
                car.centerX -=7.5
                frontWindow.centerX -=7.5
                backWindow.centerX -=7.5
                top.centerX -=7.5
        
        
        if(car.hitsShape(hitbox1)) or (car.hitsShape(hitbox2)) or (car.hitsShape(hitbox3)):
            mainLogo.value = "You Crashed"
            mainLogo.fill = gradient('fireBrick', 'red', start='bottom')
            mainLogo.border = 'maroon'
            showRestart()
            
        if(progressBar.x2 < 335):
            progressBar.x2 += 0.25
            
        subtitle.visible=False

        if(progressBar.x2 >=335):    
            mainLogo.value = "You Win!"
            mainLogo.fill = gradient('forestGreen', 'limeGreen', start='bottom')
            mainLogo.border = 'darkGreen'
            mainLogo.borderWidth = 4
            mainLogo.centerY = 185
            mainLogo.size = 75
            subtitle.visible=False
            showRestart()
    else:
        subtitle.visible=True

cmu_graphics.run()
