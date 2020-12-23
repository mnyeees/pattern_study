
# Пример ситуации, в которой шаблонный паттерн ещё не применён.
# Cеттинг - разные подходы к разработке игр у разных компаний


class ElectronicArts:

    def __init__(self):
        self.game_in_development = None

    def start_development(self, game_name):
        self.game_in_development = game_name
        self.gather_developer_team()
        print('Начинаем разработку.')
        self.improve_graphics()
        print('Продолжаем разработку.')
        self.add_more_explosions()
        self.release()

    def gather_developer_team(self):
        print('Собираем команду разработчиков...')

    def improve_graphics(self):
        print('Улучшаем графоний...')

    def add_more_explosions(self):
        print('Добавляем в игру больше взрывающихся объектов...')

    def release(self):
        print(f'{self.game_in_development} готова.\n')


class Ubisoft:

    def __init__(self):
        self.game_in_development = None

    def start_development(self, game_name):
        self.game_in_development = game_name
        self.gather_developer_team()
        print('Начинаем разработку.')
        self.improve_graphics()
        print('Продолжаем разработку.')
        self.add_more_towers()
        self.release()

    def gather_developer_team(self):
        print('Собираем команду разработчиков...')

    def improve_graphics(self):
        print('Улучшаем графоний...')

    def add_more_towers(self):
        print('Добавляем в открытый мир игры побольше вышек, на которые можно забраться...')

    def release(self):
        print(f'{self.game_in_development} готова.\n')


EA = ElectronicArts()
EA.start_development(game_name='Battlefield')

UB = Ubisoft()
UB.start_development(game_name="Assassin's creed")
