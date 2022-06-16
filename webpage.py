import streamlit as st
import numpy as np
import pandas as pd
from main import SudokoSolover, format_ouput
from PIL import Image

from imgreader import extract
from img_interpreter import CNN_interpret, intepretation2text, render_solution


if 'mode' not in st.session_state:
    st.session_state['mode'] = None



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
        margin-top: -44px;
        margin-left: 0px;
        margin-right: 0px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.session_state.mode = st.selectbox('Select input method', ('Manual', "Read by camera"))


if st.session_state.mode=='Manual':
    st.text("Manual")
else:
    st.text("Camera")
    cam_input = st.camera_input(label='aa')

manual_button = st.button("Enter manually instead")

# placeholder = st.empty()
#test = placeholder.text_input(label='')
# test = placeholder.selectbox('', ('', 1, 2, 3, 4, 5, 6, 7, 8, 9), index=3, key='a11')


placeholders=[[None for _ in range(9)] for _ in range(9)]
options=[[None for _ in range(9)] for _ in range(9)]

c1, c2, c3, s1, c4, c5, c6, s2, c7, c8, c9 = st.columns([5,5,5,1,5,5,5, 1, 5,5,5])
c_cols = [c1, c2, c3, c4, c5, c6, c7, c8, c9]

for i_col in range(9):
    with c_cols[i_col]:
        for i_row in range(9):
            placeholders[i_row][i_col] = st.empty()
            if (i_row+1)%3==0 and i_row!=8:
                st.markdown("")
                #st.markdown("<p><span style='background-color: #0000ff;'>---</span></p>",unsafe_allow_html=True)

solve_button = st.button("Solve")



if cam_input:
    img = Image.open(cam_input)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)
    img_array = np.rot90(img_array)
    extracted = extract(img_array)

    # st.text("Here's what has been detected")
    # cols = st.columns(9)
    # for icol in range(9):
    #     with cols[icol]:
    #         for irow in range(9):
    #           #st.text(extracted[irow][icol].shape)
    #           st.image(extracted[irow][icol])



    #st.text(f"{extracted}")
    interpretations = CNN_interpret(extracted)
    #st.text(intepretation2text(interpretations))



    for i_col in range(9):
        with c_cols[i_col]:
            for i_row in range(9):
                key=f"{i_row}_{i_col}"
                options[i_row][i_col]=placeholders[i_row][i_col].selectbox(
                    '',
                    ('', 1, 2, 3, 4, 5, 6, 7, 8, 9),
                    key=key,
                    index=int(interpretations[i_row][i_col]))


if manual_button:
    for i_col in range(9):
        with c_cols[i_col]:
            for i_row in range(9):
                key = f"{i_row}_{i_col}"
                options[i_row][i_col] = placeholders[i_row][i_col].selectbox(
                    '',
                    ('', 1, 2, 3, 4, 5, 6, 7, 8, 9),
                    key=key,
                    index=0)



if solve_button:

    arr = [[val if type(val)==int else 0 for val in row ] for row in options]
    ###st.text(f"{arr}")
    A=np.array(arr)
    ###st.text(f"{A}")

    solver = SudokoSolover(A)
    solution = solver.solve()
    if 0 in solution:
        st.error(f"Could not solve sudoku. Check input!")
        with st.expander("See solution"):
            img = render_solution(solution)
            st.image(img)
    else:
        st.success(f"Solution found!")
        st.balloons()
        with st.expander("See solution"):
            img = render_solution(solution)
            st.image(img)
    #st.text(f"Solution:\n{format_ouput(solution)}")

