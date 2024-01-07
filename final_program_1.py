import cv2
import serial
import pygame
from pygame.locals import *
import numpy as np
import sys
import time
from openpyxl import load_workbook
import keras

model = keras.models.load_model("iteration4.keras")
all_liq = np.array(['Coca Cola','Orange Juice','Water','Pepsi','Vinegar','Gingerale','Red Bull','Milk','Diet Pepsi'])

def get_arduino_sensor_data():
    arduino_data = serial.Serial('COM9', 9600, timeout = 0.05)  # establish serial communication link
    run = 1
    while run == 1:
        sensor_data = arduino_data.readline().decode('utf-8')[:-2]
        if sensor_data != '':
            run = 0
    arduino_data.close()
    return sensor_data

def color_bgr():
    cap = cv2.VideoCapture(1)

    counter = 0
    total_avg = [0, 0, 0]

    while True:
        ret, frame = cap.read()
        height, width, _ = frame.shape

        # Define the region around the center
        center_x = width // 2
        center_y = height // 2
        sample_size = 150  # Size of sample in the middle
        sample = frame[center_y - sample_size // 2:center_y + sample_size // 2, center_x - sample_size // 2:center_x + sample_size // 2]

        # Display the frame with the region of interest
        # cv2.imshow('Original', frame)
        cv2.imshow('Sample', sample)

        # Calculate the average color of the region in BGR and HSV
        avg_color = np.mean(sample, axis=(0, 1))
        # avg_color_hsv = cv2.cvtColor(np.uint8([[avg_color]]), cv2.COLOR_BGR2HSV)[0][0]

        if counter > 30:
            total_avg = total_avg + avg_color

        counter += 1
        # Print the average color values
        # print(counter, ". BGR:", np.round(avg_color), "HSV:", avg_color_hsv)

        
        # Exits after "counter" number of instances
        if cv2.waitKey(1) & counter >= 60:
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

    return total_avg/30

def combine_data(data, bgr):
    data = data.split(",")
    data[0] = int(data[0])/175
    data[1]=int(data[1])/1000
    bgr = bgr/255
    bgr = bgr.tolist()
    print(bgr)
    all_data = np.append(data, bgr)
    return all_data

def save2excel(data):

    wb = load_workbook("book2.xlsx")
    ws = wb.worksheets[0]
    ws.append(data.tolist())
    wb.save("book2.xlsx")

pygame.init()

SCREEN_W = 800
SCREEN_H = 800

screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
yellow = ((255,255,0))
font = pygame.font.Font('freesansbold.ttf', 64)
font2 = pygame.font.Font('freesansbold.ttf', 32)

screen.fill(black)

pygame.display.set_caption('Liquid Classification')

button_text = font.render('Classify Liquid', True, black, green)
button_textframe = button_text.get_rect()
button_textframe.center = (SCREEN_W // 2, SCREEN_H // 2 - SCREEN_H/4)

return_text = font.render('No Liquid Sampled', True, black, white)
return_textframe = return_text.get_rect()
return_textframe.center = (SCREEN_W // 2, SCREEN_H // 2 + SCREEN_H/4)

collect_text = font.render('Collecting Data...', True, black, white)
collect_textframe = collect_text.get_rect()
collect_textframe.center = (SCREEN_W // 2, SCREEN_H // 2)

not_pressed = 1
counter = 0

while True:
    
    clock.tick(60)

###############################Check for quitting##########################################
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if (160 <= mouse[0] <= 640) and (165 <= mouse[1] <= 230):
                not_pressed = 0
                
        
    screen.fill(white)
    if not (not_pressed):
        button_text = font.render('Classify Liquid', True, black, yellow)
        screen.blit(collect_text, collect_textframe)
    screen.blit(return_text, return_textframe)
    screen.blit(button_text, button_textframe)
    pygame.display.update()

    if not (not_pressed):
        data = get_arduino_sensor_data()
        color_BGR = np.round(color_bgr())
        final_data = combine_data(data, color_BGR)
        predicted = np.zeros([1,1,5])
        predicted[0][0] = final_data
        pred = model.predict(predicted)
        liq = np.argmax(pred)
        print(str(pred))
        print(final_data)
        return_text = font2.render(str(all_liq[liq]), True, black, white)
        return_textframe = return_text.get_rect()
        return_textframe.center = (SCREEN_W // 2, SCREEN_H // 2 + SCREEN_H/4)
        button_text = font.render('Classify Liquid', True, black, green)
        not_pressed = 1
