import random
# build cells
CELLS = [(0,0) , (0,1) , (0,2),
        (1,0) , (1,1) , (1,2),
        (2,0) , (2,1) , (2,2),
        ]
# build random positions for monster/door/start

def get_position():
  door = random.choice(CELLS)
  monster = random.choice(CELLS)
  start = random.choice(CELLS)
  if door == monster or door == start or monster == start:
    get_position()
  return monster,door,start


# make moves for player
def make_move(player):
  MOVES = ['UP','DOWN','RIGHT','LEFT','QUIT']
  if player[0]==0:
    MOVES.remove('LEFT')
  if player[0]==2:
    MOVES.remove('RIGHT')
  if player[1]==0:
    MOVES.remove('UP') 
  if player[1]==2:
    MOVES.remove('DOWN')  
  move = input('make move in > {}  :'.format(MOVES))
  
  if move not in MOVES:
    print('can not move there')
    make_move(player)
  return move

def move_player(player,move):
  x , y = player 
  if move == 'LEFT':
    x -= 1
  if move == 'RIGHT':
    x += 1
  if move == 'UP':
    y -= 1
  if move == 'DOWN':
    y += 1
  return x,y
    
def draw_map(player):
  print(' _ _ _')
  tile = '|{}'
  for idx, cell in enumerate(CELLS):
    if idx in [0,1,3,4,6,7]:
      if cell == player:
        print(tile.format('X'),end='')
      else:
        print(tile.format('_'),end='')
    else:
      if cell == player:
        print(tile.format('X|'))
      else:
        print(tile.format('_|'))
    
  
# main loop 
monster , door , player = get_position()
while True:
  print('welcome to dungeon game!' 
        'enter QUIT to quit.'
        'you are currently in room > {}'.format(player))
  print('map:')
  print('monster is at {}, and door at {} .'.format(monster,door))
  print('(0,0) (1,0) (2,0) \n'
         '(0,1) (1,1) (2,1) \n'
         '(0,2) (1,2) (2,2) \n')
  draw_map(player)
  
  move = make_move(player)
  if move == 'QUIT':
    print('bye bye')
    break
    
  player = move_player(player,move)
  if player == door:
    print('you win')
    break
  if player == monster:
    print('you lose')
    break
  else:
    continue
    

  