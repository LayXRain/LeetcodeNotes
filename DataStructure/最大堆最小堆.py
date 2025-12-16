class MinHeap:
    def __init__(self):
        self.heap = []  # 用数组存储堆元素
    # 1. 插入元素（push）：上浮调整
    def push(self, val):
        # 步骤1：把新元素放到数组末尾（完全二叉树的最后一个位置）
        self.heap.append(val)
        # 步骤2：上浮调整（让新元素找到自己的正确位置，恢复堆序性）
        self._sift_up(len(self.heap) - 1)
    # 辅助函数：上浮调整（index：需要上浮的元素索引）
    def _sift_up(self, index):
        while index > 0:  # 只要不是根节点（index=0），就可能需要上浮
            parent_index = (index - 1) // 2  # 计算父节点索引
            # 最小堆：如果当前元素 < 父节点，交换两者（破坏堆序性，需要上浮）
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index  # 继续向上检查父节点
            else:
                break  # 当前元素 ≥ 父节点，堆序性恢复，停止上浮
    # 2. 删除堆顶（pop）：下沉调整
    def pop(self):
        if not self.heap:  # 堆为空，返回None
            return None
        # 步骤1：交换堆顶（索引0）和数组末尾元素（保证完全二叉树结构）
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        # 步骤2：删除数组末尾元素（原堆顶），并保存值用于返回
        top_val = self.heap.pop()
        # 步骤3：下沉调整（让新堆顶找到自己的正确位置，恢复堆序性）
        self._sift_down(0)
        return top_val
    # 辅助函数：下沉调整（index：需要下沉的元素索引）
    def _sift_down(self, index):
        n = len(self.heap)
        while True:
            left_child_idx = 2 * index + 1  # 左子节点索引
            right_child_idx = 2 * index + 2  # 右子节点索引
            smallest_idx = index  # 初始化“最小元素索引”为当前节点

            # 找到当前节点、左子节点、右子节点中的最小值索引
            # 1. 左子节点存在，且左子节点 < 当前最小元素
            if left_child_idx < n and self.heap[left_child_idx] < self.heap[smallest_idx]:
                smallest_idx = left_child_idx
            # 2. 右子节点存在，且右子节点 < 当前最小元素
            if right_child_idx < n and self.heap[right_child_idx] < self.heap[smallest_idx]:
                smallest_idx = right_child_idx

            # 如果最小元素不是当前节点（说明需要下沉）
            if smallest_idx != index:
                self.heap[index], self.heap[smallest_idx] = self.heap[smallest_idx], self.heap[index]
                index = smallest_idx  # 继续向下检查子节点
            else:
                break  # 最小元素是当前节点，堆序性恢复，停止下沉
    # 3. 查看堆顶元素（不删除）
    def peek(self):
        return self.heap[0] if self.heap else None
    # 4. 查看堆是否为空
    def is_empty(self):
        return len(self.heap) == 0

class MaxHeap:
    def __init__(self):
        self.heap = []
    # 1. 插入元素（push）：上浮调整
    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)
    # 辅助函数：上浮调整（当前元素 > 父节点时上浮）
    def _sift_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:  # 最大堆：当前元素>父节点则交换
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break
    # 2. 删除堆顶（pop）：下沉调整
    def pop(self):
        if not self.heap:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        top_val = self.heap.pop()
        self._sift_down(0)
        return top_val
    # 辅助函数：下沉调整（找到当前节点、左右子节点中的最大值，交换后下沉）
    def _sift_down(self, index):
        n = len(self.heap)
        while True:
            left_child_idx = 2 * index + 1
            right_child_idx = 2 * index + 2
            largest_idx = index  # 初始化“最大元素索引”为当前节点

            # 找到三者中的最大值索引
            if left_child_idx < n and self.heap[left_child_idx] > self.heap[largest_idx]:
                largest_idx = left_child_idx
            if right_child_idx < n and self.heap[right_child_idx] > self.heap[largest_idx]:
                largest_idx = right_child_idx

            if largest_idx != index:
                self.heap[index], self.heap[largest_idx] = self.heap[largest_idx], self.heap[index]
                index = largest_idx
            else:
                break
    # 3. 查看堆顶
    def peek(self):
        return self.heap[0] if self.heap else None
    # 4. 查看是否为空
    def is_empty(self):
        return len(self.heap) == 0