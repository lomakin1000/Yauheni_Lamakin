import random
# TODO установите пакеты
# import keyboard
# import click

def randomize(state):
    coordinates = None # [(x0, y0), (x1, y1), ...]
    x, y = random.choice(coordinates)
    state[x][y] = random.choice([2, 4])
    return state
    

def show_state(state):
    
    #  TODO параметризируйте эти константы через sys.args (click) в show_state
    n_cols = 4
    n_rows = 4
    w_cell = 3
    h_cell = 1
    
    matrix = state['matrix']
    # matrix = [
    #     [2, 0, 0, 2],
    #     [2, 4, 0, 0],
    #     [2, 0, 0, 2],
    #     [2, 0, 0, 2],
    # ]
    
    # TODO вы можете поменять вывод на более приемлемый вам
    hor_line = ('+' + '-' * w_cell) * n_cols + '+\n'
    line_with_gaps = ('|' + '%s') * n_cols + '|\n'
    table = (hor_line + line_with_gaps * h_cell) * n_rows + hor_line
    
    # TODO добавьте отображение текущего и лучшего score
    print('\n' * 50)
    print(table % tuple((str(cell).center(w_cell, ' ') for row in matrix for cell in row)))

def step(state, cmd):
    n_turns = { # main direction is left
        'w': (0, 0),
        'a': (1, 3),
        's': (2, 2),
        'd': (3, 1),
    }
    before, after = n_turns[cmd]

    # turn - функция поворота матрицы на 90 гр
    '''
    [[0, 2],
     [2, 4]]
       |
       v
    [[2, 0],
     [4, 2]]
    '''
    
    # remove_zeros - функция, удаляющая из каждой строки все нули
    '''
    [[0, 0, 2],
     [2, 4, 0],
     [0, 2, 0]]
       |
       v
    [[2],
     [2, 4],
     [2]]
    '''
    
    # aggregation - в каждой строке сгруппировать соседние одинаковые элементы
    '''
    [[2, 2, 2, 2],
     [2, 4, 4],
     [2, 2, 4, 4],
     []]
       |
       v
    [[4, 4],
     [2, 8],
     [4, 8],
     []]
    '''
    
    # append_zeros - добавить справа в каждую строку нули (столько, чтоб длина строк совпадала с исходной)
    '''
    [[4, 4],
     [2, 8],
     [4, 8],
     []]
       |
       v
    [[4, 4, 0, 0],
     [2, 8, 0, 0],
     [4, 8, 0, 0],
     [0, 0, 0, 0]]
    '''
    
    # randomize - DONE
    
    # save_state - сохранить state на диск используя pickle/json
    
    # TODO реализовать псевдокод снизу    
    # repeate turn() `before` times
    # for_each row remove zeros
    # for_each  row aggregation
    # for_each  append zeros at the end
    # randomize()
    # repeate turn() `after` times
    # save_state()
    pass

def event(state, cmd):
    # TODO обрабатывать новые команды можно тут
    if cmd == 'exit':
        pass
    elif cmd == 'new':
        pass
    elif cmd in 'wasd':
        step(state, cmd)
    

# TODO добавьте click-параметры (размер сетки)
def run():
    state = dict()
    state['matrix'] = None # matrix 4x4 with initial number "2" in random cell
    state['score'] = 0
    state['best_score'] = 0 # read best score from some file
    state['is_finished'] = False
    
    # TODO сделайте инициализацию через init_state() с возможностью загрузки state с уже сохраненного раннее файла
    # state = init_state() # it's better option
    
    while True:
        event = keyboard.read_event()
        # handling keys push up
        if event.event_type != 'up': continue
        cmd = event.name
        state = event(state, cmd)
        show_state(state)
        # TODO добавьте операцию выхода из игры
        

if __name__ == '__main__':
    run()