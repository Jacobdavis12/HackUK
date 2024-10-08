from PIL import Image
import base64
from mistralai import Mistral
from io import BytesIO
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import json
from utils import decode_image_base64, encode_image_base64, save_ingredients_as_json
from llms import mistral
from prompts import generate_shopping

def get_shopping(ingredients, client, model, personal_details =None):
    # Analyze the image and get the ingredients list
    recipes = mistral(None, client, model, generate_shopping + str(ingredients), personal_details = personal_details)

    return recipes