import pandas as pd
import nltk
from .config import measures, words_to_remove
import string
import ast
import re
import unidecode
from nltk.stem import WordNetLemmatizer


def ingredient_parser(ingreds):
    if isinstance(ingreds, list):
        ingredients = ingreds
    else:
        ingredients = ast.literal_eval(ingreds)
    translator = str.maketrans('', '', string.punctuation)
    lemmatizer = WordNetLemmatizer()
    ingred_list = []
    for i in ingredients:
        i.translate(translator)
        items = re.split(' |-', i)
        items = [word for word in items if word.isalpha()]
        items = [word.lower() for word in items]
        items = [unidecode.unidecode(word) for word in items]
        items = [lemmatizer.lemmatize(word) for word in items]
        items = [word for word in items if word not in measures]
        items = [word for word in items if word not in words_to_remove]
        if items:
            ingred_list.append(' '.join(items))
    ingred_list = " ".join(ingred_list)

    return ingred_list


if __name__ == "__main__":
    # recipe_df = pd.read_csv('./ml_models/input/df_recipes.csv')
    # recipe_df['ingredients_parsed'] = recipe_df['ingredients'].apply(lambda x: ingredient_parser(x))
    #
    # df = recipe_df[['recipe_name', 'ingredients_parsed', 'ingredients', 'recipe_urls']]
    # df = recipe_df.dropna()
    #
    # m = df.recipe_name.str.endswith('Recipe - Allrecipes.com')
    #
    # df['recipe_name'].loc[m] = df.recipe_name.loc[m].str[:-23]
    # print(df)
    import json
    import os

    current_directory = os.path.dirname(__file__)
    parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
    # data_directory = os.path.join(parent_directory, 'data')
    files_path = os.path.join(parent_directory, 'core\\ml_models\\input')
    recipe_df = pd.read_csv(f'{files_path}\\df_recipes.csv')


    # files_in_data_directory = os.listdir(data_directory)
    new_df = recipe_df[857:]
    new_df.to_csv(f'{files_path}\\df_recipes.csv')

    # print(files_path)