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

  # Map each allergen to list of foods containing them
  # Map each allergen to a set of possible ingredients ("possibilities").
  #  ^^ Remember each allergen is really in exactly one of those ingredients
  #
  # Find an allergen that maps to just one ingredient
  #  Remove the ingredient from other allergen's possibility lists.
  #  Repeat until no more allergens have only one possibility.
  #
  # Print out the possibility lists and see what the situation is

  # Maps allergen string to a set of foods (as ints) containing the allergen
  print(parsed)
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

  # Map of allergen to ingredient
  identified_allergens = dict()

  while (True):
    newly_decisive_allergen = None
    for allergen in allergen_to_possible_ingredients.keys():
      if len(allergen_to_possible_ingredients[allergen]) == 1:
        newly_decisive_allergen = allergen
        break
    if not newly_decisive_allergen:
      break

    identified_allergens[newly_decisive_allergen] = (
      list(allergen_to_possible_ingredients[newly_decisive_allergen])[0])
    del allergen_to_possible_ingredients[newly_decisive_allergen]
    for possibilities in allergen_to_possible_ingredients.values():
      possibilities.discard(identified_allergens[newly_decisive_allergen])
      assert len(possibilities) > 0, 'Conflict'

  assert not allergen_to_possible_ingredients, 'Ambiguity'

  print('Done with first pass')
  print('allergen_to_possible_ingredients', allergen_to_possible_ingredients)
  print('identified_allergens', identified_allergens)
  
  return ','.join([identified_allergens[allergen] for allergen in sorted(identified_allergens.keys())])


if __name__ == '__main__':
    print(solve('input.txt'))