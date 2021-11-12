import numpy as np

adj_matrix = np.array([
    [-1, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0, 0],  # Na
    [-1, -1, 0, -2, -2, 0, 0, -2, -2, -1, -1, -1, 0],  # Cl2
    [0, 0, -2, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],  # O2
    [0, 0, -2, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0],  # H2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],  # Cu
    [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],  # S
    [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # K
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],  # Fe
    [-2, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0],  # NaCl
    [0, 0, 0, -1, -1, 0, 0, 0, 0, -2, 0, 0, 0],  # HCl
    [0, 0, -1, -2, -2, 0, -2, 0, -1, -1, 0, 0, 0],  # H2O
    [0, 0, 0, 0, 0, 0, -1, 0, -2, 0, 0, 0, 0],  # NaOH
    [0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0],  # HClO
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0],  # CuCl2
    [0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -2],  # H2SO4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0],  # FeCl3
    [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # MnO2
    [0, -2, 0, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0],  # KCl
    [0, 0, 0, -2, -2, 0, 0, 0, 0, 0, 0, 0, 0],  # MnCl2
    [0, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0],  # Na2SO4
    [0, 0, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0, -1],  # SO3
    [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],  # KMnO4
])

# Column
list_column = [
    "Na + Cl2 -> NaCl",
    "K + Cl2 -> KCl",
    "2H2O -> 2H2 + O2",
    "MnO2 + 4HCL -> MnCl2 + Cl2 + 2H2O",
    "16HCL + 2KMnO4 -> 2KCl + 2MnCl2 + 8H2O + 5Cl2",
    "2S + 3O2 -> 2SO3",
    "2NaOH + H2SO4 -> Na2SO4 + 2H2O",
    "2NaCL -> 2Na + Cl2",
    "2NaCl + 2 H2O -> Cl2 + H2 + 2NaOH",
    "Cl2 + H2O -> HCl + HClO",
    "Cu + Cl2 -> CuCl2",
    "2Fe + 3Cl2 -> 2FeCl3",
    "SO3 + H2O -> H2SO4"
]


class Solve:
    def __init__(self, adj_matrix, default, find):
        self.adj_matrix = adj_matrix
        # ma trận kề
        self.adj_matrix[default, :] = np.abs(adj_matrix[default, :])
        # Đổi dấu dòng các chất đã có
        self.result = []
        # Lưu các phương trình đã dùng để giải

        self.find = find
        # Các chất cần tìm phương trình

    def isFound(self):
        return self.adj_matrix[self.find, :] == np.abs(self.adj_matrix[self.find, :])
        # check các dòng cần tìm đã được đổi dấu

    def isEnd(self):
        return self.iter > self.adj_matrix.shape[1]
        # kết thúc khi không thể tìm được lời giải

    def solving(self):
        self.iter = 0
        while not self.isFound or not self.isEnd():
            self.iter += 1

            for i in range(self.adj_matrix.shape[1]):
                # lặp qua chỉ số cột

                if i not in self.result and np.all(self.adj_matrix[:, i] != -1):
                    # kiểm tra phương trình đã có trong kết quả chưa & cột có giá trị khác -1
                    for j in range(self.adj_matrix.shape[0]):
                        # Lặp qua các chỉ số dòng của cột này
                        if self.adj_matrix[j, i] < 0:

                            self.adj_matrix[j, :] = np.abs(
                                self.adj_matrix[j, :])
                            # giá trị tại dòng j cột i < 0 thi đổi dấu các dòng j
                    self.result.append(i)
                    # đánh dấu đã chọn phương trình

    def printResult(self):
        for i in self.result:
            print(list_column[i])
            # lặp, kiểm tra và in ra phương trình sử dụng


default = np.array([5, 8, 10])
# mảng đầu vào (S2, H2O, NaCl)

find = np.array([0, 9, 14, 19])
# mảng cần tìm (Na2SO4, H2SO4, HCL, Na)

engine = Solve(adj_matrix, default, find)
engine.solving()
engine.printResult()
