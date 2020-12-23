
# Пример использования шаблонного метода

from abc import abstractmethod, ABC


class GamePublisher(ABC):

    def __init__(self):
        self.game_in_development = None

    def start_development(self, game_name):
        self.game_in_development = game_name
        self.gather_developer_team()
        print('Начинаем разработку.')
        self.make_improvements()
        print('Продолжаем разработку.')
        self.add_distinctive_feature()
        self.release()

    def gather_developer_team(self):
        print('Собираем команду разработчиков...')

    @abstractmethod
    def make_improvements(self):
        pass

    @abstractmethod
    def add_distinctive_feature(self):
        pass

    def release(self):
        print(f'{self.game_in_development} готова.\n')


class ElectronicArts(GamePublisher):

    def make_improvements(self):
        print(f'Добавляем в {self.game_in_development} новые модельки оружия')

    def add_distinctive_feature(self):
        print(f'БОЛЬШЕ ВЗРЫВОВ БОГУ ВЗРЫВОВ')


class Ubisoft(GamePublisher):

    def make_improvements(self):
        print('Улучшаем графоний...')

    def add_distinctive_feature(self):
        print('Добавляем в игру побольше вышек')


class Bethesda(GamePublisher):

    def start_development(self, game_name):
        self.game_in_development = game_name
        self.gather_developer_team()
        print('Начинаем разработку.')
        self.make_improvements()
        print('Недостаточно багов. Добавим ещё.')
        self.add_distinctive_feature()
        self.release()

    def make_improvements(self):
        print('Добавляем баги.')

    def add_distinctive_feature(self):
        print('Делаем графон красочнее, у нас же тут пост-апокалипсис как никак. '
              'Ну и ещё пару сотен багов, чтобы наверняка.')


EA = ElectronicArts()
EA.start_development(game_name='Battlefield')

UB = Ubisoft()
UB.start_development(game_name="Assassin's creed")

BD = Bethesda()
BD.start_development(game_name='Fallout 76')
