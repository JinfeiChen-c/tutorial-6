Python 3.13.6 (v3.13.6:4e665351082, Aug  6 2025, 11:22:35) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
game.splash("Hotpot Match")

SIZE = 8

# Food images
foods = [
...     img("""
...         . . . . c c c b b b b b . . . .
...         . . c c b 4 4 4 4 4 4 b b b . .
...         . c c 4 4 4 4 4 5 4 4 4 4 b c .
...         . e 4 4 4 4 4 4 4 4 4 5 4 4 e .
...         e b 4 5 4 4 5 4 4 4 4 4 4 4 b c
...         e b 4 4 4 4 4 4 4 4 4 4 5 4 4 e
...         e b b 4 4 4 4 4 4 4 4 4 4 4 b e
...         . e b 4 4 4 4 4 5 4 4 4 4 b e .
...         8 7 e e b 4 4 4 4 4 4 b e e 6 8
...         8 7 2 e e e e e e e e e e 2 7 8
...         e 6 6 2 2 2 2 2 2 2 2 2 2 6 c e
...         e c 6 7 6 6 7 7 7 6 6 7 6 c c e
...         e b e 8 8 c c 8 8 c c c 8 e b e
...         e e b e c c e e e e e c e b e e
...         . e e b b 4 4 4 4 4 4 4 4 e e .
...         . . . c c c c c e e e e e . . .
...     """),
...     img("""
...     . . . . . . . e c 7 . . . . . .
...     . . . . e e e c 7 7 e e . . . .
...     . . c e e e e c 7 e 2 2 e e . .
...     . c e e e e e c 6 e e 2 2 2 e .
...     . c e e e 2 e c c 2 4 5 4 2 e .
...     c e e e 2 2 2 2 2 2 4 5 5 2 2 e
...     c e e 2 2 2 2 2 2 2 2 4 4 2 2 e
...     c e e 2 2 2 2 2 2 2 2 2 2 2 2 e
...     c e e 2 2 2 2 2 2 2 2 2 2 2 2 e
...     c e e 2 2 2 2 2 2 2 2 2 2 2 2 e
...     c e e 2 2 2 2 2 2 2 2 2 2 4 2 e
...     . e e e 2 2 2 2 2 2 2 2 2 4 e .
...     . 2 e e 2 2 2 2 2 2 2 2 4 2 e .
...     . . 2 e e 2 2 2 2 2 4 4 2 e . .
...     . . . 2 2 e e 4 4 4 2 e e . . .
...     . . . . . 2 2 e e e e . . . . .
...     """),
...     img("""
...     4 4 4 . . 4 4 4 4 4 . . . . . .
...     4 5 5 4 4 5 5 5 5 5 4 4 . . . .
...     b 4 5 5 1 5 1 1 1 5 5 5 4 . . .
    . b 5 5 5 5 1 1 5 5 1 1 5 4 . .
    . b d 5 5 5 5 5 5 5 5 1 1 5 4 .
    b 4 5 5 5 5 5 5 5 5 5 5 1 5 4 .
    c d 5 5 5 5 5 5 5 5 5 5 5 5 5 4
    c d 4 5 5 5 5 5 5 5 5 5 5 1 5 4
    c 4 5 5 5 d 5 5 5 5 5 5 5 5 5 4
    c 4 d 5 4 5 d 5 5 5 5 5 5 5 5 4
    . c 4 5 5 5 5 d d d 5 5 5 5 5 b
    . c 4 d 5 4 5 d 4 4 d 5 5 5 4 c
    . . c 4 4 d 4 4 4 4 4 d d 5 d c
    . . . c 4 4 4 4 4 4 4 4 5 5 5 4
    . . . . c c b 4 4 4 b b 4 5 4 4
    . . . . . . c c c c c c b b 4 .
    """),
    img("""
    . . 2 2 b b b b b . . . . . . .
    . 2 b 4 4 4 4 4 4 b . . . . . .
    2 2 4 4 4 4 d d 4 4 b . . . . .
    2 b 4 4 4 4 4 4 d 4 b . . . . .
    2 b 4 4 4 4 4 4 4 d 4 b . . . .
    2 b 4 4 4 4 4 4 4 4 4 b . . . .
    2 b 4 4 4 4 4 4 4 4 4 e . . . .
    2 2 b 4 4 4 4 4 4 4 b e . . . .
    . 2 b b b 4 4 4 b b b e . . . .
    . . e b b b b b b b e e . . . .
    . . . e e b 4 4 b e e e b . . .
    . . . . . e e e e e e b d b b .
    . . . . . . . . . . . b 1 1 1 b
    . . . . . . . . . . . c 1 d d b
    . . . . . . . . . . . c 1 b c .
    . . . . . . . . . . . . c c . .
    """),
    img("""
    . . . . . . 2 2 2 2 . . . . . .
    . . . . 2 2 3 3 3 3 2 e . . . .
    . . . 2 3 d 1 1 d d 3 2 e . . .
    . . 2 3 1 d 3 3 3 d d 3 e . . .
    . 2 3 1 3 3 3 3 3 d 1 3 b e . .
    . 2 1 d 3 3 3 3 d 3 3 1 3 b b .
    2 3 1 d 3 3 1 1 3 3 3 1 3 4 b b
    2 d 3 3 d 1 3 1 3 3 3 1 3 4 4 b
    2 d 3 3 3 1 3 1 3 3 3 1 b 4 4 e
    2 d 3 3 3 1 1 3 3 3 3 1 b 4 4 e
    e d 3 3 3 3 d 3 3 3 d d b 4 4 e
    e d d 3 3 3 d 3 3 3 1 3 b 4 b e
    e 3 d 3 3 1 d d 3 d 1 b b e e .
    . e 3 1 1 d d 1 1 1 b b e e e .
    . . e 3 3 3 3 3 3 b e e e e . .
    . . . e e e e e e e e e e . . .
    """)
]

