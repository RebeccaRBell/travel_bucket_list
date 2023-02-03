from flask import Flask, render_template, request, redirect
from flask import Blueprint

countries_blueprint = Blueprint("countries", __name__)
