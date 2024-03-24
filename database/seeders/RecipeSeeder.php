<?php

namespace Database\Seeders;

use App\Models\Recipe;
use App\Models\User;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class RecipeSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $users = User::all()->pluck("id")->toArray();

        foreach ($users as $user_id) {
            Recipe::create([
                'user_id' => $user_id,
                'title' => fake()->sentence,
                'description' => fake()->paragraph,
                'instructions' => fake()->randomHtml,
                'prep_time' => fake()->text,
                'cook_time' => fake()->sentence(2),
                'total_time' => fake()->sentence(2),
                'servings' => fake()->randomDigit,
                'image_url' => fake()->imageUrl(640, 480, 'animals', true),
                'premium' => fake()->randomElement([true, false]),
                'ingredients' => json_encode(array_fill(0, 3, [
                    'name' => fake()->sentence,
                    'amount' => fake()->randomNumber(2, false),
                    'unit' => fake()->randomElement(['g', 'kg', 'ml', 'l', 'cup', 'piece']),
                ])),
                'nutritional_info' => json_encode([
                    'calories' => fake()->randomFloat(2, 0, 1000),
                    'saturated_fat' => fake()->randomFloat(2, 0, 1000),
                    'carbohydrates' => fake()->randomFloat(2, 1, 1000),
                    'protein' => fake()->randomFloat(2, 1, 1000)

                ]),
            ]);
        };

        // Add Collaborators to recipes
        $recipes = Recipe::all(); // Get all users. This will prevent Eloquent from having to re-run queries subsequently

        foreach ($recipes->random(floor($recipes->count() * 0.5)) as $recipe) { // Half the recipies in our collection will have collaborators
            $users = User::whereNot('id', $recipe->creator->id)->inRandomOrder()->take(fake()->numberBetween(1, 3))->get(); // Get 1-3 users that are not the recipe's creator

            foreach ($users as $user) {
                $recipe->collaborators()->attach($user); // Populate the pivot table
            }
        };

        // Add likes to Recipes
        $recipes = Recipe::all();

        foreach ($recipes->random(floor($recipes->count() * 0.9)) as $recipe) { // At least 90% of our recipies will have > 1 like
            $users = User::whereNot('id', $recipe->creator->id)->inRandomOrder()->get();
            foreach ($users->take(fake()->numberBetween(1, floor($user->count() * 0.6))) as $user) { // At least 60% of our users will have liked a recipe
                $user->liked_recipes()->attach($recipe);
            }
        };


        // Add ratings for different recipes
        /*
         * Todo: Add ratings to pivot table such that onlu users who've liked a recipe should rate it 3 stars and above
         * and other recipies can get rated between 1 and 2. Note that not all recipes should have ratings
         */
    }
}
