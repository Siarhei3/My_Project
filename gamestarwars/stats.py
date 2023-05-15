class Stats():# отслеживание статистики
    def __init__(self): # иницилизация статистики
        self.reset_stats()
        self.run_game = True
        with open('hight_score.txt', 'r') as f:
            self.hight_score =int(f.readline())

    def reset_stats(self): # статистика во время игры
        self.guns_left = 2
        self.score = 0



