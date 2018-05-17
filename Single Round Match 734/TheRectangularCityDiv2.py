# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

# Ans
# https://community.topcoder.com/stat?c=problem_solution&rm=331269&rd=17158&pm=14902&cr=40484882

class TheRectangularCityDiv2:
    def find(self, city):
        total_houses = 0
        if not city or not city[0]:
            return 0
        n, m = len(city), len(city[0])

        res = [0]
        for r in city:
            total_houses += r.count(".")

        def dfs(x,y, visited, houses_visited, res):
            if x >= n or y >= m or x < 0 or y < 0 or visited[x][y] or city[x][y] == "#":
                return
            houses_visited += 1
            visited[x][y] = True
            print(x,y)
            if houses_visited == total_houses:
                if x == 0 or x == n-1 or y == 0 or y == m-1:
                    print(x, y, houses_visited, visited)
                    res[0] += 1
            for (xx, yy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(x+xx, y+yy, visited, houses_visited, res)
            visited[x][y] = False

        for i in range(n):
            for j in range(m):
                visited = [[False]*m for _ in range(n)]
                print("###")
                print(i,j)
                dfs(i,j,visited,0, res)
        return res[0]

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(city, __expected):
    startTime = time.time()
    instance = TheRectangularCityDiv2()
    exception = None
    try:
        __result = instance.find(city);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("TheRectangularCityDiv2 (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("TheRectangularCityDiv2.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            city = []
            for i in range(0, int(f.readline())):
                city.append(f.readline().rstrip())
            city = tuple(city)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(city, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1526520511
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
