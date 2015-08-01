# Ramdom number generation static functions

import random

class Random:

    def get_gaussian_box_muller_values(n):
        
        x = 0
        y = 0
        euclid_sq = 0
        values = []

        for i in n:
            while True:
                x = 2 * random.random()
                y = 2 * random.random()
                euclid_sq = math.pow(x,2) + math.pow(y,2)
                if euclid_sq < 1:
                    values.append(euclid_sq)
                    break
                
        return values
        