# 散列表构建图
graph = {}
graph['anuj'] = []
graph['bob'] = ['anuj', 'peggy']
graph['peggy'] = []
graph['you'] = ['bob', 'alice', 'claire']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['thom'] = []
graph['jonny'] = []


def is_mangoSeller(person):
    return person[-1] == 'm'


from collections import deque


# 广度优先遍历
def searchName():
    searchQueue = deque()
    searchQueue += graph
    searched = []
    while searchQueue:
        person = searchQueue.popleft()
        if not person in searched:
            if is_mangoSeller(person):
                print(person + ' is a mango seller.')
                return True
            else:
                searchQueue += graph[person]
                searched.append(person)
    return False


if __name__ == '__main__':
    searchName()
