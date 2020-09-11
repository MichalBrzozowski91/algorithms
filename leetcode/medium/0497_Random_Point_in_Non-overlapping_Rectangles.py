class Solution:
    from random import randrange, choices
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = [(rect[2] - rect[0] + 1)*(rect[3] - rect[1] + 1) for rect in rects]

    def pick(self) -> List[int]:
        '''This functions picks an arbitrary point from the area covered by given rectangles'''
        # Random choice of the rectangle
        rectangle_index = choices(population = range(len(self.rects)), weights = self.areas)
        rect = self.rects[rectangle_index[0]]
        x_coordinate = randrange(rect[0],rect[2]+1)
        y_coordinate = randrange(rect[1],rect[3]+1)
        return [x_coordinate,y_coordinate]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
