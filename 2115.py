from typing import List


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        result = []
        dep = {s: set() for s in supplies}

        for rec, ing in zip(recipes, ingredients):
            dep[rec] = set(ing)

        def dfs(rec: str, visited: set = set()):
            if rec not in dep or rec in visited:
                return False

            visited.add(rec)
            for ing in list(dep[rec]):
                if not dfs(ing, visited):
                    return False

                dep[rec].remove(ing)
            visited.remove(rec)
            return True

        for rec in recipes:
            if dfs(rec):
                result.append(rec)

        return result
