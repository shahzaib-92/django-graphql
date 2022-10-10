import graphene
from graphene_django import DjangoObjectType
from ingredients.models import Category, Ingredient
from ingredients import schema as ingredient_schema


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")


class Query(ingredient_schema.Query, graphene.ObjectType):
    pass
    # all_ingredients = graphene.List(IngredientType)
    # category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
    #
    # @staticmethod
    # def resolve_all_ingredients(root, info):
    #     # We can easily optimize query count in the resolve method
    #     return Ingredient.objects.select_related("category").all()
    #
    # @staticmethod
    # def resolve_category_by_name(root, info, name):
    #     try:
    #         return Category.objects.get(name=name)
    #     except Category.DoesNotExist:
    #         return None


main_schema = graphene.Schema(query=Query)
