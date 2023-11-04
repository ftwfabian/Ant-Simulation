from Math import angle_between

class Container:
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def set_agents(self, list_of_ants, list_of_food, list_of_homes):
        self.list_of_ants = list_of_ants
        self.list_of_food = list_of_food
        self.list_of_homes = list_of_homes

    def run_all(self):
        self.ant_collision()
        self.collect_food()
        self.food_in_sight()

    def draw_all(self):
        for ant in self.list_of_ants:
            ant.move()
            ant.draw()
        for food in self.list_of_food:
            food.draw()
        for home in self.list_of_homes:
            home.draw()
        
    def ant_collision(self):
        pass

    def collect_food(self):
        for ant in self.list_of_ants:
            for food in self.list_of_food:
                if self.food_is_very_near(ant.position, food.position, food.radius):
                    food.decrement_food()
                    #and then update ant to head back to home

    def food_is_very_near(self, position1, position2, food_radius):
        offset = food_radius
        p1x1_offset = abs(position1[0]-offset)
        p1x2_offset = abs(position1[0]+offset)
        p1y1_offset = abs(position1[1]-offset)
        p1y2_offset = abs(position1[1]+offset)

        if (position2[0] > p1x1_offset and position2[0] < p1x2_offset
        and position2[1] > p1y1_offset and position2[1] < p1y2_offset):
            return True
        return False
    
    def food_in_sight(self):
        for ant in self.list_of_ants:
            for food in self.list_of_food:
                vector_to_food = food.position - ant.position
                if vector_to_food.length() > ant.sight_distance:
                    return
                angle = angle_between(ant.direction, vector_to_food)
                if angle != None:
                    if angle <= ant.sight_angle:
                        ant.direction = vector_to_food