board: List[List[number]] = None
sprites2: List[List[Sprite]] = None
row = 0
col = 0
pick: List[number] = None
cur: Sprite = None

def init():
    global board, sprites2
    scene.set_background_color(9)
    info.set_score(0)
    board = []
    sprites2 = []
    for r in range(SIZE):
        board.append([])
        sprites2.append([])
        for c in range(SIZE):
            board[r].append(randint(0, 4))
            sprites2[r].append(None)
    draw()
    makeCur()
    clear()

def draw():
    for r in range(SIZE):
        for c in range(SIZE):
            if sprites2[r][c]:
                sprites2[r][c].destroy()
            s = sprites.create(foods[board[r][c]])
            s.set_position(c * 16 + 16, r * 16 + 16)
            sprites2[r][c] = s

def makeCur():
    global cur
    cur = sprites.create(img("""
7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
7 . . . . . . . . . . . . . . 7
7 . . . . . . . . . . . . . . 7
7 . . . . . . . . . . . . . . 7
7 . . . . . . . . . . . . . . 7
7 . . . . . . . . . . . . . . 7
7 . . . . . . . . . . . . . . 7
7 . . . . . . . . . . . . . . 7
7 . . . . . . . . . . . . . . 7
7 . . . . . . . . . . . . . . 7
7 . . . . . . . . . . . . . . 7
7 . . . . . . . . . . . . . . 7
7 . . . . . . . . . . . . . . 7
7 . . . . . . . . . . . . . . 7
7 . . . . . . . . . . . . . . 7
7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
"""))
    cur.set_position(16, 16)

def check():
    found: List[List[number]] = []
    for r in range(SIZE):
        for c in range(SIZE - 2):
            if board[r][c] == board[r][c+1] and board[r][c] == board[r][c+2]:
                found.append([r, c])
                found.append([r, c+1])
                found.append([r, c+2])
    for c in range(SIZE):
        for r in range(SIZE - 2):
            if board[r][c] == board[r+1][c] and board[r][c] == board[r+2][c]:
                found.append([r, c])
                found.append([r+1, c])
                found.append([r+2, c])
    return found

def clear():
    m = check()
    if len(m) > 0:
        for i in range(len(m)):
            r = m[i][0]
            c = m[i][1]
            if sprites2[r][c]:
                sprites2[r][c].destroy()
                sprites2[r][c] = None
                board[r][c] = -1
        info.change_score_by(len(m) * 10)
        pause(200)
        fill()
        pause(200)
        clear()

def fill():
    for c in range(SIZE):
        for r in range(SIZE - 1, -1, -1):
            if board[r][c] == -1:
                for r2 in range(r - 1, -1, -1):
                    if board[r2][c] != -1:
                        board[r][c] = board[r2][c]
                        sprites2[r][c] = sprites2[r2][c]
                        board[r2][c] = -1
                        sprites2[r2][c] = None
                        if sprites2[r][c]:
                            sprites2[r][c].set_position(c * 16 + 16, r * 16 + 16)
                        break
    for c in range(SIZE):
        for r in range(SIZE):
            if board[r][c] == -1:
                board[r][c] = randint(0, 4)
                s = sprites.create(foods[board[r][c]])
                s.set_position(c * 16 + 16, r * 16 + 16)
                sprites2[r][c] = s

def swap(r1: number, c1: number, r2: number, c2: number):
    t = board[r1][c1]
    board[r1][c1] = board[r2][c2]
    board[r2][c2] = t
    ts = sprites2[r1][c1]
    sprites2[r1][c1] = sprites2[r2][c2]
    sprites2[r2][c2] = ts
    if sprites2[r1][c1]:
        sprites2[r1][c1].set_position(c1 * 16 + 16, r1 * 16 + 16)
    if sprites2[r2][c2]:
        sprites2[r2][c2].set_position(c2 * 16 + 16, r2 * 16 + 16)

def on_up():
    global row
    if row > 0:
        row -= 1
        cur.set_position(col * 16 + 16, row * 16 + 16)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up)

def on_down():
    global row
    if row < 7:
        row += 1
        cur.set_position(col * 16 + 16, row * 16 + 16)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down)

def on_left():
    global col
    if col > 0:
        col -= 1
        cur.set_position(col * 16 + 16, row * 16 + 16)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left)

def on_right():
    global col
    if col < 7:
        col += 1
        cur.set_position(col * 16 + 16, row * 16 + 16)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right)

def on_a():
    global pick
    if pick == None:
        pick = [row, col]
    else:
        r1 = pick[0]
        c1 = pick[1]
        r2 = row
        c2 = col
        if (abs(r1-r2)==1 and c1==c2) or (abs(c1-c2)==1 and r1==r2):
            swap(r1, c1, r2, c2)
            pause(200)
            if len(check()) > 0:
                clear()
            else:
                swap(r1, c1, r2, c2)
        pick = None
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a)

