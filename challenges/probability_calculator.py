import copy
import random
# Consider using the modules imported above.
class Hat:

    def __init__(self, **kwargs):
      self.contents = []
      if kwargs:
          for key, value in kwargs.items():
              self.contents.extend([key] * value)

    def draw(self, amount):
        draws = []
        for _ in range(amount):
            if self.contents:
                item = random.choice(self.contents)
                draws.append(item)
                self.contents.remove(item)
            else:
                return draws

        return draws


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    colors = list(expected_balls.keys())

    for _ in range(num_experiments):
        if hat.contents:
            hat_copy = copy.deepcopy(hat)
            draw_ = hat_copy.draw(num_balls_drawn)
            actual_balls_drawn = [draw_.count(color) for color in colors]

        if (actual_balls_drawn >= list(expected_balls.values())):
            m += 1

    return m / num_experiments
