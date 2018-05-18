# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class TheSquareCityDiv2:
    def __init__(self):
        self.n = 0

    def find(self, r, t):
        self.n = int(math.sqrt(len(t)))
        a, b = None, None
        def BFS(i, j, depth):
            maxx, maxy, maxt = 21, 21, 0
            q = []
            q.append((i,j, depth))
            mask = 0
            while q:
                curi, curj, curdepth = q.pop(0)
                if curdepth <= -1: continue
                curt = t[self.get(curi, curj)]
                mask |= (1 << self.get(i, j))
                if curt > maxt:
                    maxt = curt
                    maxx, maxy = curi, curj
                for ii,jj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x, y = curi + ii, curj + jj
                    if x < 0 or y < 0 or x >= self.n or y >= self.n: continue
                    if (mask | (1 << self.get(x, y))) == 1: continue
                    q.append((x, y, curdepth-1))
            return (maxx, maxy)

        cnt = [1]*len(t)
        ord_lst = []
        for i in range(self.n):
            for j in range(self.n):
                ord_lst.append((t[self.get(i,j)], i, j))
        ord_lst.sort()
        for (x, i, j) in ord_lst:
            maxx,maxy = BFS(i, j, r)
            if maxx == i and maxy == j:  continue
            cnt[self.get(maxx,maxy)] += cnt[self.get(i,j)]
            cnt[self.get(i, j)] = 0
            # print(i,j,maxx,maxy,cnt)
        a = len([ele for ele in cnt if ele != 0])
        b = max(cnt)
        print(a,b,cnt)
        return (a,b)

    def get(self, x, y):
        return x*self.n+y
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

def do_test(r, t, __expected):
    startTime = time.time()
    instance = TheSquareCityDiv2()
    exception = None
    try:
        __result = instance.find(r, t);
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
    sys.stdout.write("TheSquareCityDiv2 (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("TheSquareCityDiv2.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            r = int(f.readline().rstrip())
            t = []
            for i in range(0, int(f.readline())):
                t.append(int(f.readline().rstrip()))
            t = tuple(t)
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(int(f.readline().rstrip()))
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(r, t, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1526606812
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
