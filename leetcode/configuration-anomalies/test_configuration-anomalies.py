from collections import deque


def missing_digits(config: str, x: int, y: int) -> str:
    if len(config) == 1:
        return config

    if y < x:
        x, y = y, x

    queue = deque()
    queue.append((int(config[0]), config[0]))

    nxt_idx = 1
    computed = set([int(config[0])])

    while queue and nxt_idx < len(config):
        nxt = int(config[nxt_idx])

        curr, fin = queue.popleft()
        for val in [x, y]:
            comp = (curr + val) % 10
            if comp == nxt:
                nxt_idx += 1
                queue.clear()
                computed.clear()
                queue.append((comp, fin + str(comp)))
                break
            elif comp not in computed:
                queue.append((comp, fin + str(comp)))
                computed.add(comp)

    if nxt_idx < len(config):
        return "-1"

    else:
        _, final = queue.popleft()
        return final


def test_case_1():
    config = "27"
    x = 2
    y = 3
    assert missing_digits(config, x, y) == "247"


def test_case_2():
    config = "521"
    x = 5
    y = 5
    assert missing_digits(config, x, y) == "-1"


def test_case_3():
    config = "324"
    x = 2
    y = 3

    assert missing_digits(config, x, y) == "36924"


def test_case_0_9():
    config = "0123"
    x = 0
    y = 9

    assert missing_digits(config, x, y) == "0987654321098765432109876543"
