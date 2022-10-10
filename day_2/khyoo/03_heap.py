import sys


class Heap:
    def __init__(self):
        self.heap_array = [None]

    def __repr__(self):
        return str(self.heap_array)

    def size(self):
        return len(self.heap_array) - 1

    def add(self, value):
        self.heap_array.append(value)
        loc = self.size()
        parent_loc = loc // 2

        while parent_loc:
            parent_value = self.heap_array[parent_loc]
            if value > parent_value:
                self.heap_array[loc], self.heap_array[parent_loc] = parent_value, value
                loc = parent_loc
                parent_loc = loc // 2
            else:
                break

    def pop(self):
        if self.size():
            max_v, last_v = self.heap_array[1], self.heap_array[self.size()]
            self.heap_array[1], self.heap_array[self.size()] = last_v, max_v
            self.heap_array.pop()

            if self.size():
                current_node_idx = 1
                left_node_idx = current_node_idx * 2
                while self.size() >= left_node_idx:
                    current_node_val = self.heap_array[current_node_idx]
                    target_idx = left_node_idx

                    right_node_idx = current_node_idx * 2 + 1
                    if self.size() >= right_node_idx:
                        left_node_value = self.heap_array[left_node_idx]
                        right_node_value = self.heap_array[right_node_idx]
                        if left_node_value < right_node_value:
                            target_idx = right_node_idx

                    target_value = self.heap_array[target_idx]

                    if target_value > current_node_val:
                        (
                            self.heap_array[current_node_idx],
                            self.heap_array[target_idx],
                        ) = (target_value, current_node_val)
                        current_node_idx = target_idx
                        left_node_idx = current_node_idx * 2
                    else:
                        break

            return max_v
        else:
            return 0


h = Heap()

i = lambda: int(sys.stdin.readline().strip())
_ = i()

while True:
    try:
        num = i()
        if num:
            h.add(num)
        else:
            print(h.pop())

    except Exception as e:

        break
