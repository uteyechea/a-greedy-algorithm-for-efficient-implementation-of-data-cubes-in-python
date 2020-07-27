# a-greedy-algorithm-for-efficient-implementation-of-data-cubes-in-python
Based on the paper "Implementing data cubes efficiently" by V. Harinarayan, et al

Decision support applications involve complex queries on very large databases. Since response times should be small, query optimization is critical. A common and powerful query optimization technique is to materialize only some views rather than compute them from raw data each time. This code snippet uses a greedy algorithm to determine a good set of views to materialize.
