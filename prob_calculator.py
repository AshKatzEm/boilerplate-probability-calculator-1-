import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        """This class takes a variable number of key word arguments that specify the number of balls of each color that are in the hat and stores it as a dictionary. e.g. hat = Hat(black=6, red=4, green=3)
      """
        self.dict = kwargs
        self._get_contents()
    
    # Get key from dict into contents
    def _get_contents(self):
        """The dictionary of hat contents is converted into a 'contents' instance variable. This is a list of strings containing one item for each ball in the hat. Each item in the list is a color name representing a single ball of that color. 
      """
        self.contents = []
        for k, v in self.dict.items():
            for i in range(0, v):
                self.contents.append(k)
    
    # draw balls from hat
    def draw(self, num):
      """This accepts an argument indicating the number of balls to draw from the hat. This method removes balls without replacement at random from 'contents' and returns the removed balls as a list of strings. When the number of balls to draw exceeds the available quantity, all the balls in the hat are returned.
      """
      self._get_contents()
      # if the number of balls to draw exceeds the available quantity, return all the balls in the hat
      if num > len(self.contents):
          return self.contents
      
      draw = []

      while num > 0:
          rand_index = random.randrange(0, len(self.contents))
          rand_content = self.contents.pop(rand_index)
          draw.append(rand_content)
          num -= 1
      
      return draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """This function takes a hat object containing a number of balls, an expected_balls dictionary indicating the exact group of balls that we want to draw from the hat for the experiment, a num_balls_drawn variable indicating the number of balls to draw from the hat in each experiment, and a num_experiments variable indicating the number of experiments to perform. It returns a probability."""

#     A deep copy constructs a new compound object which doesn't reference the original. We need to deepcopy expected_balls so that each copy, for each experiment performed, is independant of the original

    expected_balls_copy = copy.deepcopy(expected_balls)
    success = 0

    for i in range(0, num_experiments):
      
      #draw balls from the hat
        drawn_balls = hat.draw(num_balls_drawn)
        test_success = True

        # For each drawn ball, if it was expected: subtract the ball from expected_balls_copy
        for i in drawn_balls:
            if i in expected_balls_copy and expected_balls_copy[i] > 0:
                expected_balls_copy[i] -= 1
        
        # If there are any balls left in expected balls, the experiment fails
        for key, val in expected_balls_copy.items():
            if val > 0:
                test_success = False

        # If the experiment was successful, record it
        if test_success:
            success += 1

        # set new independant copy of expected balls for next experiment
        expected_balls_copy = copy.deepcopy(expected_balls)

    return float(success) / num_experiments