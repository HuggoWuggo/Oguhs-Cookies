# Made By Thomas McLean

import pygame as py, sys

def init(data_set):

    if data_set == [] or type(data_set) is not list:
        print('Missing Data Argument')
        py.quit()
        sys.exit()

    py.init()

    fps = 10
    time = py.time.Clock()
    width = 800 
    height = 600 
    fill_colour = 'white'
    run = True
    font = py.font.SysFont(None, 50)

    screen = py.display.set_mode([width, height])

    try:
        icon = py.image.load('C:\\Users\\anna_\\OneDrive\\Desktop\\Coding\\Python Files\\Graphene\\Graphene.jpg')
    except:
        pass

    py.display.set_caption('Graphene')
    py.display.set_icon(icon)

    return screen, width, height, fps, time, fill_colour, run, font

def draw_menu(screen, width, height):
    py.draw.line(screen, 'black', (100, height - 100), (width - 100, height - 100), 5) # x axis
    py.draw.line(screen, 'black', (100, height - 100), (100, 100), 5) # y axis

def dot(data_set=[], draw_connecting_lines=True, dot_size=15):
    
    screen, width, height, fps, time, fill_colour, run, font = init(data_set)

    while run:
        time.tick(fps)
        screen.fill(fill_colour)

        draw_menu(screen, width, height)

        plot_dots(screen, width, height, data_set, draw_connecting_lines, dot_size, font)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        py.display.flip()
    py.quit()

def plot_dots(screen, width, height, data_set, draw_connecting_lines, dot_size, font):
    x_max_dist = width - 200
    y_max_dist = height - 200

    y_spread = y_max_dist / max(data_set)

    if isinstance(max(data_set), float):
        y_spread = y_max_dist / round(max(data_set) + 0.4999)

    point_pos = [(100, height - 100)]

    for c in range(len(data_set)):
        distx = x_max_dist / len(data_set) * (c + 1)
        disty = y_spread * data_set[c]
        py.draw.circle(screen, 'black', (100 + distx, height - 100 - disty), dot_size)
        py.draw.line(screen, 'black', (100 + distx, height - 115), (100 + distx, height - 85), 3)
        if len(data_set) > 12:
            font = py.font.SysFont(None, 50 - round(0.85 * len(data_set)))
            img = font.render(str(c + 1), True, (0, 0, 0))
            screen.blit(img, (102 + distx - (10 - 0.15 * len(data_set)) * len(str(c + 1)), height - 80))
        else:
            img = font.render(str(c + 1), True, (0, 0, 0))
            screen.blit(img, (102 + distx - 10 * len(str(c + 1)), height - 80))
        point_pos.append((100 + distx, height - 100 - disty))

    font = py.font.SysFont(None, 50)

    if max(data_set) > 10:
        for i in range(10):
            py.draw.line(screen, 'black', (85, height - 100 - y_max_dist / 10 * (i + 1)), (115, height - 100 - y_max_dist / 10 * (i + 1)), 3)
            if round(max(data_set) / 10 * (i + 1), 1) - int(round(max(data_set) / 10 * (i + 1), 1)) == 0:
                text = str(int(round(max(data_set) / 10 * (i + 1), 1)))
            else:
                text = str(round(max(data_set) / 10 * (i + 1), 1))
            img = font.render(text, True, (0, 0, 0))
            screen.blit(img, (70 - 15 * len(text), height - 115 - y_max_dist / 10 * (i + 1)))

    else:
        for i in range(round(max(data_set) + 0.4999)):
            py.draw.line(screen, 'black', (85, height - 100 - y_spread * (i + 1)), (115, height - 100 - y_spread * (i + 1)), 3)
            img = font.render(str(i + 1), True, (0, 0, 0))
            screen.blit(img, (75 - 18 * len(str(i + 1)), height - 115 - y_spread * (i + 1)))

    if draw_connecting_lines:
        py.draw.lines(screen, 'black', False, point_pos, 5)

def bar(data_set=[], bar_size=30):
    
    screen, width, height, fps, time, fill_colour, run, font = init(data_set)

    while run:
        time.tick(fps)
        screen.fill(fill_colour)

        draw_menu(screen, width, height)

        plot_bars(screen, width, height, data_set, bar_size, font)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        py.display.flip()
    py.quit()

