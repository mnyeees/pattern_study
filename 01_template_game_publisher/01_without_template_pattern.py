
# Пример ситуации, в которой шаблонный паттерн ещё не применён.
# Cеттинг - разные подходы к разработке игр у разных компаний
import random
import time

from tqdm import tqdm

def gather_dev_team(company_name):
    print(f'{company_name}: Собираем команду разработчиков...')
    for i in tqdm(['11', '22', '33', ]):
        print(i)
        time.sleep(.5)
    return random.randint(5, 100)


def sigle_uno_dev(company_name):
    print(f'Генеральный директор "{company_name}" решает пустить игру на опенсорс. Игру разрабатывают индусы.')
    return random.randint(1000, 10000)


def create_game_by_company(game_name, company_name):
    if company_name == 'Electronic Arts' or 'Ubisoft':  # developer_team
        num_staff = gather_dev_team(company_name)
    elif company_name == 'Some_Indie_Developer':
        print('Команда? Да я один справлюсь.')
        num_staff = 1
    else:
        num_staff = sigle_uno_dev(company_name)

    print(f'Разработка {game_name} началась.')  # development_started

    if company_name == 'Electronic Arts':  # improvement over older renditions of the series
        if num_staff < 10:
            print('И так сойдет')
        else:
            print('Больше зрелищных катсцен и взрывающихся вертолетов!')
    elif company_name == 'Ubisoft':
        print('Улучшаем графоний, а в остальном оставляем всё также - формула не подводит.')
    elif company_name == 'Some_Indie_Developer':
        print('У меня сейчас сессия, так что я отложу пока разработку.')
    else:
        print('Коллективное бессознательное индусов-опенсорсников насыщает игру задорной музыкой, танцами '
              'и вулканами страстей.')

    if company_name == 'Some_Indie_Developer': # development_continues
        print('Отчислили. Ну да ладно, игрой займусь.')
    else:
        print(f'Разработка {game_name} продолжается.')

    if company_name == 'Electronic Arts': # distinctive feature
        print('"Ты уверен, что имеющихся взрывов и катсцен хватит? Может ещё добавим?"')
    elif company_name == 'Ubisoft':
        print('Разработка практически окончена, мир, как мы и хотели, открытый, '
              'но не хватает последнего штриха - вышек.')
    elif company_name == 'Some_Indie_Developer':
        print('Сюжет игры будет разворачиваться вокруг непростой жизни антропоморфного горного барана Сергея,'
              'страдающего сонными параличами. Каждый уровень будет одним из его снов, '
              'раскрывающих завесу тайны его жизни.'
              'Господи, да я же гениальный писатель, к черту этот вуз.')
    else:
        print('ТУТ_ВАРИАНТ_С_ИНДУСАМИ_КОТОРЫЙ_Я_ЕЩЁ_НЕ_ПРИДУМАЛ_')

    print('РЕЛИЗ_ДОПИШУ_ПОЗЖЕ')


def electronic_arts(game_name):

    def gather_dev_team():
        print('Собираем команду разработчиков...')

    def start_development():
        print(f'Разработка {game_name} началась.')

    def distinctive_feature():
        print('Добавляем больше зрелищных катсцен и взрывающихся вертолетов.')

    def finish():
        print('Последние этапы разработки...')

    def release():
        print(f'Релиз {game_name}.\n')

    def run():
        gather_dev_team()
        start_development()
        distinctive_feature()
        finish()
        release()

    run()


def ubisoft(game_name):

    def gather_dev_team():
        print('Собираем команду разработчиков...')

    def start_development():
        print(f'Разработка {game_name} началась.')

    def distinctive_feature():
        print('Добавляем в открытый мир игры побольше вышек, на которые можно забраться.')

    def finish():
        print('Последние этапы разработки...')

    def release():
        print(f'Релиз {game_name}.\n')

    def run():
        gather_dev_team()
        start_development()
        distinctive_feature()
        finish()
        release()

    run()


# electronic_arts('Battlefield')
# ubisoft('assasins creed')

gather_dev_team('zx')
