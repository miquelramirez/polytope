import polytope # Caltech baseline
import numpy as np

def test_quickhull_algorithm():
    P_points = [np.array([-6., -6.]), np.array([-6.0, 6.0]),
                np.array([6.0, 6.0]), np.array([6.0, -6.0])]
    Q = polytope.qhull(np.array(P_points), [3, 1, 2])

    print(Q)
    print(Q.vertices)
    assert False

if __name__ == '__main__':
    test_quickhull_algorithm()