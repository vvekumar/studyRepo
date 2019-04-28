"""
purpose: euler.py used to run algorithms for problem IDs in the Euler set
usage :
euler.py --id <problem_id> --show-ids
"""
import argparse
from eid_1 import eid_1 # need to replace this with a catch-all all-module-within-pkg-import
from eid_2 import eid_2 # need to replace this with a catch-all all-module-within-pkg-import
from eid_081 import eid_081 # need to replace this with a catch-all all-module-within-pkg-import


class Euler:
    def __init__(self, id=None, show_id=None):
        self.id, self.show_id = id, show_id


    def euler(self,):
        """runner for input euler problem id
        :return None
        """

        if self.show_id is not None:
            # shows all available options and exit
            # NOT IMPLEMENTED
            print "This is currently not implemented"
            raise NotImplementedError
            # methods = dir('euler')
            # print ",".join(methods)


        if self.id is not None:
            # run publem id 'id'
            rslt = eval("eid_%s"%self.id)()
            print "Output: " + str(rslt)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run an Euler problem Id")
    parser.add_argument('--id', dest='id', default=None, help='(int) Integer problem ID')
    parser.add_argument('--show-id', dest='show_id', default=None, help='Shows all (solved) available problem IDs ')

    args = parser.parse_args()
    E = Euler(args.id, args.show_id)
    E.euler()