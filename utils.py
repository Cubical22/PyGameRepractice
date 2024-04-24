import math

def dis_point_from_line_by_points(line_point_A, line_point_B, point):
    if line_point_A[0] == line_point_B[0]: # if the line has no slope
        return math.fabs(line_point_A[0] - point[0])

    # the slope of the line passing the two A and B defining points
    m = (line_point_A[1] - line_point_B[1]) / (line_point_A[0] - line_point_B[0])

    # refer to ./ideas/point_dis.png for knowing where this came from
    d = math.fabs(point[1] - m * point[0] + m * line_point_A[0] - line_point_A[1]) / math.sqrt(1 + m ** 2)

    return d # returns the distance