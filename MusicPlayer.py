import pygame

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music Player")

music_file = "C:\\Users\\LENOVO\\Downloads\\Dream.mp3"

pygame.mixer.init()

pygame.mixer.music.load(music_file)
pygame.mixer.music.play()

screen.fill((255, 255, 255))
font = pygame.font.Font(None, 24)
text = font.render(music_file, True, (0, 0, 0))
text_rect = text.get_rect(center=(screen_width // 2, 100))
screen.blit(text, text_rect)

volume_slider_width = 200
volume_slider_height = 20
volume_slider_x = screen_width // 2 - volume_slider_width // 2
volume_slider_y = 150
volume_slider_handle_x = volume_slider_x
volume_slider_handle_y = volume_slider_y
volume_slider_dragging = False

pause_button_width = 80
pause_button_height = 40
pause_button_x = screen_width // 2 - pause_button_width - 50
pause_button_y = 200

resume_button_width = 80
resume_button_height = 40
resume_button_x = screen_width // 2 - resume_button_width // 2
resume_button_y = 200

stop_button_width = 80
stop_button_height = 40
stop_button_x = screen_width // 2 + 50
stop_button_y = 200

def draw_volume_slider():
    pygame.draw.rect(screen, (200, 200, 200), (volume_slider_x, volume_slider_y, volume_slider_width, volume_slider_height))
    pygame.draw.rect(screen, (0, 0, 255), (volume_slider_x, volume_slider_y, volume_slider_handle_x - volume_slider_x, volume_slider_height))

def draw_button(text, x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    button_font = pygame.font.Font(None, 24)
    button_text = button_font.render(text, True, (255, 255, 255))
    button_text_rect = button_text.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(button_text, button_text_rect)

def update_volume(volume):
    pygame.mixer.music.set_volume(volume)

def handle_button_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button
            if pause_button_x <= event.pos[0] <= pause_button_x + pause_button_width and pause_button_y <= event.pos[1] <= pause_button_y + pause_button_height:
                pygame.mixer.music.pause()
            elif resume_button_x <= event.pos[0] <= resume_button_x + resume_button_width and resume_button_y <= event.pos[1] <= resume_button_y + resume_button_height:
                pygame.mixer.music.unpause()
            elif stop_button_x <= event.pos[0] <= stop_button_x + stop_button_width and stop_button_y <= event.pos[1] <= stop_button_y + stop_button_height:
                pygame.mixer.music.stop()

def handle_volume_slider_event(event):
    global volume_slider_handle_x, volume_slider_dragging

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button
            if volume_slider_x <= event.pos[0] <= volume_slider_x + volume_slider_width and volume_slider_y <= event.pos[1] <= volume_slider_y + volume_slider_height:
                volume_slider_dragging = True
    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:  # Left mouse button
            volume_slider_dragging = False
    elif event.type == pygame.MOUSEMOTION:
        if volume_slider_dragging:
            volume_slider_handle_x = min(max(event.pos[0], volume_slider_x), volume_slider_x + volume_slider_width)
            volume = (volume_slider_handle_x - volume_slider_x) / volume_slider_width
            update_volume(volume)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
            handle_button_event(event)
            handle_volume_slider_event(event)

    screen.fill((255, 255, 255))
    draw_volume_slider()
    draw_button("Pause", pause_button_x, pause_button_y, pause_button_width, pause_button_height, (000, 000,  000))
    draw_button("Resume", resume_button_x, resume_button_y, resume_button_width, resume_button_height, (000, 000, 000))
    draw_button("Stop", stop_button_x, stop_button_y, stop_button_width, stop_button_height, (000, 000, 000))
    screen.blit(text, text_rect)
    pygame.display.flip()

pygame.quit()
