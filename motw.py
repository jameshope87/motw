import os
import string
import random

#molecule list, to be replaced in the future by a more comprehensive one!
molecules = {'Hexane': 'Hexane is a saturated hydrocarbon, it is used as a fuel and that\'s about it'}

#opens the current webpage
def open_page():
    with open("index.html", "r") as f:
        oldpage = f.read()
    return oldpage


def find_section(page):
    start = page.find('<div class="motw">')
    end = page.find('</div>', start)
#    section = page[start:end]
    return start, end

def pick_molecule(molecule_dict):
    return  random.choice(list(molecule_dict.items()))

def format_new(molecule, description):
    new_section = '<div class="motw">\n <h2> Below you will find my molecule of the week </h2>\n<h3>' + molecule + '</h3>\n<p>' + description + '</p>\n</div>'
    return new_section
    
def make_new(molecule, description, page):
    start, end = find_section(page)
    new_page = page[:start] + format_new(molecule, description) + page[end:]
    return new_page

def write_file(molecule, description, page):
    with open("index.html", "w") as f:
        f.write(make_new(molecule, description, page))

oldpage = open_page()
molecule, description = pick_molecule(molecules)
write_file(molecule, description, oldpage)
