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

def draw_menu(screen, width, height):
    py.draw.line(screen, 'black', (100, height - 100), (width - 100, height - 100), 5) # x axis
    py.draw.line(screen, 'black', (100, height - 100), (100, 100), 5) # y axis

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

    elif isinstance(max(data_set), float):
        for i in range(round(max(data_set) + 0.4999)):
            py.draw.line(screen, 'black', (85, height - 100 - y_spread * (i + 1)), (115, height - 100 - y_spread * (i + 1)), 3)
            img = font.render(str(i + 1), True, (0, 0, 0))
            screen.blit(img, (75 - 18 * len(str(i + 1)), height - 115 - y_spread * (i + 1)))
    
    else:
        for i in range(max(data_set)):
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

    elif isinstance(max(data_set), float):
        for i in range(round(max(data_set) + 0.4999)):
            py.draw.line(screen, 'black', (85, height - 100 - y_spread * (i + 1)), (115, height - 100 - y_spread * (i + 1)), 3)
            img = font.render(str(i + 1), True, (0, 0, 0))
            screen.blit(img, (75 - 18 * len(str(i + 1)), height - 115 - y_spread * (i + 1)))

    else:
        for i in range(max(data_set)):
            py.draw.line(screen, 'black', (85, height - 100 - y_spread * (i + 1)), (115, height - 100 - y_spread * (i + 1)), 3)
            img = font.render(str(i + 1), True, (0, 0, 0))
            screen.blit(img, (75 - 18 * len(str(i + 1)), height - 115 - y_spread * (i + 1)))