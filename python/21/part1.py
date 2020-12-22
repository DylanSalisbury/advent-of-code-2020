import itertools
import util

def solve(input_path):
  f = open(input_path)
  parsed = util.parse(f)

  num_foods = len(parsed)
  allergens = set()
  ingredients = set()
  for pair in parsed:
    for ingredient in pair[0]:
      ingredients.add(ingredient)
    for allergen in pair[1]:
      allergens.add(allergen)
  print('Number of foods and allergens:', num_foods, len(allergens))

  # Maps allergen string to a set of foods (as ints) containing the allergen
  allergen_to_food = dict()
  for allergen in allergens:
    allergen_to_food[allergen] = set([
      index for index in range(num_foods) if allergen in parsed[index][1]
    ])
  print('allergen_to_food', allergen_to_food)

  # Maps allergen to a set (which will be modified) of ingredients.
  # In truth exactly one ingredient contains the allergen.
  allergen_to_possible_ingredients = dict()
  for allergen in allergens:
    for food in allergen_to_food[allergen]:
      new_set = set(parsed[food][0])
      if allergen not in allergen_to_possible_ingredients:
        allergen_to_possible_ingredients[allergen] = new_set
      else:
        allergen_to_possible_ingredients[allergen] = (
          allergen_to_possible_ingredients[allergen].intersection(new_set)
        )
  print('allergen_to_possible_ingredients', allergen_to_possible_ingredients)

  suspicious_ingredients = set(itertools.chain.from_iterable([
    allergen_to_possible_ingredients[allergen] for allergen in allergens
  ]))
  clear_ingredients = [
    ingredient for ingredient in ingredients if ingredient not in suspicious_ingredients]
  print('sus', list(suspicious_ingredients))
  print('clear', list(clear_ingredients))
  print(parsed)

  result = 0
  for pair in parsed:
    result += sum([1 for ingredient in pair[0] if ingredient in clear_ingredients])
  return result

if __name__ == '__main__':
    print(solve('input.txt'))