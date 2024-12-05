import pygame as py, Pypoint

py.init()

fps = 120
time = py.time.Clock()
width = 800
height = 600
active_size = 20
fill_colour = 'white'
active_colour = 'red'
vertex_list = []
parts_list = []
parts_colour_list = []
painting = []
drawing_line = False
drawing_paint = False
joining = False

screen = py.display.set_mode([width, height])

try:
    icon = py.image.load('C:\\Users\\anna_\\OneDrive\\Desktop\\Pictures\\Icon.jpg')
except:
    pass

py.display.set_icon(icon)
py.display.set_caption("PageMate")

def draw_menu(active_size, active_colour):
    py.draw.rect(screen, 'gray', [0, 0, width, 70])
    py.draw.line(screen, 'black', (0, 70), (width, 70), 3)

    line_tool = py.draw.rect(screen, "black", [10, 10, 50, 50])
    py.draw.line(screen, 'white', (20, 20), (50, 50), 7)

    xl_brush = py.draw.rect(screen, 'black', [70, 10, 50, 50])
    py.draw.circle(screen, 'white', (95, 35), 20)
    l_brush = py.draw.rect(screen, 'black', [130, 10, 50, 50])
    py.draw.circle(screen, 'white', (155, 35), 15)
    m_brush = py.draw.rect(screen, 'black', [190, 10, 50, 50])
    py.draw.circle(screen, 'white', (215, 35), 10)
    s_brush = py.draw.rect(screen, 'black', [250, 10, 50, 50])
    py.draw.circle(screen, 'white', (275, 35), 5)

    blue = py.draw.rect(screen, (0, 0, 255), [width - 35, 10, 25, 25])
    red = py.draw.rect(screen, (255, 0, 0), [width - 35, 35, 25, 25])
    green = py.draw.rect(screen, (0, 255, 0), [width - 60, 10, 25, 25])
    yellow = py.draw.rect(screen, (255, 255, 0), [width - 60, 35, 25, 25])
    teal = py.draw.rect(screen, (0, 255, 255), [width - 85, 10, 25, 25])
    purple = py.draw.rect(screen, (255, 0, 255), [width - 85, 35, 25, 25])
    white = py.draw.rect(screen, (0, 0, 0), [width - 110, 10, 25, 25])
    black = py.draw.rect(screen, (255, 255, 255), [width - 110, 35, 25, 25])

    fill_tool = py.draw.circle(screen, 'black', (width / 2, 35), 25)
    py.draw.rect(screen, 'white', [width / 2 - 13, 22.5, 27, 27])
    py.draw.rect(screen, 'black', [width / 2 - 9, 22.5, 18, 22])
    py.draw.rect(screen, active_colour, [width / 2 - 9, 35, 18, 10])

    if drawing_paint:
        if active_size == 20:
            py.draw.rect(screen, 'green', [70, 10, 50, 50], 3)
            py.draw.circle(screen, active_colour, (95, 35), 20)
        elif active_size == 15:
            py.draw.rect(screen, 'green', [130, 10, 50, 50], 3)
            py.draw.circle(screen, active_colour, (155, 35), 15)
        elif active_size == 10:
            py.draw.rect(screen, 'green', [190, 10, 50, 50], 3)
            py.draw.circle(screen, active_colour, (215, 35), 10)
        elif active_size == 5:
            py.draw.rect(screen, 'green', [250, 10, 50, 50], 3)
            py.draw.circle(screen, active_colour, (275, 35), 5)

    if drawing_line:
        py.draw.rect(screen, 'green', [10, 10, 50, 50], 3)
        py.draw.line(screen, active_colour, (20, 20), (50, 50), 7)

    brush_list = [xl_brush, l_brush, m_brush, s_brush]
    colour_list = [blue, red, green, yellow, teal, purple, white, black]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]

    return line_tool, fill_tool, brush_list, colour_list, rgb_list

def draw_vertices(vertex_list):
    for i in range(len(vertex_list) - 1):
        py.draw.line(screen, active_colour, vertex_list[i], vertex_list[i + 1], 5)

