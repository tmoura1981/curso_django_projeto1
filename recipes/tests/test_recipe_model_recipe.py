from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65)
    ]
    )
    def teste_recipe_fields_max_lengh(self, field, max_lengh):
        setattr(self.recipe, field, 'A' * (max_lengh + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
