# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class Resistance:
    def spyProbability(self, P, S, missions):
        tot = 0
        counts = [0 for __ in xrange(P)]
        for spies in range(1 << P):
            # this set of spies is valid if the number of spies is exactly S and for each mission, it is a success, or there is a spy on it.
            print(bin(spies))
            if str(bin(spies)).count("1") == S and all(m[0] == 'S' or int(m[1:], 2) & spies for m in missions):
                tot += 1
                for i in range(P):
                    counts[i] += (spies >> i) & 1
        print(counts)
        print(tot)
        if tot == 0: return []
        return map(lambda x: 1.0 * x / tot, counts)[::-1]

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

def do_test(P, S, missions, __expected):
    startTime = time.time()
    instance = Resistance()
    exception = None
    try:
        __result = instance.spyProbability(P, S, missions);
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
    sys.stdout.write("Resistance (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("Resistance.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            P = int(f.readline().rstrip())
            S = int(f.readline().rstrip())
            missions = []
            for i in range(0, int(f.readline())):
                missions.append(f.readline().rstrip())
            missions = tuple(missions)
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(float(f.readline().rstrip()))
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(P, S, missions, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1524956938
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
