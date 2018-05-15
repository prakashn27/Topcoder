# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

from collections import defaultdict
class MakingPotions:
    def getCost(self, marketGoods, cost, recipes):
        marketGoods = list(marketGoods)
        cost = list(cost)
        receipe_lst = list(recipes)
        # for r in list(recipes):
        #     spl = r.split("=")
        #     if len(spl) != 2:
        #         print spl
        #         continue
        #     k,v = spl[0], spl[1]
        #     receipe_map[k].append(v)

        cost_map = {}
        for i, v in enumerate(marketGoods):
            cost_map[v] = cost[i]
        current_tree = set()  # 1 currently visiting, 2 finished visiting
        # if "LOVE" not in receipe_map:
        #     if "LOVE" not in cost_map:
        #         return -1
        #     return cost_map["LOVE"]
        # print cost_map
        # print receipe_map

        run = 40
        while run:
            run -= 1
            for rec in receipe_lst:
                p, r = rec.split("=")[0], rec.split("=")[1]
                spl = r.split("+")
                if len(spl) == 0: continue
                n_val = 0
                for item in spl:
                    mul = int(item[0])
                    item = item[1:]
                    if item not in cost_map:
                        n_val = -1
                        break
                    n_val += mul*cost_map[item]
                    if n_val > 1000000000:
                        n_val = 1000000001
                        break
                if n_val != -1:
                    cur_val = 1000000002
                    if p in cost_map: cur_val = cost_map[p]
                    cost_map[p] = min(cur_val, n_val)
        if "LOVE" in cost_map: return cost_map["LOVE"]
        return -1

        # def getmin(potion):
        #     if potion not in cost_map and potion not in receipe_map:
        #         return -1  # not in market as well as we dont have receipe
        #     if potion in current_tree:
        #         return "terminate"  # cycle
        #     current_tree.add(potion)
        #     cur_res = 0
        #     ret_res = sys.maxint
        #     for r in receipe_map[potion]:
        #         spl = r.split("+")
        #         if len(spl) == 0: continue
        #         for item in spl:
        #             if len(item) < 2: continue
        #             mul = int(item[0])
        #             item = item[1:]
        #             cur_min = getmin(item)
        #             if cur_min == "terminate": return -1
        #             if cur_min == -1: continue
        #             cur_res += mul*cur_min
        #         ret_res = min(ret_res, cur_res)
        #     current_tree.remove(potion)
        #     return ret_res if ret_res != sys.maxint else cost_map[potion] if potion in cost_map else -1
        #
        # return getmin("LOVE")

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

def do_test(marketGoods, cost, recipes, __expected):
    startTime = time.time()
    instance = MakingPotions()
    exception = None
    try:
        __result = instance.getCost(marketGoods, cost, recipes);
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
    sys.stdout.write("MakingPotions (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("MakingPotions.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            marketGoods = []
            for i in range(0, int(f.readline())):
                marketGoods.append(f.readline().rstrip())
            marketGoods = tuple(marketGoods)
            cost = []
            for i in range(0, int(f.readline())):
                cost.append(int(f.readline().rstrip()))
            cost = tuple(cost)
            recipes = []
            for i in range(0, int(f.readline())):
                recipes.append(f.readline().rstrip())
            recipes = tuple(recipes)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(marketGoods, cost, recipes, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1526421974
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
