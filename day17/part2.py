"""
    Math Again:
    I should mention my input values are as follows:
    target area: x=217..240, y=-126..-69
    * At the description below, I'll use Vy0 and Vx0 as the initial velocities in X and Y direction.
    As you might know, we can separate Y from X.
    The algorithm for all Vy0s and Vx0s finds all steps in which the trajectory can be in the
    target area.
    Then we'll see for a given Vx0, which Vy0s have steps in common with it.
    For example, there might be a Vx0 which is in target area at steps 1,2,3. For all Vy0s, we check
    if their steps have any number in common with the given Vx0, if yes then the pair [Vx0, Vy0] is valid.
    Y:
        We know the upper bound for Vy0 is 125 (from part1). But what Vy0s might result in overshooting:
        If you think about it, the best candidate for overshooting is the fastest speed which causes the
        trajectory to get to position y = y_max + 1 -> Vy0 = - y_max - 2
        there are other speeds that might cause overshooting, but the lower bound is the height of the
        target area (y_max - y_min)
        so we will consider all speeds in that region.
        * For simplicity, we will cover all velocities from y_min to -y_max - 1
    X:
        It's the same idea for x as well.
"""

import math

Y_MAX = -69
Y_MIN = -126
X_MAX = 240
X_MIN = 217
y_steps = []
x_steps = []
for Vy0 in range(Y_MIN, -Y_MIN):
    v_temp = Vy0
    step = 0
    y = 0
    tmp = []
    while True:
        if Y_MAX >= y >= Y_MIN and len(tmp) == 0:
            tmp.append(step)
        elif y < Y_MIN:
            if len(tmp) > 0:
                tmp.append(step - 1)
            break
        y += v_temp
        v_temp -= 1
        step += 1
    if len(tmp) != 0:
        y_steps.append(tmp + [Vy0])

for Vx0 in range(X_MAX + 1):
    v_temp = Vx0
    step = 0
    x = 0
    tmp = []
    while True:
        if X_MAX >= x >= X_MIN and len(tmp) == 0:
            tmp.append(step)
        elif x > X_MAX:
            if len(tmp) > 0:
                tmp.append(step - 1)
            break
        if v_temp == 0:
            if len(tmp) > 0:
                tmp.append(math.inf)
            break
        x += v_temp
        v_temp -= 1
        step += 1
    if len(tmp) != 0:
        x_steps.append(tmp + [Vx0])
res = 0
for y_step in y_steps:
    for x_step in x_steps:
        if y_step[1] >= x_step[0] >= y_step[0] or \
                y_step[1] >= x_step[1] >= y_step[0] or \
                x_step[1] >= y_step[1] >= x_step[0] or \
                x_step[1] >= y_step[1] >= x_step[0]:
            res += 1

print(res)
