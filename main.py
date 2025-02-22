import tkinter as tk
import random

# 遊戲設定
WIDTH = 500
HEIGHT = 500
GRID_SIZE = 20


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("貪食蛇遊戲")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="red")
        self.canvas.pack()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.create_food()
        self.direction = "Right"

        self.running = True
        self.root.bind("<KeyPress>", self.change_direction)
        self.update_game()

    def create_food(self):
        x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE
        y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
        return (x, y)

    def change_direction(self, event):
        directions = {"Left": "Right", "Right": "Left", "Up": "Down", "Down": "Up"}
        if event.keysym in directions and directions[event.keysym] != self.direction:
            self.direction = event.keysym

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Left":
            head_x -= GRID_SIZE
        elif self.direction == "Right":
            head_x += GRID_SIZE
        elif self.direction == "Up":
            head_y -= GRID_SIZE
        elif self.direction == "Down":
            head_y += GRID_SIZE

        new_head = (head_x, head_y)

        if (
                head_x < 0 or head_x >= WIDTH or
                head_y < 0 or head_y >= HEIGHT or
                new_head in self.snake
        ):
            self.running = False
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.create_food()
        else:
            self.snake.pop()

    def draw_elements(self):
        self.canvas.delete("all")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill="green")
        fx, fy = self.food
        self.canvas.create_oval(fx, fy, fx + GRID_SIZE, fy + GRID_SIZE, fill="red")

    def update_game(self):
        if self.running:
            self.move_snake()
            self.draw_elements()
            self.root.after(100, self.update_game)
        else:
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="white", font=("Arial", 24))


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