def draw_parts(parts_list):
    for p in range(len(parts_list)):
        for v in range(len(parts_list[p]) - 1):
            py.draw.line(screen, parts_colour_list[p], parts_list[p][v], parts_list[p][v + 1], 5)

def vertex_clicked(vertex_list, event):
    joining = False
    for vertex in vertex_list:

        if Pypoint.diff([vertex, event.pos], 25) == True:
            joining = add_joining(joining, vertex_list, vertex, parts_list)
            return joining

        # if event.pos[0] > vertex[0] and event.pos[1] > vertex[1]:
        #     if event.pos[0] - vertex[0] < 25 and event.pos[1] - vertex[1] < 25:
        #        joining = add_joining(joining, vertex_list, vertex, parts_list)
        #         return joining
        # if event.pos[0] < vertex[0] and event.pos[1] < vertex[1]:
        #     if vertex[0] - event.pos[0] < 25 and vertex[1] - event.pos[1] < 25:
        #         joining = add_joining(joining, vertex_list, vertex, parts_list)
        #         return joining
        # if event.pos[0] > vertex[0] and event.pos[1] < vertex[1]:
        #     if event.pos[0] - vertex[0] < 25 and vertex[1] - event.pos[1] < 25:
        #         joining = add_joining(joining, vertex_list, vertex, parts_list)
        #         return joining
        # if event.pos[0] < vertex[0] and event.pos[1] > vertex[1]:
        #     if vertex[0] - event.pos[0] < 25 and event.pos[1] - vertex[1] < 25:
        #         joining = add_joining(joining, vertex_list, vertex, parts_list)
        #         return joining
            
def add_joining(joining, vertex_list, vertex, parts_list):
    joining = True
    parts_colour_list.append(active_colour)
    vertex_list.append(vertex)
    parts_list.append(vertex_list)
    del vertex_list
    vertex_list = []
    return joining

def render_vertex_square(vertex_list):
    for vertex in vertex_list:
        vertex_rect = py.Rect(vertex[0] - 10, vertex[1] - 10, 20, 20)
        if vertex_rect.collidepoint(mouse):
            py.draw.rect(screen, 'black', vertex_rect)

def draw_painting(painting):
    for i in range(len(painting)):
        py.draw.circle(screen, painting[i][0], painting[i][1], painting[i][2])

run = True
while run:
    time.tick(fps)
    screen.fill(fill_colour)
    mouse = py.mouse.get_pos()
    left_click = py.mouse.get_pressed()[0]
    right_click = py.mouse.get_pressed()[2]

    if left_click and mouse[1] > 70 and not drawing_line and drawing_paint:
        painting.append((active_colour, mouse, active_size))

    draw_painting(painting)

    line_tool, fill_tool, brushes, colours, rgbs = draw_menu(active_size, active_colour)

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

        if event.type == py.MOUSEBUTTONDOWN:
            
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    drawing_line = False
                    parts_colour_list.append(active_colour)
                    parts_list.append(vertex_list)
                    del vertex_list
                    vertex_list = []
                    drawing_paint = not drawing_paint
                    active_size = 20 - (i * 5)

            for i in range(len(colours)):
                if colours[i].collidepoint(event.pos):
                    active_colour = rgbs[i]

            if fill_tool.collidepoint(event.pos):
                fill_colour = active_colour

            if len(vertex_list) > 1:
                joining = vertex_clicked(vertex_list, event)

            if line_tool.collidepoint(event.pos) or joining:
                drawing_line = not drawing_line
                drawing_paint = False
                joining = False

                if not drawing_line:
                    parts_colour_list.append(active_colour)
                    parts_list.append(vertex_list)
                    del vertex_list
                    vertex_list = []
                break

            if drawing_line and mouse[1] > 70 and not joining:
                vertex_list.append(mouse)

    if len(vertex_list) > 1:
        draw_vertices(vertex_list)
        render_vertex_square(vertex_list)

    if len(parts_list) > 0:
        draw_parts(parts_list)

    py.display.flip()
py.quit()