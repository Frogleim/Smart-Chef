import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import unidecode, ast
from .ingredients_parser import ingredient_parser
from . import config


def get_recommendations(N, scores):
    df_recipes = pd.read_csv(config.PARSED_DF)
    top = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:N]
    recommendation = pd.DataFrame(columns=['recipe', 'ingredients', 'score', 'url'])
    count = 0
    for i in top:
        print(i)
        recommendation.at[count, 'recipe'] = title_parser(df_recipes['recipe_name'][i])
        recommendation.at[count, 'ingredients'] = ingredient_parser_final(df_recipes['ingredients'][i])
        recommendation.at[count, 'url'] = df_recipes['recipe_urls'][i]
        recommendation.at[count, 'score'] = "{:.3f}".format(float(scores[i]))
        count += 1
    return recommendation


def ingredient_parser_final(ingredient):
    if isinstance(ingredient, list):
        ingredients = ingredient
    else:
        ingredients = ast.literal_eval(ingredient)

    ingredients = ','.join(ingredients)
    ingredients = unidecode.unidecode(ingredients)
    return ingredients


def title_parser(title):
    title = unidecode.unidecode(title)
    return title


def RecSys(ingredients, N=8):
    with open(config.ENCODING_TF, 'rb') as f:
        tfidf_encodings = pickle.load(f)

    with open(config.TFK, "rb") as f:
        tfidf = pickle.load(f)

    try:
        ingredients_parsed = ingredient_parser(ingredients)
    except Exception:
        ingredients_parsed = ingredient_parser([ingredients])

    ingredients_tfidf = tfidf.transform([ingredients_parsed])
    cos_sim = map(lambda x: cosine_similarity(ingredients_tfidf, x), tfidf_encodings)
    scores = list(cos_sim)
    recommendations = get_recommendations(N, scores)
    response = {}
    rec = []
    count = 0
    for index, row in recommendations.iterrows():
        response = {
            'recipe': str(row['recipe']),
            'score': str(row['score']),
            'ingredients': str(row['ingredients']),
            'url': str(row['url'])
        }
        rec.append(response)
    return rec


if __name__ == '__main__':
    test_ingredients = "pasta, tomato, onion"
    recs = RecSys(test_ingredients)
    print(recs)
