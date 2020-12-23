
# Пример ситуации, в которой шаблонный паттерн ещё не применён.
# Cеттинг - разные подходы к разработке игр у разных компаний


def create_game_by_company(game_name, company_name):
    if company_name == 'Electronic Arts' or 'Ubisoft':  # developer_team
        print('Собираем команду разработчиков...')
    elif company_name == 'Some_Indie_Developer':
        print('Команда? Да я один справлюсь.')
    else:
        print(f'Генеральный директор "{company_name}" решает пустить игру на опенсорс. Игру разрабатывают индусы.')

    print(f'Разработка {game_name} началась.')  # development_started

    if company_name == 'Electronic Arts':  # improvement over older renditions of the series
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

