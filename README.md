# Bespectacled-Belligerents
Hackathon 2024 - Bespectacled-Belligerents


This project was to create a module which sampled liquids and predicted what they are. It did this via interfaing sensors with Arduino, and then collecting this info from the Arduino in Python via a serial connection (ph_serial_monitor.ino). After collecting enough info using python (Take samples program.py created book2.xlsx, and book3.xlsx was manually created as a normalized version for training), a neural network was trained that could predict the current liquid (machinelearn.py created iteration4.keras). A GUI was made in pygame as well, which worked in the main program (final_program_1.py).
