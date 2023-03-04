import abc


class BaseSolver:
    def __init__(self, cube_dict):
        self.cube_dict = cube_dict
        self.d_color = ''.join(self.cube_dict[(0, -1, 0)])
        self.u_color = ''.join(self.cube_dict[(0, 1, 0)])

    @classmethod
    def _find_path(self):
        raise NotImplementedError(f"Find path not implemented in{self.__class__.__name__}")

    def _move_up(self, node):
        """
        Appends the node to the end of open_set and move it up the tree.
        """
        self.open_set.append(node)

        while True:
            # Node info, compare f_cost and h_cost at the same time
            node_index = self.open_set.index(node)
            node_value = node.f_cost + node.h_cost / 100

            # If index is 0, can't move up anymore
            if not node_index:
                return

            # The position above node n is int half of (n - 1)
            node_up_index = (node_index - 1) // 2
            node_up = self.open_set[node_up_index]
            node_up_value = node_up.f_cost + node_up.h_cost/100

            # Compare values
            if node_value < node_up_value:
                self._swap(node_index, node_up_index)
            else:
                return

    def _move_down(self):
        """
        Sorts the top node down the heap.
        """
        set_len = len(self.open_set)

        # Don't run if open_set is empty
        if not set_len:
            return

        fn = self.open_set[0]
        fn_val = fn.f_cost + fn.h_cost/100

        while True:
            fn_ind = self.open_set.index(fn)

            left_ind = 2 * fn_ind + 1
            right_ind = left_ind + 1

            # Check if left node exists, if not we are finished
            if set_len > left_ind:
                left = self.open_set[left_ind]
                left_val = left.f_cost + left.h_cost/100
            else:
                return

            # Check if right node exists
            if set_len > right_ind:
                right = self.open_set[right_ind]
                right_val = right.f_cost + right.h_cost/100
            else:
                right = None

            # Left value must be less and either there is no right node or
            # the left node is the lower choice
            if (left_val < fn_val) and \
                (right is None or left_val <= right_val):
                self._swap(fn_ind, left_ind)
            elif right is not None and right_val < fn_val:
                self._swap(fn_ind, right_ind)
            else:
                return

    def _swap(self, i, j):
        """
        Swaps elements at i and j in open_set
        """
        self.open_set[i], self.open_set[j] = self.open_set[j], self.open_set[i]