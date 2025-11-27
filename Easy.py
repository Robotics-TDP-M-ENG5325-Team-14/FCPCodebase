from agent.Base_Agent import Base_Agent as Agent
from math_ops.Math_Ops import Math_Ops as M
from scripts.commons.Script import Script


script = Script()
a = script.args


# Args: Server IP, Agent Port, Monitor Port, Uniform No., Robot Type, Team Name
# This could be done in 1 line, but calling batch_create twice enhances readability

script1.batch_create(Agent, ((a1.i,a1.p,a1.m,u+1,a1.r,"Easy") for u in range(4)) )

players = script.players
p_num = len(players)



positions = [
    (-14, 0, 0.5, 0),
    (-8, 3, 0.5, 0),
    (-8, -3, 0.5, 0),
    (-3, 0, 0.5, 0),
   
]

script.batch_unofficial_beam(positions)
getting_up = [False]*p_num

 

while True:
   for i in range(p_num):
        p = players[i]
        w = p.world


        player_2d = w.robot.loc_head_position[:2]
        ball_2d = w.ball_abs_pos[:2]
        goal_dir = M.vector_angle( (15,0)-player_2d ) # Goal direction


        if p.behavior.is_ready("Get_Up") or getting_up[i]:
            getting_up[i] = not p.behavior.execute("Get_Up") # True on completion
        else:
            p.behavior.execute("Basic_Kick", goal_dir)

    script1.batch_commit_and_send()
    script1.batch_receive()
