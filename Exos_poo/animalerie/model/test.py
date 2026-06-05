import arcade

# Window settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Grid Movement Example"

TILE_SIZE = 50
GRID_WIDTH = SCREEN_WIDTH // TILE_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Player starts in the middle of the grid
        self.player_x = GRID_WIDTH // 2
        self.player_y = GRID_HEIGHT // 2

    def on_draw(self):
        arcade.start_render()

        # Draw grid
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                arcade.draw_rectangle_outline(
                    x * TILE_SIZE + TILE_SIZE / 2,
                    y * TILE_SIZE + TILE_SIZE / 2,
                    TILE_SIZE,
                    TILE_SIZE,
                    arcade.color.LIGHT_GRAY
                )

        # Draw player (a red square)
        arcade.draw_rectangle_filled(
            self.player_x * TILE_SIZE + TILE_SIZE / 2,
            self.player_y * TILE_SIZE + TILE_SIZE / 2,
            TILE_SIZE * 0.8,
            TILE_SIZE * 0.8,
            arcade.color.RED
        )

    def on_key_press(self, key, modifiers):
        # Move player by grid squares
        if key == arcade.key.UP:
            self.player_y += 1
        elif key == arcade.key.DOWN:
            self.player_y -= 1
        elif key == arcade.key.LEFT:
            self.player_x -= 1
        elif key == arcade.key.RIGHT:
            self.player_x += 1

        # Keep player inside screen bounds
        self.player_x = max(0, min(GRID_WIDTH - 1, self.player_x))
        self.player_y = max(0, min(GRID_HEIGHT - 1, self.player_y))


def main():
    game = Game()
    arcade.run()


if __name__ == "__main__":
    main()