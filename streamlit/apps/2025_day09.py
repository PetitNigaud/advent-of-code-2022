import streamlit as st
from plotly import graph_objects as go
from typing import List, Tuple

Point   = Tuple[float, float]
Polygon = List[Point]

def point_on_segment(p: Point, a: Point, b: Point) -> bool:
    """
    Return True if p lies on the (closed) segment ab.
    Works for both horizontal and vertical segments.
    """
    (px, py), (ax, ay), (bx, by) = p, a, b
    # first check collinearity: cross‑product == 0
    if (bx - ax) * (py - ay) != (by - ay) * (px - ax):
        return False
    # then check that p lies between a and b
    return min(ax, bx) <= px <= max(ax, bx) and min(ay, by) <= py <= max(ay, by)

def _segments_intersect(a1: Point, a2: Point, b1: Point, b2: Point) -> bool:
    """
    Return True only if the two *open* segments a1–a2 and b1–b2 intersect.
    • Colinear & overlapping (or just touching) → False
    • Perpendicular crossing at a point that lies *strictly* inside
      both segments → True
    • Intersection that coincides with an endpoint of either segment → False
    """
    # Helper: is the segment vertical?
    def is_vert(p1, p2):
        return p1[0] == p2[0]

    # 1. Same orientation: both vertical or both horizontal
    if is_vert(a1, a2) == is_vert(b1, b2):
        # If both vertical
        if is_vert(a1, a2):
            if a1[0] != b1[0]:  # parallel, different x → no intersection
                return False
            # Overlap in y‑range?
            ay_min, ay_max = sorted([a1[1], a2[1]])
            by_min, by_max = sorted([b1[1], b2[1]])
            # Strict overlap (excluding a single touching point)
            return max(ay_min, by_min) < min(ay_max, by_max)
        # Both horizontal
        if a1[1] != b1[1]:
            return False
        ax_min, ax_max = sorted([a1[0], a2[0]])
        bx_min, bx_max = sorted([b1[0], b2[0]])
        return max(ax_min, bx_min) < min(ax_max, bx_max)

    # 2. Perpendicular: one vertical, one horizontal
    # Ensure a is vertical, b is horizontal
    if not is_vert(a1, a2):
        a1, a2, b1, b2 = b1, b2, a1, a2

    # a is vertical, b horizontal
    vx = a1[0]
    hy = b1[1]
    ay_min, ay_max = sorted([a1[1], a2[1]])
    bx_min, bx_max = sorted([b1[0], b2[0]])

    # Check if intersection point lies strictly inside both segments
    inside_v = (ay_min < hy < ay_max)      # vertical segment interior
    inside_h = (bx_min < vx < bx_max)      # horizontal segment interior

    return inside_v and inside_h

number_params = dict(min_value = 0, max_value = 10, step=1)

st.header("Line definition")
st.write("Line 1 (P1, P2) (horizontal)")
cols = st.columns(4)
x1 = cols[0].number_input("x1", value=0, **number_params)
y1 = cols[1].number_input("y1", value=1, **number_params)
x2 = cols[2].number_input("x2", value=2, **number_params)
y2 = y1#cols[3].number_input("y2", value=1, **number_params)
st.write("Line 2 (P3, P4) (vertical)")
cols = st.columns(4)
x3 = cols[0].number_input("x3", value=1, **number_params)
y3 = cols[1].number_input("y3", value=0, **number_params)
x4 = x3#cols[2].number_input("x4", value=1, **number_params)
y4 = cols[3].number_input("y4", value=2, **number_params)

P1 = (x1, y1)
P2 = (x2, y2)
P3 = (x3, y3)
P4 = (x4, y4)

st.markdown(f"P3 on Line 1 `{point_on_segment(P3, P1, P2)}`")
st.markdown(f"P4 on Line 1 `{point_on_segment(P4, P1, P2)}`")
st.markdown(f"Lines intersect `{_segments_intersect(P1, P2, P3, P4)}`")

fig = go.Figure()
fig.add_trace(go.Scatter(x=[x1, x2], y=[y1, y2], name=f"Line1 ({x1}, {y1}) -> ({x2}, {y2})"))
fig.add_trace(go.Scatter(x=[x3, x4], y=[y3, y4], name=f"Line2 ({x3}, {y4}) -> ({x4}, {y4})"))
#fig.show()
fig.update_layout(yaxis_scaleanchor="x", width=800, height=800)
st.plotly_chart(fig)
