import gym
class CdmEnv(gym.Env):
    def __init__(self):
        self.state = [['-' for _ in range(3)] for _ in range(3)]
        self.counter = 0  # 当前步数
        self.done = 0  # 对局是否结束
        self.add = [0, 0]  # 表示胜负情况，1代表获胜
        self.reward = 0

    def check(self):  # 检查当前棋盘是否有人可以获得胜利
        if self.counter < 5:
            return 0  # 步数小于五步，无人获胜
        for i in range(3):  # 判断横竖三行是否有连子，有则返回对应胜者
            if self.state[i][0] != '-' and self.state[i][1] == self.state[i][0] and self.state[i][1] == self.state[i][
                2]:
                if self.state[i][0] == 'o':  # o代表第一名选手的棋子
                    return 1
                else:
                    return 2
            if self.state[0][i] != '-' and self.state[1][i] == self.state[0][i] and self.state[1][i] == self.state[2][
                i]:
                if self.state[0][i] == 'o':  # o代表第一名选手的棋子
                    return 1
                else:
                    return 2
        # 判断两条对角线上是否有连子
        if self.state[0][0] != '-' and self.state[1][1] == self.state[0][0] and self.state[1][1] == self.state[2][2]:
            if self.state[0][0] == 'o':  # o代表第一名选手的棋子
                return 1
            else:
                return 2
        if self.state[0][2] != '-' and self.state[1][1] == self.state[0][2] and self.state[1][1] == self.state[2][0]:
            if self.state[0][2] == 'o':  # o代表第一名选手的棋子
                return 1
            else:
                return 2
        # 所有其他情况均无胜者
        return 0

    def step(self, action):  # 执行动作，返回状态、奖励、是否重置及相关信息
        x, y = action[0], action[1]  # 这里用1-9的数字表示棋盘上点的坐标
        if self.done == 1:
            print("游戏结束")
            return [self.state, self.reward, self.done, self.add]
        elif self.state[x][y] != '-':
            print("非法步骤")
            return [self.state, self.reward, self.done, self.add]
        else:
            if self.counter % 2 == 0:  # 偶数步表示第一名选手
                self.state[x][y] = 'o'
            else:
                self.state[x][y] = 'x'
            self.counter += 1
            if self.counter == 9:  # 棋盘放满则游戏结束
                self.done = 1
            # self.render() # 可视化棋盘
        win = self.check()  # 判断当前的胜负情况
        if win:  # 如果可以分出胜负
            self.done = 1
            print("玩家 ", win, " 号获胜", sep='', end='\n')
            self.add[win - 1] = 1
            if win == 1:  # 这里1号玩家赢了给予奖励，2号赢了则给予惩罚（即环境希望1号获胜）
                self.reward = 1
            else:
                self.reward = -1
        return [self.state, self.reward, self.done, self.add]

    def reset(self):  # 重置环境
        self.state = [['-' for _ in range(3)] for _ in range(3)]
        self.counter = 0
        self.done = 0
        self.add = [0, 0]
        self.reward = 0
        return self.state

    def render(self):
        for i in range(3):
            for j in range(3):
                print(self.state[i][j], end=" ")
            print("")  # 换行
        print("")

    def getPosition(self, x, y):
        item = self.state[x][y]
        return item

    def close(self):
        print("env closed")
