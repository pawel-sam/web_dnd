# 'l', 's', 'b', 'm'
import json
import math


class Map():
    def __init__(self):
        self.rows = 27
        self.cols = 48
        self.map_range = self.rows * self.cols
        self.world_map = {}
        self.actual_map = [[[] for _ in range(self.cols)] for _ in range(self.rows)]
        # print(self.actual_map)
        # self.actual_map = []
        self.percentage_land = .1

    def fill_water(self):
        # for y in range((self.rows * -1) // 2, self.rows // 2):
        #     for x in range((self.cols * -1) // 2, self.cols // 2):
        #         self.actual_map[y][x] = ['s', [y, x]]
        for y in range(self.rows // 2, (self.rows // 2) * -1 - 1, -1):
            for x in range((self.cols * -1) // 2, self.cols // 2 + 1):
                # print(y, x)
                self.actual_map[y][x] = ['s', [y, x]]
        # print(self.actual_map)

    def create_land(self):
        # lower_y_id, higher_y_id = (int(self.rows * self.percentage_land)) - (self.rows // 2), self.rows - (int(self.rows * self.percentage_land)) - (self.rows // 2)
        # lower_x_id, higher_x_id = (int(self.cols * self.percentage_land)) - (self.cols // 2), self.cols - (int(self.cols * self.percentage_land)) - (self.cols // 2)

        lower_y_id = math.ceil(self.rows / 2 * -1) + math.ceil(self.rows * self.percentage_land / 2)
        higher_y_id = math.ceil(self.rows / 2) - math.ceil(self.rows * self.percentage_land / 2)
        lower_x_id = math.ceil(self.cols / 2 * -1) + math.ceil(self.cols * self.percentage_land / 2)
        higher_x_id = math.ceil(self.cols / 2) - math.ceil((self.cols * self.percentage_land / 2))
        # for y in range(higher_y_id - lower_y_id + 1):
        #     for x in range(higher_x_id - lower_y_id + 1):
        # print(higher_y_id, lower_y_id)
        # print(lower_x_id, higher_x_id)
        for y in range(higher_y_id, lower_y_id - 1, -1):
            for x in range(lower_x_id, higher_x_id + 1):
                # self.actual_map[y + lower_y_id][x + lower_x_id][0] = 'l'
                self.actual_map[y][x][0] = 'l'
                # print(self.actual_map[y][x])
                # print(f"create_land: created with id = {y + 10, x + 10}")
        return self.actual_map

    def print_map(self, case):
        match case:
            case 'only_letter':
                for y in range(self.rows // 2, (self.rows // 2) * -1 - 1, -1):
                    for x in range((self.cols * -1) // 2, self.cols // 2 + 1):
                        if self.actual_map[y][x][0] == 's':
                            print('~', end=' ')
                            # print(_)
                        else:
                            print('+', end=' ')
                    print()
            case 'full_info':
                print(self.actual_map)
                # pass
            case _:
                print('Неправильный ввод, требуется проверка ввода')
                # pass

    def get_json(self):
        id = 0
        json_dict = {}
        # [['s',[y, x]],[],[],[]]
        for y in range(self.rows // 2, (self.rows // 2) * -1 - 1, -1):
            for x in range((self.cols * -1) // 2, self.cols // 2 + 1):
                json_dict[id] = self.actual_map[y][x][0], self.actual_map[y][x][1][0], self.actual_map[y][x][1][1]
                id += 1
        with open('map.json', 'w', encoding="utf-8") as file:
            json.dump(json_dict, file, indent=0, ensure_ascii=False)
            # print(json_dict[id])
        # print(json_dict)

        # id += 1
        # self.world_map[id] = {'s', (y, x)}

# create_full_water()
# create_land()
# print_map('only_letter')

# map = Map()
# map.fill_water()
# map.create_land()
# print(map.print_map('only_letter'))
# print(map.actual_map)
# print(map.get_json())

# print(round(12*0.1/2))
