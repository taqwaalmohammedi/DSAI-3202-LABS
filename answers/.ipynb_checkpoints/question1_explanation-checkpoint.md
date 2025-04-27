# Question 1: How the Automated Maze Explorer Works

## Original Algorithm: Right-Hand Rule

At first, I used the **right-hand rule** algorithm. This is a basic method where the explorer always turns right and tries to go forward. If it can’t move, it keeps turning left until it finds a path.

### How it works:
1. Turn right and try to move.
2. If that fails, turn left and try again.
3. If still blocked, turn left again (to face left).
4. If none work, turn around and move backward.

This method works in most mazes, but it's not guaranteed to be efficient.

---

## Loop Detection

To prevent getting stuck in a loop, I tracked the last 3 positions using a `deque`.  
If the explorer visited the same place three times in a row, it meant it was going in circles.

### Code idea:
- I used `self.move_history = deque(maxlen=3)`
- Then `is_stuck()` checks if all 3 moves are the same.
