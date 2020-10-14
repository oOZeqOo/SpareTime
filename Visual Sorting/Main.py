'''
    Created a Visual Sorter using lines to show sorting algorithms    
    When the script is executed, select your settings and enter a number between 
    the values and hit 'Sort'
    
    Controls:
        Right Click - restarts the application
        Space       - starts the sorting algorithm

'''

import pygame
import numpy as np
import random
import tkinter as tk
from tkinter import messagebox, simpledialog

# Screen
WIDTH, HEIGHT = 600, 400
SCALE = 200

# Colors
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Static Variables
# Size shouldn't be over WIDTH - 40
SIZE = 50

#How fast the lines get Sorted
SPEED = {"Slow": 100, "Medium": 50, "Fast" : 10, "Super Fast": 0}



# Global Variables
global array, debug
array = []
debug = False

# Selection sort
def selection_sort(surface, input_list, speed):
    print('Selection Sort' if debug else '')
    for idx in range(len(input_list)):

        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
        
        # Swap the minimum value with the compared value
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
        
        # Update the pygame window to show the steps in the algorithm
        redrawWindow(surface)
        drawLines(surface, input_list)
        pygame.display.update()
        pygame.time.delay( SPEED[speed] )


# Merge Sort
def merge_sort(surface, unsorted_list, speed):
    print('Merge Sort' if debug else '')
    if len(unsorted_list) <= 1:
        return unsorted_list

    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(surface, left_list, speed)
    right_list = merge_sort(surface, right_list, speed)
    return list(merge( left_list, right_list, surface, speed))

#Merge sort algorithm
def merge(left_half,right_half, surface, speed):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half = left_half[1:]
        else:
            res.append(right_half[0])
            right_half = right_half[1:]

    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half

    # Update the pygame window to show the steps in the algorithm
    redrawWindow(surface)
    drawLines(surface, left_half)
    drawLines(surface, right_half)
    pygame.display.update()
    pygame.time.delay(SPEED[speed])

    return res

#Shell sort
def shellSort(surface, input_list, speed):
    print('Shell Sort' if debug else '')
    gap = len(input_list) // 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
            # Sort the sub list for this gap

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j - gap
            input_list[j] = temp

            # Update the pygame window to show the steps in the algorithm
            redrawWindow(surface)
            drawLines(surface, input_list)
            pygame.display.update()
            pygame.time.delay(SPEED[speed])

        # Reduce the gap for the next element
        gap = gap // 2


#Insertion sort
def insertion_sort(surface, list, speed):
    print('Insertion Sort' if debug else '')
    for i in range(1, len(list)):
        j = i - 1
        nxt_element = list[i]

        # Compare the current element with next one
        while (list[j] > nxt_element) and (j >= 0):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = nxt_element

        # Update the pygame window to show the steps in the algorithm
        redrawWindow(surface)
        drawLines(surface, list)
        pygame.display.update()
        pygame.time.delay(SPEED[speed])

#Bubble sort
def bubblesort(surface, list, speed):
    print('sorting' if debug else '')

    # Swap the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp

        # Update the pygame window to show the steps in the algorithm
        redrawWindow(surface)
        drawLines(surface, list)
        pygame.display.update()
        pygame.time.delay(SPEED[speed])

# Draws one line onto the screen
def drawLine(surface, num, x):
    pygame.draw.line(surface, BLUE, (x + (1/(2*WIDTH)) , HEIGHT - 20), (x + (1/(2*WIDTH)) ,  num))

# Draws lines of different length onto the screen
def drawLines(surface, arr):
    global SIZE
    for num in range(len(arr)):
        drawLine(surface, array[num], ((num / SIZE) * (WIDTH - 40) ) + 20)
    pygame.display.update()

# Method to call to update the screen
def redrawWindow(surface):
    global array
    surface.fill(WHITE)
    pygame.draw.line(surface, BLACK, ( 20 , HEIGHT - 20 ), ( WIDTH - 20, HEIGHT - 20 ), 2)
    drawLines(surface, array)
    pygame.display.update()

#Creates a popup to handle selection
# @return int numberOfLines, algorithm string, speed string
def getInput():
    print("Creating input")
    global numberOfLines, SPEED
    numberOfLines = '0'
    options = ["Bubble Sort", "Insertion Sort", "Merge Sort", "Shell Sort", "Selection Sort",]
    speeds = ["Slow", "Medium", "Fast", "Super Fast"]
    root = tk.Tk()

    # Set up a drop down box for sorting options
    clicked = tk.StringVar()
    clicked.set(options[0])
    drop = tk.OptionMenu(root, clicked, *options)
    drop.pack()

    # Set up a drop down box for speeds  
    speed = tk.StringVar()
    speed.set(speeds[0])
    speeddrop = tk.OptionMenu(root, speed, *speeds)
    speeddrop.pack()

    numbox = tk.Entry(root)
    def onnumentry(evt):
        global numberOfLines
        numberOfLines = numbox.get()
        root.destroy()
    def onokclick():
        global numberOfLines
        numberOfLines = numbox.get()
        if numberOfLines is None:
            numberOfLines = 5
        if numberOfLines.isnumeric():
            numberOfLines = int(numberOfLines)
            if numberOfLines > 2 or numberOfLines < 560:
                root.destroy()

    tk.Label(root, text = "Enter a number between 2 and " + str(WIDTH - 40)).pack(side = 'top')

    numbox.pack(side = 'top')
    numbox.bind('<Return>', onnumentry)
    tk.Button(root, command=onokclick, text = 'Sort').pack(side = 'top')
    root.geometry("200x150")
    root.mainloop()
    return int(numberOfLines), clicked.get(), speed.get()

# Restarts the application as if it was just opened
def restart(surface, number):
    global SIZE, array
    redrawWindow(surface)
    SIZE = number
    array = np.random.randint(low=1, high=HEIGHT - 40, size=number)
    drawLines(surface, array)

# Main loop 
def main(d=False):
    global SIZE, array, debug
    debug = d
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    redrawWindow(win)
    number_of_cases , sort_type, speed = getInput()
    restart(win, number_of_cases)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # Right Click resets the screen
            if pygame.mouse.get_pressed()[2]:
                print('Restarting')
                number_of_cases, sort_type, speed = getInput()
                restart(win, number_of_cases)


            keys = pygame.key.get_pressed()

            # Pressing space starts the algorithm
            if keys[pygame.K_SPACE] :
                if sort_type == "Bubble Sort":
                    bubblesort(win, array, speed)
                if sort_type == "Insertion Sort":
                    insertion_sort(win, array, speed)
                if sort_type == "Shell Sort":
                    shellSort(win, array, speed)
                if sort_type == "Merge Sort":
                    merge_sort(win, array, speed) #Doesnt work
                if sort_type == "Selection Sort":
                    selection_sort(win, array, speed)


        redrawWindow(win)


if __name__ == "__main__":
    main(d=True)