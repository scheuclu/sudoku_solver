import cv2
import torch
from models import FLAT, CNN
import torch.nn.functional as F
import numpy as np
import os
from google.cloud import vision
import asyncio

from google.oauth2 import service_account
from google.cloud import storage
import streamlit as st

# Create API client.
credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"])
client = storage.Client(credentials=credentials)

def intepretation2text(result):
    s=""
    for row in range(9):
        for col in range(9):
            s=s+f"{result[row][col]} "
        s=s+"\n"
    return s

async def interpret_cell(cellimage):
    img_encode = cv2.imencode('.png', cellimage)[1]
    content = img_encode.tobytes()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    # print(response)
    texts = response.text_annotations
    if len(texts) == 0:
        return 0
    try:
        detected = texts[0].description
        if int(detected)<10 and int(detected)>0:
            return int(detected)
        return 0
    except:
        return 0

async def GCP_interpret(extracted):

    flatttened = []
    for irow in range(9):
        for icol in range(9):
            flatttened.append(extracted[irow][icol])
    flat_results = await asyncio.gather(*map(interpret_cell, flatttened))
    result = []
    for irow in range(9):
        row = []
        for icol in range(9):
            row.append(flat_results[irow*9+icol])
        result.append(row)

    return result



def cell2pred(model, resized):

    x = resized / resized.max()
    x = x.astype(float)
    t = torch.from_numpy(x)
    t = t[None, None, :]
    t = t.type(torch.FloatTensor)
    logits = model(t)
    probabilities = F.softmax(logits, dim=-1)
    max_prob = torch.max(probabilities)
    if max_prob<0.5:
        return 0
    index = torch.argmax(probabilities)
    return index


# def CNN_interpret(extracted):
#
#     model = CNN() # we do not specify pretrained=True, i.e. do not load default weights
#     model.load_state_dict(torch.load('CNN_MNIST.pth'))
#     model.eval()
#
#     result = [[None for _ in range(9)] for _ in range(9)]
#
#     for row in range(9):
#         for col in range(9):
#             img=extracted[row][col]
#             img = img[10:40][10:40]
#             resized = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)
#             cv2.imwrite(f"cells/{row}_{col}.png", resized)
#             x = resized / resized.max()
#             if x.std().round(2)>0.2:
#                 pred=cell2pred(model, resized)
#                 result[row][col]=pred
#             else:
#                 result[row][col] = 0
#
#     return result


def render_solution(initial, solution):
    img = np.ones((900, 900, 3), np.uint8)*255

    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 50)
    fontScale = 1
    linecolor = (0, 0, 0)

    cv2.line(img, (0, 0), (0, 900), linecolor, 20)
    cv2.line(img, (900, 0), (900, 900), linecolor, 20)
    cv2.line(img, (0, 0), (900, 0), linecolor, 20)
    cv2.line(img, (0, 900), (900, 900), linecolor, 20)

    cv2.line(img, (310, 0), (310, 900), linecolor, 5)
    cv2.line(img, (610, 0), (610, 900), linecolor, 5)
    cv2.line(img, (0, 300), (900, 300), linecolor, 5)
    cv2.line(img, (0, 600), (900, 600), linecolor, 5)

    for i in range(8):
        cv2.line(img, (110 + i * 100, 0), (110 + i * 100, 900), linecolor, 1)
        cv2.line(img, (0, 98 + i * 100), (900, 98 + i * 100), linecolor, 1)

    for row in range(9):
        for col in range(9):
            loc = (100 * col + 50, 100 * row + 50)
            sol = solution[row][col]
            ###print("init:", initial[row][col])
            if int(initial[row][col])==0 or initial[row][col]=='':
                color = (100, 100, 100)
                thickness = 2
            else:
                color = (0, 0, 0)
                thickness = 4

            if sol==0:
                t=''
            else:
                t=str(solution[row][col])
            img = cv2.putText(img, t, loc, font, fontScale, color, thickness, cv2.LINE_AA)

    return img
