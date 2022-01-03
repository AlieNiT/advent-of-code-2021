"""
This problem doesn't need any kind of programming. It's just math.
The key observation is this: If we're only concerned about y < 0 (target area is completely under y = 0)
then there are 3 important facts about the solution:
    1. The Trajectory will be at position y = 0 at some point in future
    2. When the Trajectory passes y = 0, its y velocity is the initial y velocity + 1
    3. Considering the first fact, maximum velocity for the trajectory happens if the
       next step takes us from 0 to y_min.
"""
y_min = int(input())  # pass y_min
v0 = -y_min - 1
H = (v0 * (v0 + 1)) // 2
print(H)
