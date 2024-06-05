# 'l', 's', 'b', 'm'
import json
import math


class Map:
    def __init__(self):
        self.rows = 10  # 27
        self.cols = 10  # 48
        self.view_rows = 5
        self.view_cols = 5
        self.map_range = (self.rows + 1) * (self.cols + 1)
        self.world_map = {}
        self.actual_map = [[[] for _ in range(self.cols)] for _ in range(self.rows)]
        self.started_id = 0
        # print(self.actual_map)
        # self.actual_map = []
        self.percentage_land = .1

    def fill_water(self):
        # for y in range((self.rows * -1) // 2, self.rows // 2):
        #     for x in range((self.cols * -1) // 2, self.cols // 2):
        #         self.actual_map[y][x] = ['s', [y, x]]
        i = 0
        for y in range(self.rows // 2, (self.rows // 2) * -1 - 1, -1):
            for x in range((self.cols * -1) // 2, self.cols // 2 + 1):
                # print(y, x)
                self.actual_map[y][x] = ['s', [y, x], i]
                self.world_map[i] = 's', y, x
                i += 1
        # print(self.actual_map)

    def create_land(self):
        lower_y_id = math.ceil(self.rows // 2 * -1) + math.ceil(self.rows * self.percentage_land / 2)
        higher_y_id = math.ceil(self.rows // 2) - math.ceil(self.rows * self.percentage_land / 2)
        lower_x_id = math.ceil(self.cols // 2 * -1) + math.ceil(self.cols * self.percentage_land / 2)
        higher_x_id = math.ceil(self.cols // 2) - math.ceil((self.cols * self.percentage_land / 2))

        for y in range(higher_y_id, lower_y_id - 1, -1):
            for x in range(lower_x_id, higher_x_id + 1):
                id_wold_cell = self.actual_map[y][x][2]
                new_data_world_cell = list(self.world_map[id_wold_cell])
                new_data_world_cell[0] = 'l'
                self.world_map[id_wold_cell] = new_data_world_cell

    def print_map(self, map={}, case='only_letter'):
        match case:
            case 'only_letter':
                i = self.started_id
                # for y in range(self.rows // 2, (self.rows // 2) * -1 - 1, -1):
                #     for x in range((self.cols * -1) // 2, self.cols // 2 + 1):
                #         if self.actual_map[y][x][0] == 's':
                for y in range(self.rows):
                    for x in range(self.cols):
                        try:
                            if map[i][0] == 's':
                                print('~', end=' ')
                                # print(_)
                            else:
                                print('+', end=' ')
                            i += 1
                        except:
                            print('_', end=' ')
                    print()
            case 'full_info':
                print(self.actual_map)
                # pass
            case _:
                print('Неправильный ввод, требуется проверка ввода')
                # pass

    def get_json(self):
        # id = 0
        json_dict = {}
        # for y in range(self.rows // 2, (self.rows // 2) * -1 - 1, -1):
        #     for x in range((self.cols * -1) // 2, self.cols // 2 + 1):
        #         print(self.actual_map[y][x][1][0], x)
        #         json_dict[id] = self.actual_map[y][x][0], self.actual_map[y][x][1][0], self.actual_map[y][x][1][1]
        #         print(json_dict[id])
        #         id += 1
        for _ in range(len(self.world_map)):
            json_dict[_] = self.world_map[_][0], self.world_map[_][1], self.world_map[_][2]
        # print(json_dict)

        with open('map.json', 'w', encoding="utf-8") as file:
            json.dump(json_dict, file, indent=2, ensure_ascii=False)
            # print(json_dict[id])
        # print(json_dict)

        # id += 1
        # self.world_map[id] = {'s', (y, x)}

    def get_new_map(self, map={}, direction='up', old_y=-3, old_x=-3):
        match direction:
            case 'up':
                old_y += 1
            case 'down':
                old_y -= 1
            case 'left':
                old_x += 1
            case 'right':
                old_x -= 1

        new_map = {}
        for i in range(self.map_range):
            if data[str(i)][1] == old_y and data[str(i)][2] == old_x:
                self.started_id = i
                break
        for i in range(self.started_id, self.map_range):
            new_map[i] = map[str(i)]
            # print(data[str(i)])
        # print(new_map)
        return new_map
        # print(len(data))
        # print(self.map_range)
        # Второй вариант
        # for y in range(old_y, old_y + self.rows):
        #     for x in range(old_x, old_x + self.cols):
        #         pass # брать из текущей actual_map

    def get_new_coords(self):
        pass


# create_full_water()
# create_land()
# print_map('only_letter')

map = Map()
map.fill_water()
map.create_land()
print(map.world_map)
# map.get_json()

with open('map.json', 'r', encoding="utf-8") as file:
    data = json.load(file)
    # print(data)
    # map.get_new_map(data)
    # print(map.print_map(map.get_new_map(data, 'down', 4, -4)))

# print(map.print_map(map.world_map))
# print(map.actual_map)

# print(round(12*0.1/2))
# print(i for i in range(2))
