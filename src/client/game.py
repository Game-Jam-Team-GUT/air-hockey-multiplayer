import config
from asset_manager import AssetManager
from board import Board
from striker import Striker


class Game:
    def __init__(self) -> None:
        self.asset_manager = AssetManager()
        self.board = Board(self.asset_manager.scale_img(self.asset_manager.board_img))
        self.strikers = []
        self.strikers.append(Striker(self.asset_manager.scale_img(self.asset_manager.striker_img),
                                     self.asset_manager.striker_img.get_height() / 2))
        self.strikers.append(Striker(self.asset_manager.scale_img(self.asset_manager.striker_img),
                                     config.WINDOW_HEIGHT - self.asset_manager.striker_img.get_height()))

    def draw(self, window):
        window.fill((255, 255, 255))
        self.board.draw(window)
        for striker in self.strikers:
            striker.draw(window)

    def update(self):
        pass
