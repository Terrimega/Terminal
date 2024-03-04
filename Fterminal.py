import pygame
from pygame.locals import *
import random
import os
import shutil
import subprocess

class Terminal:
    def __init__(self, font):
        self.font = font
        self.prompt = "AlbertoPC--$>"
        self.command_history = []
        self.current_command = ""
        self.output = []

    def process_command(self, command):
        if command.lower() == "help":
            # Help command output
            self.output.append(f"AlbertoPC--$>{command}")
            self.output.append("")
            self.output.append("List of available commands:")
            self.output.append("1. help - Show this help message")
            self.output.append("2. echo [text] - Display the given text")
            self.output.append("3. clear - Clear the screen")
            self.output.append("4. snake - Play the Snake game")
            self.output.append("5. ls - List files in the current directory")
            self.output.append("6. pwd - Show current working directory")
            self.output.append("7. date - Show current date and time")
            self.output.append("8. mkdir [directory_name] - Create a new directory")
            self.output.append("9. touch [file_name] - Create an empty file")
            self.output.append("10. rm [file_name] - Remove a file")
            self.output.append("11. rm -rf [directory_name] - Remove a directory recursively")
            self.output.append("12. cd [directory_name] - Change directory")
            self.output.append("13. pong - Open the Pong game")
            self.output.append("14. Hangman - Open the hangman game")
            self.output.append("15. cat - Open a file")
            self.output.append("16. quit - Close the terminal")
            self.output.append("")

        elif command.lower().startswith("echo"):
            # Echo command
            self.output.append(f"AlbertoPC--$>{command}")
            parts = command.split(">")
            if len(parts) == 1:
                text = parts[0][5:].strip()  # Get the text after "echo"
                self.output.append(text)
            elif len(parts) == 2:
                text = parts[0][5:].strip()  # Get the text after "echo"
                filename = parts[1].strip()  # Get the filename
                try:
                    with open(filename, 'w') as file:
                        file.write(text)
                    self.output.append(f"Text written to file: {filename}")
                except Exception as e:
                    self.output.append(f"Error writing to file: {e}")
            else:
                self.output.append("Usage: echo [text] or echo [text] > [filename]")
            self.output.append("")

        elif command.lower() == "clear":
            # Clear command
            self.output = []

        elif command.lower() == "snake":
            # Snake game command
            self.output.append(f"AlbertoPC--$>{command}")
            self.output.append("")
            self.output.append("")
            return "snake"

        elif command.lower() == "ls":
            # List files command
            self.output.append(f"AlbertoPC--$>{command}")
            files = os.listdir('.')
            for file in files:
                self.output.append(file)
            self.output.append("")

        elif command.lower() == "pwd":
            # Print working directory command
            self.output.append(f"AlbertoPC--$>{command}")
            cwd = os.getcwd()
            self.output.append(cwd)
            self.output.append("")

        elif command.lower() == "date":
            # Date command
            self.output.append(f"AlbertoPC--$>{command}")
            import datetime
            now = datetime.datetime.now()
            self.output.append(now.strftime("%Y-%m-%d        %H:%M:%S"))
            self.output.append("")

        elif command.lower().startswith("mkdir"):
            # Make directory command
            self.output.append(f"AlbertoPC--$>{command}")
            parts = command.split(" ", 1)
            if len(parts) == 2:
                try:
                    os.mkdir(parts[1])
                    self.output.append(f"Created directory: {parts[1]}")
                except FileExistsError:
                    self.output.append(f"Directory '{parts[1]}' already exists.")
            else:
                self.output.append("Usage: mkdir [directory_name]")
            self.output.append("")

        elif command.lower().startswith("touch"):
            # Touch command
            self.output.append(f"AlbertoPC--$>{command}")
            parts = command.split(" ", 1)
            if len(parts) == 2:
                try:
                    with open(parts[1], 'w'):
                        pass
                    self.output.append(f"Created file: {parts[1]}")
                except Exception as e:
                    self.output.append(f"Error creating file: {e}")
            else:
                self.output.append("Usage: touch [file_name]")
            self.output.append("")

        elif command.lower().startswith("rm"):
            # Remove command
            self.output.append(f"AlbertoPC--$>{command}")
            parts = command.split(" ", 1)
            if len(parts) == 2:
                try:
                    if parts[1].startswith("-rf"):  # Recursive force remove
                        directory = parts[1][4:].strip()
                        shutil.rmtree(directory)
                        self.output.append(f"Removed directory: {directory}")
                    else:  # Remove file
                        os.remove(parts[1])
                        self.output.append(f"Removed file: {parts[1]}")
                except Exception as e:
                    self.output.append(f"Error removing: {e}")
            else:
                self.output.append("Usage:")
                self.output.append("rm [file_name] - Remove a file")
                self.output.append("rm -rf [directory_name] - Remove a directory recursively")
            self.output.append("")

        elif command.lower().startswith("cd"):
            # Change directory command
            self.output.append(f"AlbertoPC--$>{command}")
            parts = command.split(" ", 1)
            if len(parts) == 2:
                try:
                    os.chdir(parts[1])
                    self.output.append(f"Changed directory to: {os.getcwd()}")
                except Exception as e:
                    self.output.append(f"Error changing directory: {e}")
            else:
                self.output.append("Usage: cd [directory_name]")
            self.output.append("")

        elif command.lower() == "pong":
            # Pong game command
            self.output.append(f"AlbertoPC--$>{command}")
            try:
                # Launch Pong game and position the window on top
                pong_process = subprocess.Popen(['python3', 'pong.py'])
                pygame_window_id = pygame.display.get_wm_info()["window"]
                subprocess.Popen(['wmctrl', '-i', '-r', str(pygame_window_id), '-e', '0,0,0,1000,600'])
                self.output.append("Opening Pong game...")
            except FileNotFoundError:
                self.output.append(".")
            except Exception as e:
                self.output.append(f"Error opening Pong game: {e}")

        elif command.lower() == "hangman":
            # Inicializar Pygame
            pygame.init()

            # Configuración de la pantalla
            WIDTH, HEIGHT = 1100, 700  # Ampliamos el tamaño de la ventana
            win = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Hangman Game")

            # Colores
            WHITE = (255, 255, 255)
            BLACK = (0, 0, 0)

            # Fuentes de texto
            LETTER_FONT = pygame.font.SysFont('comicsans', 40)
            WORD_FONT = pygame.font.SysFont('comicsans', 60)
            TITLE_FONT = pygame.font.SysFont('comicsans', 70)

            # Variables globales
            hangman_status = 0
            words = ["CLEAR", "TOUCH", "BASH", "DATE", "ECHO", "PSTREE", "MKDIR", "KILL-9"]
            word = random.choice(words)
            guessed = []
            used_letters = []

            # Función para dibujar el ahorcado
            def draw_man():
                if hangman_status >= 1:
                    pygame.draw.circle(win, WHITE, (WIDTH // 2, 150), 50, 5)  # Cabeza
                if hangman_status >= 2:
                    pygame.draw.line(win, WHITE, (WIDTH // 2, 200), (WIDTH // 2, 400), 5)  # Cuerpo
                if hangman_status >= 3:
                    pygame.draw.line(win, WHITE, (WIDTH // 2, 250), (WIDTH // 2 - 75, 325), 5)  # Brazo izquierdo
                if hangman_status >= 4:
                    pygame.draw.line(win, WHITE, (WIDTH // 2, 250), (WIDTH // 2 + 75, 325), 5)  # Brazo derecho
                if hangman_status >= 5:
                    pygame.draw.line(win, WHITE, (WIDTH // 2, 400), (WIDTH // 2 - 75, 450), 5)  # Pierna izquierda
                if hangman_status >= 6:
                    pygame.draw.line(win, WHITE, (WIDTH // 2, 400), (WIDTH // 2 + 75, 450), 5)  # Pierna derecha

            # Función para dibujar las letras adivinadas
            def draw_word():
                display_word = ""
                for letter in word:
                    if letter in guessed:
                        display_word += letter + " "
                    else:
                        display_word += "_ "
                text = WORD_FONT.render(display_word, 1, WHITE)
                win.blit(text, (WIDTH // 2 - text.get_width() // 2, 500))

            # Función para dibujar la lista de letras utilizadas
            def draw_used_letters():
                used = "Letras utilizadas: " + ", ".join(used_letters)
                text = LETTER_FONT.render(used, 1, WHITE)
                win.blit(text, (10, HEIGHT - 50))

            # Función para dibujar el título
            def draw_title():
                text = TITLE_FONT.render("Juego del Ahorcado", 1, WHITE)
                win.blit(text, (WIDTH // 2 - text.get_width() // 2, 20))

            # Función para dibujar la pantalla
            def redraw_window():
                win.fill(BLACK)
                draw_title()
                draw_word()
                draw_man()
                draw_used_letters()
                pygame.display.update()

            # Loop principal
            FPS = 60
            clock = pygame.time.Clock()
            run = True

            while run:
                clock.tick(FPS)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key in range(97, 123):  # Teclas de letras (a-z)
                            letter = chr(event.key).upper()  # Convertir a mayúsculas
                            if letter not in used_letters:
                                used_letters.append(letter)
                                if letter in word:
                                    guessed.append(letter)
                                else:
                                    hangman_status += 1

                redraw_window()

                won = True
                for letter in word:
                    if letter not in guessed:
                        won = False
                        break

                if won:
                    win.fill(WHITE)
                    pygame.time.delay(1500)
                    text = WORD_FONT.render("¡Ganaste!", 1, BLACK)
                    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
                    pygame.display.update()
                    pygame.time.delay(1500)
                    break

                if hangman_status == 6:
                    pygame.time.delay(1500)
                    win.fill(WHITE)
                    text = WORD_FONT.render("¡Perdiste!", 1, BLACK)
                    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
                    pygame.display.update()
                    pygame.time.delay(1500)
                    return

        elif command.lower().startswith("cat"):
            self.output.append(f"AlbertoPC--$>{command}")
            parts = command.split(" ", 1)
            if len(parts) == 2:
                try:
                    with open(parts[1], 'r') as file:
                        contents = file.read()
                        self.output.append(contents)
                except:
                    self.output.append(f"Error cannot find file")
            else:
                self.output.append("Usage: touch [file_name]")
            self.output.append("")

        elif command.lower().startswith("quit"):
            self.output.append(f"AlbertoPC--$>{command}")
            quit()


        elif command == "":
            # Empty command
            self.font.render(self.prompt, True, (0, 255, 0))
            self.output.append("AlbertoPC--$>")
        else:
            # Unknown command
            self.output.append(f"AlbertoPC--$>{command}")
            self.output.append(f"Command not found: {command}")

    def draw(self, surface):
        surface.fill((0, 0, 0))  # Fill with black

        # Render output lines
        y = 0
        for line in self.output:
            text_surface = self.font.render(line, True, (255, 255, 255))
            surface.blit(text_surface, (0, y))
            y += text_surface.get_height()

        # Render prompt (different color)
        prompt_surface = self.font.render(self.prompt, True, (0, 255, 0))  # Green color for prompt
        surface.blit(prompt_surface, (0, y))

        # Render current command (white color)
        command_surface = self.font.render(self.current_command, True, (255, 255, 255))
        surface.blit(command_surface, (prompt_surface.get_width(), y))

    def add_to_command(self, char):
        self.current_command += char

    def delete_last_char(self):
        self.current_command = self.current_command[:-1]

    def play_snake_game(self):
        # Snake game code
        pygame.init()

        # Colors
        white = (255, 255, 255)
        yellow = (255, 255, 102)
        black = (0, 0, 0)
        red = (213, 50, 80)
        green = (0, 255, 0)
        blue = (50, 153, 213)

        # Screen Size
        dis_width = 1000
        dis_height = 600
        dis = pygame.display.set_mode((dis_width, dis_height))
        pygame.display.set_caption('Snake Game')

        clock = pygame.time.Clock()

        snake_block = 10
        snake_speed = 15

        font_style = pygame.font.SysFont(None, 20)

        def our_snake(snake_block, snake_list):
            for x in snake_list:
                pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

        def message(msg, color):
            mesg = font_style.render(msg, True, color)
            dis.blit(mesg, [dis_width / 6, dis_height / 3])

        def gameLoop():
            game_over = False
            game_close = False

            x1 = dis_width / 2
            y1 = dis_height / 2

            x1_change = 0
            y1_change = 0

            snake_List = []
            Length_of_snake = 1

            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            score = 0

            while not game_over:

                while game_close == True:
                    dis.fill(black)
                    message("Perdiste, Presiona la tecla 'C' para volver a jugar o 'Q' para salir.", white)
                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                return "quit"
                            if event.key == pygame.K_c:
                                gameLoop()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return "quit"
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x1_change = -snake_block
                            y1_change = 0
                        elif event.key == pygame.K_RIGHT:
                            x1_change = snake_block
                            y1_change = 0
                        elif event.key == pygame.K_UP:
                            y1_change = -snake_block
                            x1_change = 0
                        elif event.key == pygame.K_DOWN:
                            y1_change = snake_block
                            x1_change = 0

                if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                    game_close = True
                x1 += x1_change
                y1 += y1_change
                dis.fill(black)
                pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
                snake_Head = []
                snake_Head.append(x1)
                snake_Head.append(y1)
                snake_List.append(snake_Head)
                if len(snake_List) > Length_of_snake:
                    del snake_List[0]

                for x in snake_List[:-1]:
                    if x == snake_Head:
                        game_close = True

                our_snake(snake_block, snake_List)

                # Display the food counter
                font = pygame.font.SysFont(None, 25)
                score_text = font.render("Comida: " + str(score), True, white)
                dis.blit(score_text, (10, 10))

                pygame.display.update()

                if x1 == foodx and y1 == foody:
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                    Length_of_snake += 1
                    score += 1

                clock.tick(snake_speed)

            return "quit"

        return gameLoop()

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Simulated Ubuntu Terminal")

    font = pygame.font.SysFont("jetbrains mono", 25)
    terminal = Terminal(font)

    clock = pygame.time.Clock()
    input_active = True
    show_terminal = True  # Flag to indicate showing terminal initially

    while True:
        screen.fill((0, 0, 0))  # Fill with black

        if show_terminal:
            terminal.draw(screen)
        else:
            pygame.display.update()  # Update screen to clear any residual snake game display

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == KEYDOWN:
                if show_terminal:  # If showing terminal, handle terminal input
                    if event.key == K_BACKSPACE:
                        terminal.delete_last_char()
                    elif event.key == K_RETURN:
                        result = terminal.process_command(terminal.current_command)
                        if result == "snake":
                            show_terminal = False
                        terminal.command_history.append(terminal.current_command)
                        terminal.current_command = ""
                    else:
                        char = event.unicode
                        if char:
                            terminal.add_to_command(char)
                else:  # If not showing terminal (after quitting snake game), set flag to show terminal again
                    if event.key == K_q:
                        show_terminal = True

        if not show_terminal:
            result = terminal.play_snake_game()
            if result == "quit":
                show_terminal = True

        clock.tick(30)


if __name__ == "__main__":
    main()
