import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()

playlist = [
    {
        "file": "music/IOWA - Улыбайся.mp3",
        "title": "IOWA - Улыбайся",
        "cover": "covers/IOWA.png"
    },
    {
        "file": "music/Blur - Song 2.mp3",
        "title": "Blur - Song 2",
        "cover": "covers/blur.png"
    },
    {
        "file": "music/The Beatles - Come Together.mp3",
        "title": "The Beatles - Come Together",
        "cover": "covers/Beatles.png"
    },
    {
        "file": "music/Red Hot Chili Peppers - Dani California.mp3",
        "title": "Red Hot Chili Peppers - Dani California",
        "cover": "covers/RHCP.png"
    }
]

current_index = 0
is_playing = False

def load_song(index):
    global cover_img
    pygame.mixer.music.load(playlist[index]["file"])
    cover_img = pygame.image.load(playlist[index]["cover"])
    cover_img = pygame.transform.scale(cover_img, (200, 200))

def play_song():
    global is_playing
    pygame.mixer.music.play()
    is_playing = True

def stop_song():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False

def next_song():
    global current_index
    current_index = (current_index + 1) % len(playlist)
    load_song(current_index)
    play_song()

def prev_song():
    global current_index
    current_index = (current_index - 1) % len(playlist)
    load_song(current_index)
    play_song()

load_song(current_index)

start_time = 0

while True:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:   
                play_song()
                start_time = pygame.time.get_ticks()

            elif event.key == pygame.K_s: 
                stop_song()

            elif event.key == pygame.K_n:
                next_song()
                start_time = pygame.time.get_ticks()

            elif event.key == pygame.K_b: 
                prev_song()
                start_time = pygame.time.get_ticks()

            elif event.key == pygame.K_q: 
                pygame.quit()
                sys.exit()

    screen.blit(cover_img, (50, 100))

    title_text = font.render(playlist[current_index]["title"], True, (255, 255, 255))
    screen.blit(title_text, (300, 100))

    if is_playing:
        elapsed_ms = pygame.time.get_ticks() - start_time
        seconds = elapsed_ms // 1000
        time_text = font.render(f"Time: {seconds}s", True, (200, 200, 200))
    else:
        time_text = font.render("Stopped", True, (200, 200, 200))

    screen.blit(time_text, (300, 150))
    controls = [
        "P = Play",
        "S = Stop",
        "N = Next",
        "B = Back",
        "Q = Quit"
    ]

    for i, txt in enumerate(controls):
        t = font.render(txt, True, (180, 180, 180))
        screen.blit(t, (300, 200 + i * 30))

    pygame.display.flip()
    clock.tick(60)