def plot_bars(screen, width, height, data_set, bar_size, font):
    x_max_dist = width - 200
    y_max_dist = height - 200

    y_spread = y_max_dist / max(data_set)

    if isinstance(max(data_set), float):
        y_spread = y_max_dist / round(max(data_set) + 0.4999)

    for c in range(len(data_set)):
        distx = x_max_dist / len(data_set) * (c + 1)
        disty = y_spread * data_set[c]
        py.draw.line(screen, 'black', (100 + distx, height - 98), (100 + distx, height - 100 - disty), bar_size)
        if len(data_set) > 12:
            font = py.font.SysFont(None, 50 - round(0.85 * len(data_set)))
            img = font.render(str(c + 1), True, (0, 0, 0))
            screen.blit(img, (102 + distx - (10 - 0.15 * len(data_set)) * len(str(c + 1)), height - 80))
        else:
            img = font.render(str(c + 1), True, (0, 0, 0))
            screen.blit(img, (102 + distx - 10 * len(str(c + 1)), height - 80))
        
    font = py.font.SysFont(None, 50)

    if max(data_set) > 10:
        for i in range(10):
            py.draw.line(screen, 'black', (85, height - 100 - y_max_dist / 10 * (i + 1)), (115, height - 100 - y_max_dist / 10 * (i + 1)), 3)
            if round(max(data_set) / 10 * (i + 1), 1) - int(round(max(data_set) / 10 * (i + 1), 1)) == 0:
                text = str(int(round(max(data_set) / 10 * (i + 1), 1)))
            else:
                text = str(round(max(data_set) / 10 * (i + 1), 1))
            img = font.render(text, True, (0, 0, 0))
            screen.blit(img, (70 - 15 * len(text), height - 115 - y_max_dist / 10 * (i + 1)))

    else:
        for i in range(round(max(data_set) + 0.4999)):
            py.draw.line(screen, 'black', (85, height - 100 - y_spread * (i + 1)), (115, height - 100 - y_spread * (i + 1)), 3)
            img = font.render(str(i + 1), True, (0, 0, 0))
            screen.blit(img, (75 - 18 * len(str(i + 1)), height - 115 - y_spread * (i + 1)))

def scatter(data_set=[], dot_size=15):
    
    screen, width, height, fps, time, fill_colour, run, font = init(data_set)

    while run:
        time.tick(fps)
        screen.fill(fill_colour)

        draw_menu(screen, width, height)

        plot_scatter(screen, width, height, data_set, dot_size, font)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        py.display.flip()
    py.quit()

def plot_scatter(screen, width, height, data_set, dot_size, font):
    x_max_dist = width - 200
    y_max_dist = height - 200
  
    x_spread = x_max_dist
    x_spread = min([x_max_dist / x[0] for x in data_set if x_spread > x_max_dist / x[0]])

    y_spread = y_max_dist
    y_spread = min([y_max_dist / y[1] for y in data_set if y_spread > y_max_dist / y[1]])

    if isinstance(y_max_dist / y_spread, float):
        y_spread = y_max_dist / round(y_max_dist / y_spread + 0.4999)

    for c in range(len(data_set)):
        distx = x_max_dist / (x_max_dist / x_spread) * data_set[c][0]
        disty = y_spread * data_set[c][1]
        py.draw.circle(screen, 'black', (100 + distx, height - 100 - disty), dot_size)

    for j in range(int(x_max_dist / x_spread)):
        py.draw.line(screen, 'black', (100 + x_spread * (j + 1), height - 115), (100 + x_spread * (j + 1), height - 85), 3)
        if x_max_dist / x_spread > 12:
            font = py.font.SysFont(None, 50 - round(0.85 * x_max_dist / x_spread))
            img = font.render(str(j + 1), True, (0, 0, 0))
            screen.blit(img, (102 + x_spread * (j + 1) - (10 - 0.15 * x_max_dist / x_spread) * len(str(j + 1)), height - 80))
        else:
            img = font.render(str(j + 1), True, (0, 0, 0))
            screen.blit(img, (102 + x_spread * (j + 1) - 10 * len(str(j + 1)), height - 80))\

    font = py.font.SysFont(None, 50)

    if y_max_dist / y_spread > 10:
        for i in range(10):
            py.draw.line(screen, 'black', (85, height - 100 - y_max_dist / 10 * (i + 1)), (115, height - 100 - y_max_dist / 10 * (i + 1)), 3)
            if round(y_max_dist / y_spread / 10 * (i + 1), 1) - int(round(y_max_dist / y_spread / 10 * (i + 1), 1)) == 0:
                text = str(int(round(y_max_dist / y_spread / 10 * (i + 1), 1)))
            else:
                text = str(round(y_max_dist / y_spread / 10 * (i + 1), 1))
            img = font.render(text, True, (0, 0, 0))
            screen.blit(img, (70 - 15 * len(text), height - 115 - y_max_dist / 10 * (i + 1)))

    else:
        for i in range(round(y_max_dist / y_spread + 0.4999)):
            py.draw.line(screen, 'black', (85, height - 100 - y_max_dist / round(y_max_dist / y_spread + 0.4999) * (i + 1)), (115, height - 100 - y_max_dist / round(y_max_dist / y_spread + 0.4999) * (i + 1)), 3)
            img = font.render(str(i + 1), True, (0, 0, 0))
            screen.blit(img, (75 - 18 * len(str(i + 1)), height - 115 - y_spread * (i + 1)))
