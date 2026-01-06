from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("name")
        recipe_description = data.get("description")
        recipe_image = request.FILES.get("image")
        # print(recipe_name)
        # print(recipe_description)
        # print(recipe_image)

        Recipe.objects.create(
            name=recipe_name, description=recipe_description, image=recipe_image
        )

        return redirect("/recipes")
    
    queryset = Recipe.objects.all()
    context = {"recipes": queryset}

    return render(request, 'recipes.html', context)

def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)

    if request.method == "POST":
        data = request.POST
        recipe.name = data.get("name")
        recipe.description = data.get("description")
        if request.FILES.get("image"):
            recipe.image = request.FILES.get("image")
        recipe.save()
        return redirect("/recipes/")

    context = {"recipe": recipe}
    return render(request, 'edit_recipes.html', context)

def delete_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    recipe.delete()
    return redirect("/recipes/")