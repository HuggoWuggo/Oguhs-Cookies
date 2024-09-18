import pygame as py

def graph(data_set=[], draw_connecting_lines=True, dot_size=15):
    run = True

    if data_set == []:
        print('Missing Data Argument')
        run = False

    if run:
        py.init()

        fps = 10
        time = py.time.Clock()
        width = 800
        height = 600
        fill_colour = 'white'

        screen = py.display.set_mode([width, height])

        try:
            icon = py.image.load('C:\\Users\\anna_\\OneDrive\\Desktop\\Coding\\Python Files\\Graphene\\Graphene.jpg')
        except:
            pass

        py.display.set_caption('Graphene')
        py.display.set_icon(icon)

    while run:
        time.tick(fps)
        screen.fill(fill_colour)

        draw_menu(screen, width, height)

        if len(data_set) > 0:
            plot_data(screen, width, height, data_set, draw_connecting_lines, dot_size)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        py.display.flip()
    py.quit()

def draw_menu(screen, width, height):
    py.draw.line(screen, 'black', (100, height - 100), (width - 100, height - 100), 5) # x axis
    py.draw.line(screen, 'black', (100, height - 100), (100, 100), 5) # y axis

def plot_data(screen, width, height, data_set, draw_connecting_lines, dot_size):
    x_max_dist = width - 200
    y_max_dist = height - 200

    y_spread = y_max_dist / max(data_set)

    point_pos = [(100, height - 100)]

    for c in range(len(data_set)):
        distx = x_max_dist / len(data_set) * (c + 1)
        disty = y_spread * data_set[c]
        py.draw.circle(screen, 'black', (100 + distx, height - 100 - disty), dot_size)
        py.draw.line(screen, 'black', (100 + distx, height - 115), (100 + distx, height - 85), 3)
        point_pos.append((100 + distx, height - 100 - disty))

    if max(data_set) > 10:
        for i in range(10):
            py.draw.line(screen, 'black', (85, height - 100 - y_max_dist / 10 * (i + 1)), (115, height - 100 - y_max_dist / 10 * (i + 1)), 3)
    
    else:
        for i in range(max(data_set)):
            py.draw.line(screen, 'black', (85, height - 100 - y_spread * (i + 1)), (115, height - 100 - y_spread * (i + 1)), 3)

    if draw_connecting_lines:
        py.draw.lines(screen, 'black', False, point_pos, 5)