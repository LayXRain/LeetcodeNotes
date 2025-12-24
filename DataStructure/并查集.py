#并查集用于多个
#查找 合并 连通性判断
class UnionFind:
    def __init__(self, n: int):
        """
        初始化并查集
        :param n: 元素的个数（元素编号从0到n-1）
        """
        # 父节点列表：parent[i]表示i的父节点
        self.parent = list(range(n))
        # 秩列表（用集合大小）：size[i]表示以i为根的集合的元素个数
        self.size = [1] * n

    def find(self, x: int) -> int:
        """
        查找元素x的根节点，同时进行路径压缩（迭代版，路径减半）
        :param x: 要查找的元素
        :return: x的根节点
        """
        # 当x的父节点不是自身时，说明不是根节点
        while self.parent[x] != x:
            # 路径压缩：让x的父节点直接指向祖父节点（路径减半）
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def find_recursive(self, x: int) -> int:
        """
        查找元素x的根节点，递归版（完全路径压缩）
        注意：Python默认递归深度有限（约1000），元素过多时可能栈溢出，建议用迭代版
        """
        if self.parent[x] != x:
            # 完全路径压缩：让x的父节点直接指向根节点
            self.parent[x] = self.find_recursive(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        """
        合并元素x和y所在的集合（按秩合并）
        :param x: 元素x
        :param y: 元素y
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            # 已经在同一个集合中，无需合并
            return

        # 按秩合并：将大小较小的集合合并到大小较大的集合下
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x  # 保证root_x的集合更大

        # 将root_y的父节点设置为root_x
        self.parent[root_y] = root_x
        # 更新root_x集合的大小
        self.size[root_x] += self.size[root_y]

    def is_connected(self, x: int, y: int) -> bool:
        """
        判断元素x和y是否连通（是否在同一个集合中）
        :param x: 元素x
        :param y: 元素y
        :return: 连通返回True，否则返回False
        """
        return self.find(x) == self.find(y)

    def get_set_size(self, x: int) -> int:
        """
        获取元素x所在集合的大小
        :param x: 元素x
        :return: 集合大小
        """
        return self.size[self.find(x)]

    def get_set_count(self) -> int:
        """
        获取当前集合的总个数
        :return: 集合个数
        """
        count = 0
        for i in range(len(self.parent)):
            # 根节点的父节点是自身，统计根节点个数即为集合个数
            if self.parent[i] == i:
                count += 1
        return count


# 测试代码
if __name__ == "__main__":
    # 初始化并查集，元素个数为5（编号0-4）
    uf = UnionFind(5)

    # 合并操作
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)

    # 连通性判断
    print(f"0和2是否连通：{uf.is_connected(0, 2)}")  # 输出：True
    print(f"0和3是否连通：{uf.is_connected(0, 3)}")  # 输出：False
    # 合并3和0
    uf.union(3, 0)
    print(f"0和3是否连通：{uf.is_connected(0, 3)}")  # 输出：True
    # 输出集合个数和集合大小
    print(f"当前集合的个数：{uf.get_set_count()}")  # 输出：1
    print(f"0所在集合的大小：{uf.get_set_size(0)}")  # 输出：5