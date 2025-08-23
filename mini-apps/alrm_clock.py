import pygame
import time
import datetime
import os
import sys
from pygame import mixer

# Initialize pygame and mixer
pygame.init()
mixer.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alarm Clock")
clock = pygame.time.Clock()

# Fonts
large_font = pygame.font.SysFont('Arial', 80)
medium_font = pygame.font.SysFont('Arial', 30)
small_font = pygame.font.SysFont('Arial', 20)

# Alarm list
alarms = []
active_alarm = None

# Sound
try:
    alarm_sound = mixer.Sound('alarm.wav')
except:
    print("Warning: Could not load alarm sound. Using default beep.")
    alarm_sound = None

class Alarm:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.active = True
    
    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"
    
    def is_time(self, current_time):
        return (self.hour == current_time.hour and 
                self.minute == current_time.minute and
                current_time.second < 2 and self.active)

def draw_button(text, x, y, width, height, color, hover_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1 and action:
            return action()
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))
    
    text_surf = medium_font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(x + width/2, y + height/2))
    screen.blit(text_surf, text_rect)
    return False

def add_alarm():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    alarms.append(Alarm(hour, (minute + 1) % 60))  # Set alarm for 1 minute from now

def toggle_alarm(index):
    if 0 <= index < len(alarms):
        alarms[index].active = not alarms[index].active

def delete_alarm(index):
    if 0 <= index < len(alarms):
        alarms.pop(index)

def main():
    global active_alarm
    alarm_ringing = False
    alarm_start_time = 0
    
    while True:
        current_time = datetime.datetime.now()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if alarm_ringing:
                        alarm_ringing = False
                        if alarm_sound:
                            alarm_sound.stop()
        
        # Check if any alarm should go off
        if not alarm_ringing:
            for alarm in alarms:
                if alarm.is_time(current_time):
                    alarm_ringing = True
                    alarm_start_time = time.time()
                    if alarm_sound:
                        alarm_sound.play(-1)  # Loop the sound
                    break
        
        # Stop alarm after 1 minute
        if alarm_ringing and (time.time() - alarm_start_time) > 60:
            alarm_ringing = False
            if alarm_sound:
                alarm_sound.stop()
        
        # Draw everything
        screen.fill(WHITE)
        
        # Draw current time
        time_text = current_time.strftime("%H:%M:%S")
        time_surface = large_font.render(time_text, True, BLACK)
        time_rect = time_surface.get_rect(center=(WIDTH//2, 150))
        screen.blit(time_surface, time_rect)
        
        # Draw date
        date_text = current_time.strftime("%A, %B %d, %Y")
        date_surface = medium_font.render(date_text, True, BLACK)
        date_rect = date_surface.get_rect(center=(WIDTH//2, 220))
        screen.blit(date_surface, date_rect)
        
        # Draw add alarm button
        if draw_button("Add Alarm", WIDTH//2 - 100, 300, 200, 50, GRAY, (200, 230, 200), add_alarm):
            pass
        
        # Draw alarms
        alarm_y = 370
        for i, alarm in enumerate(alarms):
            # Alarm time
            alarm_text = f"{alarm.hour:02d}:{alarm.minute:02d}"
            alarm_surface = medium_font.render(alarm_text, True, BLUE if alarm.active else GRAY)
            screen.blit(alarm_surface, (WIDTH//2 - 100, alarm_y))
            
            # Toggle button
            toggle_text = "ON" if alarm.active else "OFF"
            toggle_color = (200, 255, 200) if alarm.active else (255, 200, 200)
            if draw_button(toggle_text, WIDTH//2 + 50, alarm_y, 50, 30, 
                          toggle_color, toggle_color, lambda i=i: toggle_alarm(i)):
                pass
            
            # Delete button
            if draw_button("X", WIDTH//2 + 110, alarm_y, 30, 30, (255, 200, 200), (255, 150, 150), 
                          lambda i=i: delete_alarm(i) if not alarm_ringing else None):
                pass
                
            alarm_y += 40
        
        # Alarm ringing overlay
        if alarm_ringing:
            s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            s.fill((255, 200, 200, 128))
            screen.blit(s, (0, 0))
            
            alarm_text = medium_font.render("ALARM! Press ESC to stop", True, RED)
            alarm_rect = alarm_text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(alarm_text, alarm_rect)
        
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()