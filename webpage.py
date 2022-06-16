import streamlit as st
import numpy as np
from logic import SudokoSolover
from PIL import Image

from imgreader import extract
from img_interpreter import CNN_interpret, intepretation2text, render_solution

def read_manual_input(placeholders, options, c_cols):
    for i_col in range(9):
            with c_cols[i_col]:
                for i_row in range(9):
                    key = f"{i_row}_{i_col}"
                    options[i_row][i_col] = placeholders[i_row][i_col].selectbox(
                        '',
                        ('', 1, 2, 3, 4, 5, 6, 7, 8, 9),
                        key=key,
                        index=0)

if 'mode' not in st.session_state:
    st.session_state['mode'] = None
if 'cam_input' not in st.session_state:
    st.session_state['cam_input'] = None



st.title("Sudoku Solver")
st.markdown("""
You can use this service if you ever get stuck on a Sudoku.
For the time being, the full solution is revealed, but I plan to make fields visible one by one.  
The Sudoko can either be entered manually or via camera/webcam.
""")

st.warning("The camera input does not work reliably yet, you probably have to fix the result. An update is coming.")

st.markdown(
    """
    <style>
    [data-baseweb="select"] {
        margin-top: -44px;
        margin-left: 0px;
        margin-right: 0px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.session_state.mode = st.selectbox('Select input method', ('Manual', "Read by camera"))
placeholders=[[None for _ in range(9)] for _ in range(9)]
options=[[None for _ in range(9)] for _ in range(9)]
c1, c2, c3, s1, c4, c5, c6, s2, c7, c8, c9 = st.columns([5,5,5,1,5,5,5, 1, 5,5,5])
c_cols = [c1, c2, c3, c4, c5, c6, c7, c8, c9]

# Create placeholders
for i_col in range(9):
    with c_cols[i_col]:
        for i_row in range(9):
            placeholders[i_row][i_col] = st.empty()
            if (i_row+1)%3==0 and i_row!=8:
                st.markdown("")

solve_button = st.button("Solve")


if st.session_state.mode=='Manual':
    read_manual_input(placeholders, options, c_cols)
else:
    st.session_state.cam_input = st.camera_input(label='aa')


if st.session_state.cam_input:
    img = Image.open(st.session_state.cam_input)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)
    img_array = np.rot90(img_array)
    extracted = extract(img_array)


    interpretations = CNN_interpret(extracted)

    for i_col in range(9):
        with c_cols[i_col]:
            for i_row in range(9):
                key=f"{i_row}_{i_col}"
                options[i_row][i_col]=placeholders[i_row][i_col].selectbox(
                    '',
                    ('', 1, 2, 3, 4, 5, 6, 7, 8, 9),
                    key=key,
                    index=int(interpretations[i_row][i_col]))



if solve_button:

    arr = [[val if type(val)==int else 0 for val in row ] for row in options]

    # For debug purposes
    # arr = [
    #     [5, 3, 0,  0, 7, 0,  0, 0, 0],
    #     [6, 0, 0,  1, 9, 5,  0, 0, 0],
    #     [0, 9, 8,  0, 0, 0,  0, 6, 0],
    #
    #     [8, 0, 0,  0, 6, 0,  0, 0, 3],
    #     [4, 0, 0,  8, 0, 3,  0, 0, 1],
    #     [7, 0, 0,  0, 2, 0,  0, 0, 6],
    #
    #     [0, 6, 0,  0, 0, 0,  2, 8, 0],
    #     [0, 0, 0,  4, 1, 9,  0, 0, 5],
    #     [0, 0, 0,  0, 8, 0,  0, 7, 9],
    #  ]
    A=np.array(arr)

    solver = SudokoSolover(A)
    solution = solver.solve()
    if 0 in solution:
        st.error(f"Could not solve sudoku. Check input!")
        with st.expander("See solution"):
            img = render_solution(arr, solution)
            st.image(img)
    else:
        st.success(f"Solution found!")
        st.balloons()
        with st.expander("See solution"):
            img = render_solution(arr, solution)
            st.image(img)

