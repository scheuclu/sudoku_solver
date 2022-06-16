import streamlit as st
import numpy as np
import pandas as pd
from main import SudokoSolover, format_ouput

st.title("Sudoko Solver")
st.markdown("""
For the time being, you need to enter the sudoko manually.
I plan to add computer vision input in the future.
Once you entered what you have, click "Solve" on the bottom
""")

st.markdown(
    """
    <style>
    [data-baseweb="select"] {
        margin-top: -40px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

placeholder = st.empty()
#test = placeholder.text_input(label='')
test = placeholder.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), index=3, key='a11')

c1, c2, c3, s1, c4, c5, c6, s2, c7, c8, c9 = st.columns([3,3,3,1,3,3,3, 1, 3,3,3])
#a, b = st.columns([9,9])
with c1:
    option11 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='11')
    option21 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='21')
    option31 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='31')
    st.markdown("---")
    option41 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='41')
    option51 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='51')
    option61 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='61')
    st.markdown("---")
    option71 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='71')
    option81 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='81')
    option91 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='91')
with c2:
    option12 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='12')
    option22 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='22')
    option32 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='32')
    st.markdown("---")
    option42 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='42')
    option52 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='52')
    option62 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='62')
    st.markdown("---")
    option72 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='72')
    option82 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='82')
    option92 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='92')
with c3:
    option13 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='13')
    option23 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='23')
    option33 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='33')
    st.markdown("---")
    option43 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='43')
    option53 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='53')
    option63 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='63')
    st.markdown("---")
    option73 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='73')
    option83 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='83')
    option93 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='93')



with c4:
    option14 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='14')
    option24 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='24')
    option34 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='34')
    st.markdown("---")
    option44 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='44')
    option54 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='54')
    option64 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='64')
    st.markdown("---")
    option74 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='74')
    option84 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='84')
    option94 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='94')
with c5:
    option15 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='15')
    option25 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='25')
    option35 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='35')
    st.markdown("---")
    option45 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='45')
    option55 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='55')
    option65 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='65')
    st.markdown("---")
    option75 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='75')
    option85 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='85')
    option95 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='95')
with c6:
    option16 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='16')
    option26 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='26')
    option36 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='36')
    st.markdown("---")
    option46 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='46')
    option56 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='56')
    option66 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='66')
    st.markdown("---")
    option76 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='76')
    option86 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='86')
    option96 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='96')


with c7:
    option17 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='17')
    option27 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='27')
    option37 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='37')
    st.markdown("---")
    option47 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='47')
    option57 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='57')
    option67 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='67')
    st.markdown("---")
    option77 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='77')
    option87 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='87')
    option97 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='97')
with c8:
    option18 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='18')
    option28 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='28')
    option38 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='38')
    st.markdown("---")
    option48 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='48')
    option58 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='58')
    option68 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='68')
    st.markdown("---")
    option78 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='78')
    option88 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='88')
    option98 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='98')
with c9:
    option19 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='19')
    option29 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='29')
    option39 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='39')
    st.markdown("---")
    option49 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='49')
    option59 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='59')
    option69 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='69')
    st.markdown("---")
    option79 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='79')
    option89 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='89')
    option99 = st.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), key='99')


solve_button = st.button("Solve")
if solve_button:
    A=np.array(
        [
            [option11, option12, option13, option14, option15, option16, option17, option18, option19 ],
            [option21, option22, option23, option24, option25, option26, option27, option28, option29],
            [option31, option32, option33, option34, option35, option36, option37, option38, option39],
            [option41, option42, option43, option44, option45, option46, option47, option48, option49],
            [option51, option52, option53, option54, option55, option56, option57, option58, option59],
            [option61, option62, option63, option64, option65, option66, option67, option68, option69],
            [option71, option72, option73, option74, option75, option76, option77, option78, option79],
            [option81, option82, option83, option84, option85, option86, option87, option88, option89],
            [option91, option92, option93, option94, option95, option96, option97, option98, option99],
        ])

    A = np.where(A == '', 0, A).astype('int')

    input = placeholder.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), index=5, key='a11')
    solver = SudokoSolover(A)
    solution = solver.solve()
    st.success("Solution found!")
    st.text(f"Solution:\n{format_ouput(solution)}")

