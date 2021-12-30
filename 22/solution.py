import sys
import queue
import itertools

class Spell:
    def __init__(self,cost,heal,damage,armor,mana,duration):
        self.cost = cost
        self.heal = heal
        self.damage = damage
        self.armor = armor
        self.mana = mana
        self.duration = duration
        
    def __str__(self):
        return f'cost {self.cost}, heal {self.heal}, damage {self.damage}, armor {self.armor}, mana {self.mana}, duration {self.duration}'


spells = {# Name           Cost  Heal  Damage  Armor  Mana  Duration
    'Magic Missile': Spell(  53,    0,      4,     0,    0,     None),
    'Drain':         Spell(  73,    2,      2,     0,    0,     None),
    'Shield':        Spell( 113,    0,      0,     7,    0,        6),
    'Poison':        Spell( 173,    0,      3,     0,    0,        6),
    'Recharge':      Spell( 229,    0,      0,     0,  101,        5),
}
#for name,spell in spells.items():
#    print(name,spell)
#exit()

spell_names = list(spells)
class GameState:
    def __init__(self, mana_cumcost, who, player_hp, player_mana, boss_hp, boss_damage, spell_timers, history):
        self.mana_cumcost = mana_cumcost
        self.who = who
        self.player_hp = player_hp
        self.player_mana = player_mana
        self.boss_hp = boss_hp
        self.boss_damage = boss_damage
        self.spell_timers = spell_timers
        self.history = history
        
    def __str__(self):
        return f'cost: {self.mana_cumcost}, who: {self.who}, boss: {self.boss_hp}, player: {self.player_hp}+{self.player_mana}, timers {self.spell_timers}, history {self.history}'
    
    def __lt__(self,other):
        #return self.mana_cumcost < other.mana_cumcost
        if len(self.history) < len(other.history):
            return True
        else:
            return self.mana_cumcost < other.mana_cumcost
    
    def copy(self):
        return GameState(self.mana_cumcost, self.who, self.player_hp, self.player_mana, self.boss_hp, self.boss_damage, {k:v for k,v in self.spell_timers.items()}, [s for s in self.history])
    
difficulty = 0
def all_next_states(state):
    global difficulty
    if state.boss_hp <= 0:
        return True,[]
    
    for name in list(state.spell_timers):
        spell = spells[name]
        state.boss_hp -= spell.damage
        state.player_mana += spell.mana
        state.spell_timers[name] -= 1
        if state.spell_timers[name] <= 0:
            del(state.spell_timers[name])
    
    if state.boss_hp <= 0:
        return True,[]
    
    if state.who == 'boss':
        next_state = state.copy()
        next_state.who = 'player'
        next_state.player_hp -= state.boss_damage - (7 if 'Shield' in state.spell_timers else 0)
        return False,[next_state]
    
    state.player_hp -= difficulty
    if state.player_hp <= 0:
        return False,[]
    
    #print(state)
    next_states = []
    for name,spell in ( (n,s) for n,s in spells.items()
                        if s.cost <= state.player_mana and
                        (not s.duration or s not in state.spell_timers) ):
        next_state = state.copy()
        next_state.who = 'boss'
        next_state.mana_cumcost += spell.cost
        next_state.player_mana -= spell.cost
        if not spell.duration:
            next_state.player_hp += spell.heal
            next_state.boss_hp -= spell.damage
        if spell.duration:
            next_state.spell_timers[name] = spell.duration
        next_state.history.append(name)
        next_states.append(next_state)
        #print(next_state)
    #print()
    return False,next_states
            

maxturns = 0
mincost = float('inf')
minstate = None
def find_minimal_cost(start_state):
    global maxturns
    global mincost
    global minstate
    rounds = queue.PriorityQueue()
    rounds.put(start_state)
    while not rounds.empty():
        state = rounds.get()
        if len(state.history)>maxturns:
            continue
        won,next_states = all_next_states(state)
        if won and state.mana_cumcost < mincost:
            print(state)
            mincost = state.mana_cumcost
            minstate = state
        for next_state in next_states:
            rounds.put(next_state)
    return mincost,minstate


boss_hp,boss_damage = [int(l.strip().split(': ')[1]) for l in sys.stdin.readlines()]
for maxturns in itertools.count(20):
    print(maxturns)
    mincost = float('inf')
    minstate = None
    start_state = GameState(
        mana_cumcost = 0,
        who = 'player',
        player_hp = 50,
        player_mana = 500,
        boss_hp = boss_hp,
        boss_damage = boss_damage,
        spell_timers = {},
        history = [],
    )
    #print(start_state)
    difficulty = 0
    mincost,winstate = find_minimal_cost(start_state)
    if mincost<float('inf'):
        print(winstate)
        break

